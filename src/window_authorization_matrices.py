from PyQt6.QtWidgets import  QWidget, QLabel, QVBoxLayout,QPushButton, QLineEdit, QMessageBox


class Window_authorization_matrices(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet('background-color: #464168')
        self.setWindowTitle('Введите имя')
        self.setMinimumSize(300, 100)
        layout = QVBoxLayout(self)

        self.label = QLabel('Пожалуйста, введите ваше имя:')
        self.label.setStyleSheet('color: white; font-size: 16px; font-family: Verdana')
        layout.addWidget(self.label)

        self.input = QLineEdit()
        layout.addWidget(self.input)

        self.startButton = QPushButton('Начать тест')
        self.startButton.setStyleSheet('color: white; font-size: 14px; font-family: Verdana; background-color: MidnightBlue')
        self.startButton.clicked.connect(self.start_test)
        layout.addWidget(self.startButton)

    def start_test(self):
        from window_matrices_test import Window_matrices_test
        name = self.input.text().strip()
        if not name:
            QMessageBox.warning(self, 'Ошибка', 'Пожалуйста, введите имя')
            return
        self.close()
        self.testWindow = Window_matrices_test(name)
        self.testWindow.show()
