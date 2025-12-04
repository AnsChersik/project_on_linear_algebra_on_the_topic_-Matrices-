import sys
from PyQt6.QtWidgets import (
    QWidget, QApplication, QPushButton, QLineEdit, QLabel, QGridLayout, QMessageBox, QFileDialog
)
from PyQt6.QtCore import Qt

class Window_transposition_calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet('background-color: #464168')
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Матрица и транспонирование')
        self.setGeometry(500, 500, 600, 600)

        self.labelSizeMatric = QLabel('Введите размер матрицы (m x n):', self)
        self.labelSizeMatric.setStyleSheet('color: white; font-size: 16px; font-family: Verdana')
        self.labelSizeMatric.move(10, 10)

        self.inputM = QLineEdit(self)
        self.inputM.setStyleSheet('color: white; font-size: 16px; font-family: Verdana')
        self.inputM.move(10, 40)
        self.inputM.setFixedSize(150, 25)
        self.inputM.setPlaceholderText("m (строк)")

        self.inputN = QLineEdit(self)
        self.inputN.setStyleSheet('color: white; font-size: 16px; font-family: Verdana')
        self.inputN.move(170, 40)
        self.inputN.setFixedSize(150, 25)
        self.inputN.setPlaceholderText("n (столбцов)")

        self.buttonCreate = QPushButton('Создать матрицу', self)
        self.buttonCreate.move(400, 40)
        self.buttonCreate.setFixedSize(180, 28)
        self.buttonCreate.setStyleSheet('color: white; font-size: 14px; font-family: Verdana; background-color: MidnightBlue')
        self.buttonCreate.clicked.connect(self.create_matrix_inputs)

        self.buttonLoadFile = QPushButton('Загрузить из файла', self)
        self.buttonLoadFile.move(400, 10)
        self.buttonLoadFile.setFixedSize(180, 28)
        self.buttonLoadFile.setStyleSheet('color: white; font-size: 14px; font-family: Verdana; background-color: MidnightBlue')
        self.buttonLoadFile.clicked.connect(self.load_matrix_from_file)

        self.matrixInputs = QWidget(self)
        self.matrixInputs.setStyleSheet('color: white; font-size: 16px; font-family: Verdana')

        self.matrixLayout = QGridLayout()
        self.matrixInputs.setLayout(self.matrixLayout)
        self.matrixInputs.move(10, 80)
        self.matrixInputs.hide()

        self.buttonTransposer = QPushButton('Транспонировать', self)
        self.buttonTransposer.move(10, 200)
        self.buttonTransposer.setFixedSize(180, 28)
        self.buttonTransposer.setStyleSheet('color: white; font-size: 14px; font-family: Verdana; background-color: MidnightBlue')
        self.buttonTransposer.clicked.connect(self.transpose_matrix)
        self.buttonTransposer.hide()

        self.labelResults = QLabel('Транспонированная матрица:', self)
        self.labelResults.setStyleSheet('color: white; font-size: 16px; font-family: Verdana')
        self.labelResults.move(10, 280)
        self.labelResults.hide()

        self.resultMatrix = QWidget(self)
        self.resultMatrixLayout = QGridLayout()
        self.resultMatrix.setLayout(self.resultMatrixLayout)
        self.resultMatrix.move(10, 310)
        self.resultMatrix.hide()

        self.show()

    def create_matrix_inputs(self):
        for i in reversed(range(self.matrixLayout.count())):
            self.matrixLayout.itemAt(i).widget().deleteLater()

        try:
            self.m = int(self.inputM.text())
            self.n = int(self.inputN.text())
            if self.m <= 0 or self.n <= 0:
                raise ValueError
        except ValueError:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, введите корректные размеры матрицы")
            return

        self.inputs = []
        for i in range(self.m):
            row = []
            for j in range(self.n):
                lineEdit = QLineEdit()
                lineEdit.setStyleSheet('color: white; font-size: 16px; font-family: Verdana')
                lineEdit.setFixedWidth(50)
                self.matrixLayout.addWidget(lineEdit, i, j)
                row.append(lineEdit)
            self.inputs.append(row)

        self.matrixInputs.show()
        self.buttonTransposer.show()
        self.labelResults.hide()
        self.resultMatrix.hide()

    def load_matrix_from_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Выберите файл", "", "Text Files (*.txt)")
        if filename:
            try:
                with open(filename, 'r') as f:
                    lines = f.readlines()
                matrix = []
                for line in lines:
                    row_str = line.strip().split()
                    row = [float(x) for x in row_str]
                    matrix.append(row)
                if len(set(len(row) for row in matrix)) != 1:
                    QMessageBox.warning(self, "Ошибка", "Некорректный формат файла: строки разной длины")
                    return

                self.m = len(matrix)
                self.n = len(matrix[0])

                self.inputM.setText(str(self.m))
                self.inputN.setText(str(self.n))

                for i in reversed(range(self.matrixLayout.count())):
                    self.matrixLayout.itemAt(i).widget().deleteLater()

                self.inputs = []
                for i in range(self.m):
                    row = []
                    for j in range(self.n):
                        lineEdit = QLineEdit()
                        lineEdit.setStyleSheet('color: white; font-size: 16px; font-family: Verdana')
                        lineEdit.setFixedWidth(50)
                        lineEdit.setText(str(matrix[i][j]))
                        self.matrixLayout.addWidget(lineEdit, i, j)
                        row.append(lineEdit)
                    self.inputs.append(row)

                self.matrixInputs.show()
                self.buttonTransposer.show()
                self.labelResults.hide()
                self.resultMatrix.hide()

            except Exception as e:
                QMessageBox.warning(self, "Ошибка", f"Ошибка при чтении файла: {str(e)}")

    def transpose_matrix(self):
        matrix = []
        try:
            for i in range(self.m):
                row = []
                for j in range(self.n):
                    val = float(self.inputs[i][j].text())
                    row.append(val)
                matrix.append(row)
        except ValueError:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, введите корректные числа.")
            return

        transposed = list(map(list, zip(*matrix)))

        for i in reversed(range(self.resultMatrixLayout.count())):
            self.resultMatrixLayout.itemAt(i).widget().deleteLater()

        for i in range(len(transposed)):
            for j in range(len(transposed[0])):
                value = int(transposed[i][j])
                label = QLabel(str(value))
                label.setStyleSheet('color: white; font-size: 16px; font-family: Verdana')
                label.setFixedWidth(50)
                label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                self.resultMatrixLayout.addWidget(label, i, j)

        self.labelResults.show()
        self.resultMatrix.show()