import sys 
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QRadioButton, QButtonGroup, QScrollArea, QVBoxLayout
from PyQt6.QtGui import QPixmap


class Window_matrices(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet('background-color: #464168')
        self.setGeometry(100, 40, 1200, 850)
        self.setWindowTitle('Матрицы')
        self.initUI()
        self.show()

    def initUI(self):
        self.buttonNewWind4 = QPushButton('Назад', self)
        self.buttonNewWind4.move(10, 10)
        self.buttonNewWind4.setFixedSize(80, 40)
        self.buttonNewWind4.setStyleSheet('color: white; font-size: 14px; font-family: Verdana; background-color: MidnightBlue')
        self.buttonNewWind4.clicked.connect(self.open_main_window)

        self.h1LabelWM = QLabel('Что такое матрици?', self)
        self.h1LabelWM.move(450, 10)
        self.h1LabelWM.setStyleSheet('color: white; font-size: 24px; font-family: Verdana')

        self.pLabelWM1 = QLabel('Матрица представляет собой таблицу, состоящую из чисел, организованных в прямоугольном формате', self)
        self.pLabelWM1.move(60, 60)
        self.pLabelWM1.setStyleSheet('color: white; font-size: 20px; font-family: Verdana')

        self.pLabelWM2 = QLabel(' Матрицы обозначаются заглавными латинскими буквами', self)
        self.pLabelWM2.move(53, 85)
        self.pLabelWM2.setStyleSheet('color: white; font-size: 20px; font-family: Verdana')

        self.imageWMMatric = './data/WindowMatrices_photoes_Matric.png'
        self.imageLabel = QLabel(self)
        self.imageLabel.move(370, 130)
        self.imageLabel.setStyleSheet('border: 2px solid black')

        self.imagePixmap = QPixmap(self.imageWMMatric)
        self.imageLabel.setPixmap(self.imagePixmap)

        self.pLabelWM2 = QLabel('Если матрица имеет одинаковое количество строк и столбцов, она называется квадратной', self)
        self.pLabelWM2.move(60, 390)
        self.pLabelWM2.setStyleSheet('color: white; font-size: 20px; font-family: Verdana')

        self.pLabelWM3 = QLabel('Векторами называют матрицы, которые содержат только одну строку или один столбец', self)
        self.pLabelWM3.move(60, 415)
        self.pLabelWM3.setStyleSheet('color: white; font-size: 20px; font-family: Verdana')

        self.imageWMMatric1 = './data/WindowMatrices_photoes_MatricKvadrat.png'
        self.imageLabe2 = QLabel(self)
        self.imageLabe2.move(270, 450)
        self.imageLabe2.setStyleSheet('border: 2px solid black')

        self.imagePixmap = QPixmap(self.imageWMMatric1)
        self.imageLabe2.setPixmap(self.imagePixmap)

        self.imageWMMatric2 = './data/WindowMatrices_photoes_MatricVector.png'
        self.imageLabe3 = QLabel(self)
        self.imageLabe3.move(750, 450)
        self.imageLabe3.setStyleSheet('border: 2px solid black')

        self.imagePixmap = QPixmap(self.imageWMMatric2)
        self.imageLabe3.setPixmap(self.imagePixmap)

        self.pLabelWM4 = QLabel('Квадратная матрица', self)
        self.pLabelWM4.move(350, 660)
        self.pLabelWM4.setStyleSheet('color: white; font-size: 20px; font-family: Verdana')

        self.pLabelWM5 = QLabel('Вектор матрицы', self)
        self.pLabelWM5.move(760, 660)
        self.pLabelWM5.setStyleSheet('color: white; font-size: 20px; font-family: Verdana')

        self.pLabelWM6 = QLabel('Главное преимущество матриц заключается в их высокой скорости обработки и масштабируемости', self)
        self.pLabelWM6.move(60, 710)
        self.pLabelWM6.setStyleSheet('color: white; font-size: 20px; font-family: Verdana')

        self.pLabelWM7 = QLabel('Современные компьютеры способны выполнять миллиарды операций с матрицами за секунду', self)
        self.pLabelWM7.move(60, 740)
        self.pLabelWM7.setStyleSheet('color: white; font-size: 20px; font-family: Verdana')

        self.buttonNewWind4 = QPushButton('Перейти к тесту', self)
        self.buttonNewWind4.move(10, 780)
        self.buttonNewWind4.setFixedSize(150, 40)
        self.buttonNewWind4.setStyleSheet('color: white; font-size: 14px; font-family: Verdana; background-color: MidnightBlue')
        self.buttonNewWind4.clicked.connect(self.open_test_matrices)

    def open_main_window(self):
        from main_window import Main_window
        self.MainWindow = Main_window()
        self.MainWindow.show()
        self.close()

    def open_test_matrices(self):
        from window_authorization_matrices import Window_authorization_matrices
        self.MainWindow = Window_authorization_matrices()
        self.MainWindow.show()
        self.close()