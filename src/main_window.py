from PyQt6.QtWidgets import QWidget, QLabel, QPushButton
from window_matrices import Window_matrices
from window_transposition import Window_transposition
from window_operations import Window_operations
from window_kramer import Window_kramer

class Main_window(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet('background-color: #464168')
        self.setGeometry(300, 50, 800, 650)
        self.setWindowTitle('Главное окно')
        self.initUI()
        self.show()

    def initUI(self):
        self.h1LabelMW = QLabel('Добро пожаловать на курс линейной алгебре', self)
        self.h1LabelMW.move(175, 20)
        self.h1LabelMW.setStyleSheet('color: white; font-size: 20px; font-family: Verdana')

        self.h2LabelMW = QLabel('по теме "Матрицы"', self)
        self.h2LabelMW.move(300, 50)
        self.h2LabelMW.setStyleSheet('color: white; font-size: 18px; font-family: Verdana')

        self.imageLabel = QLabel(self)
        self.imageLabel.move(190, 100)
        self.imageLabel.setStyleSheet('border: 2px solid black')
        from PyQt6.QtGui import QPixmap
        self.imagePixmap = QPixmap('./data/MainWindow_photoes_Matric.jpg')
        self.imageLabel.setPixmap(self.imagePixmap)

        self.pLabelDescPrt1= QLabel('Мы предлагаем вам изучить темы предложенные ниже,', self)
        self.pLabelDescPrt1.move(150, 300)
        self.pLabelDescPrt1.setStyleSheet('color: white; font-size: 16px; font-family: Verdana')

        self.pLabelDescPrt2 = QLabel('а по окончанию изучения пройти тест нато как хорошо вы усвоили материал', self)
        self.pLabelDescPrt2.move(20, 320)
        self.pLabelDescPrt2.setStyleSheet('color: white; font-size: 16px; font-family: Verdana')

        self.pLabelUl = QLabel('Перечень тем для изучения:', self)
        self.pLabelUl.move(20, 370)
        self.pLabelUl.setStyleSheet('color: white; font-size: 16px; font-family: Verdana')

        # Тема 1
        self.pLabelLi1 = QLabel('Матрицы - это...', self)
        self.pLabelLi1.move(60, 400)
        self.pLabelLi1.setFixedSize(300, 90)
        self.pLabelLi1.setStyleSheet('color: white; font-size: 16px; font-family: Verdana; background-color: MediumSlateBlue; padding-left: 5px; border: 5px solid MidnightBlue')
        self.buttonNewWind1 = QPushButton('Перейти', self)
        self.buttonNewWind1.move(270, 430)
        self.buttonNewWind1.setFixedSize(80, 40)
        self.buttonNewWind1.setStyleSheet('color: white; font-size: 14px; font-family: Verdana; background-color: MidnightBlue')
        self.buttonNewWind1.clicked.connect(self.open_window_matrices)

        # Тема 2
        self.pLabelLi2 = QLabel('Транспонирование', self)
        self.pLabelLi2.move(400, 400)
        self.pLabelLi2.setFixedSize(300, 90)
        self.pLabelLi2.setStyleSheet('color: white; font-size: 16px; font-family: Verdana; background-color: MediumSlateBlue; padding-left: 5px; border: 5px solid MidnightBlue')
        self.buttonNewWind2 = QPushButton('Перейти', self)
        self.buttonNewWind2.move(610, 430)
        self.buttonNewWind2.setFixedSize(80, 40)
        self.buttonNewWind2.setStyleSheet('color: white; font-size: 14px; font-family: Verdana; background-color: MidnightBlue')
        self.buttonNewWind2.clicked.connect(self.open_window_transposition)

        # Тема 3
        self.pLabelLi3 = QLabel('Операции матриц', self)
        self.pLabelLi3.move(60, 500)
        self.pLabelLi3.setFixedSize(300, 90)
        self.pLabelLi3.setStyleSheet('color: white; font-size: 16px; font-family: Verdana; background-color: MediumSlateBlue; padding-left: 5px; border: 5px solid MidnightBlue')
        self.buttonNewWind3 = QPushButton('Перейти', self)
        self.buttonNewWind3.move(270, 530)
        self.buttonNewWind3.setFixedSize(80, 40)
        self.buttonNewWind3.setStyleSheet('color: white; font-size: 14px; font-family: Verdana; background-color: MidnightBlue')
        self.buttonNewWind3.clicked.connect(self.open_window_operations)

        # Тема 4
        self.pLabelLi4 = QLabel('Метод Крамера', self)
        self.pLabelLi4.move(400, 500)
        self.pLabelLi4.setFixedSize(300, 90)
        self.pLabelLi4.setStyleSheet('color: white; font-size: 16px; font-family: Verdana; background-color: MediumSlateBlue; padding-left: 5px; border: 5px solid MidnightBlue')
        self.buttonNewWind4 = QPushButton('Перейти', self)
        self.buttonNewWind4.move(610, 530)
        self.buttonNewWind4.setFixedSize(80, 40)
        self.buttonNewWind4.setStyleSheet('color: white; font-size: 14px; font-family: Verdana; background-color: MidnightBlue')
        self.buttonNewWind4.clicked.connect(self.open_window_kramer)

    def open_window_matrices(self):
        self.windowMatric = Window_matrices()
        self.windowMatric.show()
        self.close()

    def open_window_transposition(self):
        self.winTransp = Window_transposition()
        self.winTransp.show()
        self.close()

    def open_window_operations(self):
        self.winOper = Window_operations()
        self.winOper.show()
        self.close()

    def open_window_kramer(self):
        self.winKramer = Window_kramer()
        self.winKramer.show()
        self.close()