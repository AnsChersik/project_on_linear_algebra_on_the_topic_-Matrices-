import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QLineEdit, QMessageBox, QGridLayout, QComboBox, QFileDialog
)
from PyQt6.QtCore import Qt

class Window_operations_calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Операции с матрицами")
        self.setStyleSheet('background-color: #464168; color: white; font-family: Verdana;')
        self.init_ui()

        self.m = 0
        self.n = 0
        self.matrix1 = []
        self.matrix2 = []

    def init_ui(self):
        self.mainLayout = QVBoxLayout()
        self.setLayout(self.mainLayout)

        self.topBar = QWidget()
        self.topLayout = QHBoxLayout()
        self.topBar.setLayout(self.topLayout)

        self.backButton = QPushButton("Назад")
        self.backButton.setFixedSize(100, 28)
        self.backButton.setStyleSheet('color: white; font-size: 14px; font-family: Verdana; background-color: MidnightBlue')
        self.backButton.clicked.connect(self.open_operation_window)

        self.topLayout.addWidget(self.backButton, alignment=Qt.AlignmentFlag.AlignLeft)
        self.topLayout.addStretch()

        self.mainLayout.addWidget(self.topBar)

        self.labelOperation = QLabel("Выберите операцию:")
        self.labelOperation.setStyleSheet('color: white; font-size: 16px; font-family: Verdana')
        self.operationComboBox = QComboBox()
        self.operationComboBox.addItems(["Сложение", "Вычитание", "Умножение на число"])

        self.buttonStart = QPushButton("Начать")
        self.buttonStart.setFixedSize(180, 28)
        self.buttonStart.setStyleSheet('color: white; font-size: 14px; font-family: Verdana; background-color: MidnightBlue')
        self.buttonStart.clicked.connect(self.start_operation)

        topLayout = QHBoxLayout()
        topLayout.addWidget(self.labelOperation)
        topLayout.addWidget(self.operationComboBox)
        topLayout.addWidget(self.buttonStart)

        self.buttonLoadFile = QPushButton("Загрузить из файла")
        self.buttonLoadFile.setFixedSize(180, 28)
        self.buttonLoadFile.setStyleSheet('color: white; font-size: 14px; font-family: Verdana; background-color: MidnightBlue')
        self.buttonLoadFile.clicked.connect(self.load_data_from_file)

        topLayout.addWidget(self.buttonLoadFile)

        self.mainLayout.addLayout(topLayout)

        self.inputArea = QWidget()
        self.inputLayout = QVBoxLayout()
        self.inputArea.setLayout(self.inputLayout)
        self.mainLayout.addWidget(self.inputArea)

        self.buttonsLayout = QHBoxLayout()
        self.buttonChange = QPushButton("Сменить операцию")
        self.buttonChange.setFixedSize(180, 28)
        self.buttonChange.setStyleSheet('color: white; font-size: 14px; font-family: Verdana; background-color: MidnightBlue')
        self.buttonChange.clicked.connect(self.reset_ui)

        self.buttonCalcut = QPushButton("Вычислить")
        self.buttonCalcut.setFixedSize(180, 28)
        self.buttonCalcut.setStyleSheet('color: white; font-size: 14px; font-family: Verdana; background-color: MidnightBlue')
        self.buttonCalcut.clicked.connect(self.calculate_result)

        self.buttonsLayout.addWidget(self.buttonChange)
        self.buttonsLayout.addWidget(self.buttonCalcut)

        self.mainLayout.addLayout(self.buttonsLayout)

        self.labelResult = QLabel()
        self.labelResult.setStyleSheet('color: white; font-size: 16px; font-family: Verdana')
        self.labelResult.setWordWrap(True)
        self.mainLayout.addWidget(self.labelResult)

        self.inputArea.hide()
        self.buttonChange.hide()
        self.buttonCalcut.hide()
        self.labelResult.hide()

        self.show()

    def start_operation(self):
        self.operation = self.operationComboBox.currentText()
        self.clear_input_area()
        self.labelResult.hide()

        sizeLayout = QHBoxLayout()
        self.inputRows = QLineEdit()
        self.inputRows.setStyleSheet('color: white; font-size: 16px; font-family: Verdana')
        self.inputRows.setPlaceholderText("Строки")

        self.inputCols = QLineEdit()
        self.inputCols.setStyleSheet('color: white; font-size: 16px; font-family: Verdana')
        self.inputCols.setPlaceholderText("Столбцы")

        self.lableRows = QLabel("Количество строк:")
        self.lableRows.setStyleSheet('color: white; font-size: 16px; font-family: Verdana')

        self.lableCols = QLabel("Количество столбцов:")
        self.lableCols.setStyleSheet('color: white; font-size: 16px; font-family: Verdana')


        sizeLayout.addWidget(self.lableRows)
        sizeLayout.addWidget(self.inputRows)
        sizeLayout.addWidget(self.lableCols)
        sizeLayout.addWidget(self.inputCols)

        self.inputLayout.addLayout(sizeLayout)

        self.buttonCreateMatric = QPushButton("Создать матрицы")
        self.buttonCreateMatric.setFixedSize(180, 28)
        self.buttonCreateMatric.setStyleSheet('color: white; font-size: 14px; font-family: Verdana; background-color: MidnightBlue')
        self.buttonCreateMatric.clicked.connect(self.create_matrices_inputs)
        self.inputLayout.addWidget(self.buttonCreateMatric)

        self.inputArea.show()
        self.buttonChange.show()
        self.buttonCalcut.show()

    def create_matrices_inputs(self):
        for i in reversed(range(self.inputLayout.count())):
            widget = self.inputLayout.itemAt(i).widget()
            if widget and widget != self.buttonCreateMatric:
                widget.deleteLater()

        try:
            self.m = int(self.inputRows.text())
            self.n = int(self.inputCols.text())
            if self.m <= 0 or self.n <= 0:
                raise ValueError
        except:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, введите корректные размеры.")
            return

        if hasattr(self, 'matrix1') and self.matrix1:
            return

        self.matrix1 = []
        self.matrix2 = []

        if self.operation in ["Сложение", "Вычитание"]:
            label1 = QLabel("Первая матрица:")
            label1.setStyleSheet('color: white; font-size: 16px; font-family: Verdana')
            label2 = QLabel("Вторая матрица:")
            label2.setStyleSheet('color: white; font-size: 16px; font-family: Verdana')
        
            self.inputLayout.addWidget(label1)
            self.matrix1Widget = QWidget()
            self.matrix1Layout = QGridLayout()
            self.matrix1Widget.setLayout(self.matrix1Layout)
            self.inputLayout.addWidget(self.matrix1Widget)

            self.inputLayout.addWidget(label2)
            self.matrix2Widget = QWidget()
            self.matrix2Layout = QGridLayout()
            self.matrix2Widget.setLayout(self.matrix2Layout)
            self.inputLayout.addWidget(self.matrix2Widget)

            for i in range(self.m):
                rowWidgets = []
                for j in range(self.n):
                    inp = QLineEdit()
                    inp.setStyleSheet('color: white; font-size: 16px; font-family: Verdana')
                    inp.setFixedWidth(50)
                    self.matrix1Layout.addWidget(inp, i, j)
                    rowWidgets.append(inp)
                self.matrix1.append(rowWidgets)

            for i in range(self.m):
                rowWidgets = []
                for j in range(self.n):
                    inp = QLineEdit()
                    inp.setStyleSheet('color: white; font-size: 16px; font-family: Verdana')
                    inp.setFixedWidth(50)
                    self.matrix2Layout.addWidget(inp, i, j)
                    rowWidgets.append(inp)
                self.matrix2.append(rowWidgets)

        elif self.operation == "Умножение на число":
            label = QLabel("Введите матрицу:")
            label.setStyleSheet('color: white; font-size: 16px; font-family: Verdana')
            self.inputLayout.addWidget(label)
            self.matrixSingleWidget = QWidget()
            self.matrixSingleLayout = QGridLayout()
            self.matrixSingleWidget.setLayout(self.matrixSingleLayout)
            self.inputLayout.addWidget(self.matrixSingleWidget)

            for i in range(self.m):
                rowWidgets = []
                for j in range(self.n):
                    inp = QLineEdit()
                    inp.setStyleSheet('color: white; font-size: 16px; font-family: Verdana')
                    inp.setFixedWidth(50)
                    self.matrixSingleLayout.addWidget(inp, i, j)
                    rowWidgets.append(inp)
                self.matrix1.append(rowWidgets)

            self.multiplyInput = QLineEdit()
            self.multiplyInput.setStyleSheet('color: white; font-size: 16px; font-family: Verdana')
            self.multiplyInput.setPlaceholderText("Коэффициент умножения")
            self.inputLayout.addWidget(self.multiplyInput)

        self.inputArea.show()

    def reset_ui(self):
        self.operationComboBox.setCurrentIndex(0)
        self.clear_input_area()
        self.labelResult.hide()
        self.matrix1 = []
        self.matrix2 = []

    def clear_input_area(self):
        for i in reversed(range(self.inputLayout.count())):
            widget = self.inputLayout.itemAt(i).widget()
            if widget:
                widget.deleteLater()

    def calculate_result(self):
        try:
            if self.operation in ["Сложение", "Вычитание"]:
                matrix_a = []
                matrix_b = []
                for i in range(self.m):
                    row_a = []
                    row_b = []
                    for j in range(self.n):
                        val_a = float(self.matrix1[i][j].text())
                        val_b = float(self.matrix2[i][j].text())
                        row_a.append(val_a)
                        row_b.append(val_b)
                    matrix_a.append(row_a)
                    matrix_b.append(row_b)

                result = []
                for i in range(self.m):
                    row_res = []
                    for j in range(self.n):
                        if self.operation == "Сложение":
                            row_res.append(matrix_a[i][j] + matrix_b[i][j])
                        else:
                            row_res.append(matrix_a[i][j] - matrix_b[i][j])
                    result.append(row_res)

            elif self.operation == "Умножение на число":
                matrix_a = []
                for i in range(self.m):
                    row_a = []
                    for j in range(self.n):
                        val_a = float(self.matrix1[i][j].text())
                        row_a.append(val_a)
                    matrix_a.append(row_a)

                k = float(self.multiplyInput.text())

                result = []
                for i in range(self.m):
                    row_res = []
                    for j in range(self.n):
                        row_res.append(matrix_a[i][j] * k)
                    result.append(row_res)

            result_str = "Результат:\n"
            for row in result:
                result_str += "  ".join(f"{int(round(x))}" for x in row) + "\n"
            self.labelResult.setText(result_str)
            self.labelResult.show()

        except:
            QMessageBox.warning(self, "Ошибка", "Ошибка при вычислении, проверьте вводимые данные.")

    def load_data_from_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Выберите файл", "", "Текстовые файлы (*.txt);;Все файлы (*)")
        if not filename:
            return
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            matrix = []
            for line in lines:
                rowStr = line.strip().split()
                row = [float(x) for x in rowStr]
                matrix.append(row)
            if len(set(len(row) for row in matrix)) != 1:
                QMessageBox.warning(self, "Ошибка", "Некорректный формат файла: строки разной длины")
                return

            if len(matrix) != 3:
                QMessageBox.warning(self, "Ошибка", "Файл должен содержать 3 строки.")
                return

            for i in range(3):
                for j in range(4):
                    if hasattr(self, 'matrix1') and self.matrix1:
                        self.matrix1[i][j].setText(str(matrix[i][j]))
                    if hasattr(self, 'matrix2') and self.matrix2:
                        self.matrix2[i][j].setText(str(matrix[i][j]))

        except Exception as e:
            QMessageBox.warning(self, "Ошибка", f"Не удалось загрузить файл: {e}")


    def open_operation_window(self):
        from window_operations import Window_operations
        self.MainWindow = Window_operations()
        self.MainWindow.show()
        self.close()

