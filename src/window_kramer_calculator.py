import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton,
    QMessageBox, QGridLayout, QFileDialog, QHBoxLayout
)
from PyQt6.QtCore import Qt

class Window_kramer_calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Калькулятор метода Крамера")
        self.setStyleSheet('background-color: #464168')
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self._init_ui()

    def _init_ui(self):
        self.topBar = QWidget()
        self.topLayout = QHBoxLayout()
        self.topBar.setLayout(self.topLayout)

        self.backButton = QPushButton("Назад")
        self.backButton.setFixedSize(100, 28)
        self.backButton.setStyleSheet(
            'color: white; font-size: 14px; font-family: Verdana; background-color: MidnightBlue'
        )
        self.backButton.clicked.connect(self.open_kramer_window)

        self.topLayout.addWidget(self.backButton, alignment=Qt.AlignmentFlag.AlignLeft)
        self.topLayout.addStretch()

        self.layout.addWidget(self.topBar)

        self.labelP = QLabel("Введите коэффициенты системы из 3 уравнений с 3 неизвестными")
        self.labelP.setStyleSheet('color: white; font-size: 16px; font-family: Verdana')
        self.layout.addWidget(self.labelP)

        self.h_layout = QHBoxLayout()

        self.left_widget = QWidget()
        self.left_layout = QVBoxLayout()
        self.left_widget.setLayout(self.left_layout)

        self.buttonLoad = QPushButton("Загрузить из файла")
        self.buttonLoad.setFixedSize(180, 28)
        self.buttonLoad.setStyleSheet(
            'color: white; font-size: 14px; font-family: Verdana; background-color: MidnightBlue'
        )
        self.buttonLoad.clicked.connect(self.load_from_file)
        self.left_layout.addWidget(self.buttonLoad)

        self.buttonCalculate = QPushButton("Вычислить")
        self.buttonCalculate.setFixedSize(180, 28)
        self.buttonCalculate.setStyleSheet(
            'color: white; font-size: 14px; font-family: Verdana; background-color: MidnightBlue'
        )
        self.buttonCalculate.clicked.connect(self.calculate_solution)
        self.left_layout.addWidget(self.buttonCalculate)

        self.left_layout.addStretch()

        self.h_layout.addWidget(self.left_widget)

        self.grid = QGridLayout()
        self.arrayCoeffec = []

        for i in range(3):
            row_widgets = []
            for j in range(3):
                input_widget = QLineEdit()
                input_widget.setStyleSheet('color: white; font-size: 16px; font-family: Verdana')
                self.grid.addWidget(input_widget, i, j)
                row_widgets.append(input_widget)

            free_widget = QLineEdit()
            free_widget.setStyleSheet('color: white; font-size: 16px; font-family: Verdana; background-color: MidnightBlue')
            self.grid.addWidget(free_widget, i, 3)
            row_widgets.append(free_widget)
            self.arrayCoeffec.append(row_widgets)

        self.layout.addLayout(self.grid)

        self.lablelResult = QLabel()
        self.lablelResult.setStyleSheet('color: white; font-size: 16px; font-family: Verdana; margin-top: 10px;')
        self.layout.addWidget(self.lablelResult, alignment=Qt.AlignmentFlag.AlignCenter)

    def load_from_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Выберите файл", "", "Текстовые файлы (*.txt);;Все файлы (*)")
        if filename:
            try:
                with open(filename, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                if len(lines) != 3:
                    QMessageBox.warning(self, "Ошибка", "Файл должен содержать 3 строки.")
                    return
                for i in range(3):
                    parts = lines[i].strip().split()
                    if len(parts) != 4:
                        QMessageBox.warning(self, "Ошибка", f"Строка {i+1} должна содержать 4 числа.")
                        return
                    for j in range(3):
                        self.arrayCoeffec[i][j].setText(parts[j])
                    self.arrayCoeffec[i][3].setText(parts[3])
            except Exception as e:
                QMessageBox.warning(self, "Ошибка", f"Не удалось загрузить файл: {e}")

    def calculate_solution(self):
        A = []
        B = []
        try:
            for row in self.arrayCoeffec:
                a_row = [float(row[j].text()) for j in range(3)]
                B.append(float(row[3].text()))
                A.append(a_row)
        except:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, заполните все поля числовыми значениями")
            return

        def matrix_det(m):
            a11, a12, a13 = m[0]
            a21, a22, a23 = m[1]
            a31, a32, a33 = m[2]
            return (a11 * a22 * a33 + a12 * a23 * a31 + a13 * a21 * a32
                    - a13 * a22 * a31 - a11 * a23 * a32 - a12 * a21 * a33)

        detA = matrix_det(A)
        if abs(detA) < 1e-9:
            QMessageBox.warning(self, "Ошибка", "Определитель равен нулю или очень близок к нему, система не имеет уникального решения")
            return

        def replace_column(matrix, index, column):
            m = [row[:] for row in matrix]
            for i in range(3):
                m[i][index] = column[i]
            return m

        solutions = []
        for i in range(3):
            Ai = replace_column(A, i, B)
            detAi = matrix_det(Ai)
            solutions.append(round(detAi / detA))
        self.lablelResult.setText(f"x1 = {solutions[0]}\n x2 = {solutions[1]}\n x3 = {solutions[2]}")

    def open_kramer_window(self):
        from window_kramer import Window_kramer
        self.MainWindow = Window_kramer()
        self.MainWindow.show()
        self.close()
