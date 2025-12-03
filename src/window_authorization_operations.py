from PyQt6.QtWidgets import  QWidget, QLabel, QVBoxLayout,QPushButton, QLineEdit, QMessageBox


class Window_authorization_operations(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Введите имя')
        self.setMinimumSize(300, 100)
        layout = QVBoxLayout(self)

        self.label = QLabel('Пожалуйста, введите ваше имя:')
        layout.addWidget(self.label)

        self.input = QLineEdit()
        layout.addWidget(self.input)

        self.startButton = QPushButton('Начать тест')
        self.startButton.clicked.connect(self.start_test)
        layout.addWidget(self.startButton)

    def start_test(self):
        from window_operations_test import Window_operations_test
        name = self.input.text().strip()
        if not name:
            QMessageBox.warning(self, 'Ошибка', 'Пожалуйста, введите имя')
            return
        self.close()
        self.testWindow = Window_operations_test(name)
        self.testWindow.show()
