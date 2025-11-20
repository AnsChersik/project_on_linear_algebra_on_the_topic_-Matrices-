import sys 
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt6.QtGui import QPixmap


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet('background-color: #464168')
        self.setGeometry(300, 50, 800, 650)
        self.setWindowTitle('Главное окно')
        self.initUI()
        self.show()

    def initUI(self):
        self.h1LabelMW = QLabel('Добропаожаловать на курс линейной алгебре', self)
        self.h1LabelMW.move(175, 20)
        self.h1LabelMW.setStyleSheet('color: white; font-size: 20px; font-family: Verdana')

        
        self.h2LabelMW = QLabel('по теме "Матрицы"', self)
        self.h2LabelMW.move(300, 50)
        self.h2LabelMW.setStyleSheet('color: white; font-size: 18px; font-family: Verdana')

        self.imageCours = './photoes/MainWindow_photoes_Matric.jpg'
        self.imageLabel = QLabel(self)
        self.imageLabel.move(190, 100)
        self.imageLabel.setStyleSheet('border: 2px solid black')

        self.imagePixmap = QPixmap(self.imageCours)
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


        self.pLabelLi1 = QLabel('Матрицы - это...', self)
        self.pLabelLi1.move(60, 400)
        self.pLabelLi1.setFixedSize(300, 90)
        self.pLabelLi1.setStyleSheet('color: white; font-size: 16px; font-family: Verdana; background-color: MediumSlateBlue; padding-left: 5px; border: 5px solid MidnightBlue')
        self.buttonNewWind1 = QPushButton('Перейти', self)
        self.buttonNewWind1.move(270, 430)
        self.buttonNewWind1.setFixedSize(80, 40)
        self.buttonNewWind1.setStyleSheet('color: white; font-size: 14px; font-family: Verdana; background-color: MidnightBlue')
        self.buttonNewWind1.clicked.connect(self.OpenWinMatric)
           
        self.pLabelLi2 = QLabel('Транспонирование', self)
        self.pLabelLi2.move(400, 400)
        self.pLabelLi2.setFixedSize(300, 90)
        self.pLabelLi2.setStyleSheet('color: white; font-size: 16px; font-family: Verdana; background-color: MediumSlateBlue; padding-left: 5px; border: 5px solid MidnightBlue')
        self.buttonNewWind2 = QPushButton('Перейти', self)
        self.buttonNewWind2.move(610, 430)
        self.buttonNewWind2.setFixedSize(80, 40)
        self.buttonNewWind2.setStyleSheet('color: white; font-size: 14px; font-family: Verdana; background-color: MidnightBlue')
        self.buttonNewWind2.clicked.connect(self.OpenWinTransp)
           
        self.pLabelLi3 = QLabel('Операции матриц', self)
        self.pLabelLi3.move(60, 500)
        self.pLabelLi3.setFixedSize(300, 90)
        self.pLabelLi3.setStyleSheet('color: white; font-size: 16px; font-family: Verdana; background-color: MediumSlateBlue; padding-left: 5px; border: 5px solid MidnightBlue')
        self.buttonNewWind3 = QPushButton('Перейти', self)
        self.buttonNewWind3.move(270, 530)
        self.buttonNewWind3.setFixedSize(80, 40)
        self.buttonNewWind3.setStyleSheet('color: white; font-size: 14px; font-family: Verdana; background-color: MidnightBlue')
        self.buttonNewWind3.clicked.connect(self.OpenWinOper)
           
        self.pLabelLi4 = QLabel('Метод Крамера', self)
        self.pLabelLi4.move(400, 500)
        self.pLabelLi4.setFixedSize(300, 90)
        self.pLabelLi4.setStyleSheet('color: white; font-size: 16px; font-family: Verdana; background-color: MediumSlateBlue; padding-left: 5px; border: 5px solid MidnightBlue')
        self.buttonNewWind4 = QPushButton('Перейти', self)
        self.buttonNewWind4.move(610, 530)
        self.buttonNewWind4.setFixedSize(80, 40)
        self.buttonNewWind4.setStyleSheet('color: white; font-size: 14px; font-family: Verdana; background-color: MidnightBlue')
        self.buttonNewWind4.clicked.connect(self.OpenWinKramer)
           
    def OpenWinMatric(self):
        self.windowMatric = WindowMatrices()
        self.windowMatric.show()
        self.close()


    def OpenWinTransp(self):
        self.winTransp = WindowTransposition()
        self.winTransp.show()
        self.close()

    def OpenWinOper(self):
        self.winOper = WindowOperations()
        self.winOper.show()
        self.close()

    def OpenWinKramer(self):
        self.winKramer = WindowKramer()
        self.winKramer.show()
        self.close()


class WindowMatrices(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet('background-color: #464168')
        self.setGeometry(300, 50, 800, 650)
        self.setWindowTitle('Матрицы')
        self.initUI()
        self.show()

    def initUI(self):
        self.buttonNewWind4 = QPushButton('Назад', self)
        self.buttonNewWind4.move(10, 10)
        self.buttonNewWind4.setFixedSize(80, 40)
        self.buttonNewWind4.setStyleSheet('color: white; font-size: 14px; font-family: Verdana; background-color: MidnightBlue')
        self.buttonNewWind4.clicked.connect(self.OpenMainWindow)
           
    def OpenMainWindow(self):
        self.MainWindow = MainWindow()
        self.MainWindow.show()
        self.close()






class WindowTransposition(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet('background-color: #464168')
        self.setGeometry(300, 50, 800, 650)
        self.setWindowTitle('Матрицы')
        self.initUI()
        self.show()

    def initUI(self):
        self.buttonNewWind4 = QPushButton('Назад', self)
        self.buttonNewWind4.move(10, 10)
        self.buttonNewWind4.setFixedSize(80, 40)
        self.buttonNewWind4.setStyleSheet('color: white; font-size: 14px; font-family: Verdana; background-color: MidnightBlue')
        self.buttonNewWind4.clicked.connect(self.OpenMainWindow)
           
    def OpenMainWindow(self):
        self.MainWindow = MainWindow()
        self.MainWindow.show()
        self.close()

class WindowOperations(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet('background-color: #464168')
        self.setGeometry(300, 50, 800, 650)
        self.setWindowTitle('Матрицы')
        self.initUI()
        self.show()

    def initUI(self):
        self.buttonNewWind4 = QPushButton('Назад', self)
        self.buttonNewWind4.move(10, 10)
        self.buttonNewWind4.setFixedSize(80, 40)
        self.buttonNewWind4.setStyleSheet('color: white; font-size: 14px; font-family: Verdana; background-color: MidnightBlue')
        self.buttonNewWind4.clicked.connect(self.OpenMainWindow)
           
    def OpenMainWindow(self):
        self.MainWindow = MainWindow()
        self.MainWindow.show()
        self.close()

class WindowKramer(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet('background-color: #464168')
        self.setGeometry(300, 50, 800, 650)
        self.setWindowTitle('Матрицы')
        self.initUI()
        self.show()

    def initUI(self):
        self.buttonNewWind4 = QPushButton('Назад', self)
        self.buttonNewWind4.move(10, 10)
        self.buttonNewWind4.setFixedSize(80, 40)
        self.buttonNewWind4.setStyleSheet('color: white; font-size: 14px; font-family: Verdana; background-color: MidnightBlue')
        self.buttonNewWind4.clicked.connect(self.OpenMainWindow)
           
    def OpenMainWindow(self):
        self.MainWindow = MainWindow()
        self.MainWindow.show()
        self.close()
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())