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
        self.h1LabelMW = QLabel('Добро пожаловать на курс линейной алгебре', self)
        self.h1LabelMW.move(175, 20)
        self.h1LabelMW.setStyleSheet('color: white; font-size: 20px; font-family: Verdana')

        self.h2LabelMW = QLabel('по теме "Матрицы"', self)
        self.h2LabelMW.move(300, 50)
        self.h2LabelMW.setStyleSheet('color: white; font-size: 18px; font-family: Verdana')

        self.imageMWMatric = './data/MainWindow_photoes_Matric.jpg'
        self.imageLabel = QLabel(self)
        self.imageLabel.move(190, 100)
        self.imageLabel.setStyleSheet('border: 2px solid black')

        self.imagePixmap = QPixmap(self.imageMWMatric)
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
        self.setGeometry(100, 40, 1200, 850)
        self.setWindowTitle('Матрицы')
        self.initUI()
        self.show()

    def initUI(self):
        self.buttonNewWind4 = QPushButton('Назад', self)
        self.buttonNewWind4.move(10, 10)
        self.buttonNewWind4.setFixedSize(80, 40)
        self.buttonNewWind4.setStyleSheet('color: white; font-size: 14px; font-family: Verdana; background-color: MidnightBlue')
        self.buttonNewWind4.clicked.connect(self.OpenMainWindow)

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
        self.buttonNewWind4.clicked.connect(self.OpenTestMatric)

    def OpenMainWindow(self):
        self.MainWindow = MainWindow()
        self.MainWindow.show()
        self.close()

    def OpenTestMatric(self):
        self.MainWindow = WindowMatricesTest()
        self.MainWindow.show()
        self.close()



class WindowMatricesTest(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet('background-color: #464168')
        self.setGeometry(100, 40, 1200, 720)
        self.setWindowTitle('Тест')
        self.initUI()
        self.show()

    def initUI(self):
        self.buttonNewWind4 = QPushButton('Назад', self)
        self.buttonNewWind4.move(10, 10)
        self.buttonNewWind4.setFixedSize(80, 40)
        self.buttonNewWind4.setStyleSheet('color: white; font-size: 14px; font-family: Verdana; background-color: MidnightBlue')
        self.buttonNewWind4.clicked.connect(self.OpenMainWindow)

    def OpenMainWindow(self):
        self.MainWindow = WindowMatrices()
        self.MainWindow.show()
        self.close()

class WindowTransposition(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet('background-color: #464168')
        self.setGeometry(100, 40, 1200, 750)
        self.setWindowTitle('Транспонирование матриц')
        self.initUI()
        self.show()

    def initUI(self):
        self.buttonWT = QPushButton('Назад', self)
        self.buttonWT.move(10, 10)
        self.buttonWT.setFixedSize(80, 40)
        self.buttonWT.setStyleSheet('color: white; font-size: 14px; font-family: Verdana; background-color: MidnightBlue')
        self.buttonWT.clicked.connect(self.OpenMainWindow)
           
        self.h1LabelWT = QLabel('Транспонирование матриц', self)
        self.h1LabelWT.move(450, 10)
        self.h1LabelWT.setStyleSheet('color: white; font-size: 24px; font-family: Verdana')

        self.pLabelWT1 = QLabel('Матрица состоит из строк и столбцов, где m — количество строк, а n — количество столбцов. ', self)
        self.pLabelWT1.move(70, 60)
        self.pLabelWT1.setStyleSheet('color: white; font-size: 20px; font-family: Verdana')

        self.pLabelWT2 = QLabel('Обозначим i как номер строки (1 ≤ i ≤ m), а j — номер столбца (1 ≤ j ≤ n).', self)
        self.pLabelWT2.move(160, 85)
        self.pLabelWT2.setStyleSheet('color: white; font-size: 20px; font-family: Verdana')

        self.imageWTMatric = './data/WindowTransp_photoes_SizeMatric.png'
        self.imageLabel = QLabel(self)
        self.imageLabel.move(300, 130)
        self.imageLabel.setStyleSheet('border: 2px solid black')

        self.imagePixmap = QPixmap(self.imageWTMatric)
        self.imageLabel.setPixmap(self.imagePixmap)

        self.pLabelWT2 = QLabel('Транспонирование матрицы — это процесс перестановки строк и столбцов матрицы', self)
        self.pLabelWT2.move(60, 400)
        self.pLabelWT2.setStyleSheet('color: white; font-size: 20px; font-family: Verdana')

        self.pLabelWT3 = QLabel('с сохранением их порядка.', self)
        self.pLabelWT3.move(60, 428)
        self.pLabelWT3.setStyleSheet('color: white; font-size: 20px; font-family: Verdana')

        self.pLabelWT4 = QLabel('Обозначение транспонированной матрицы — A', self)
        self.pLabelWT4.move(60, 455)
        self.pLabelWT4.setStyleSheet('color: white; font-size: 20px; font-family: Verdana')

        self.pLabelWT4 = QLabel('T', self)
        self.pLabelWT4.move(554, 447)
        self.pLabelWT4.setStyleSheet('color: white; font-size: 18px; font-family: Verdana')

        self.imageWTTransponirovanie = './data/WindowTransp_photoes_TrancMatric.png'
        self.imageLabe2 = QLabel(self)
        self.imageLabe2.move(260, 500)
        self.imageLabe2.setStyleSheet('border: 2px solid black')

        self.imagePixmap = QPixmap(self.imageWTTransponirovanie)
        self.imageLabe2.setPixmap(self.imagePixmap)

        self.buttonTestW4 = QPushButton('Перейти к тесту', self)
        self.buttonTestW4.move(10, 700)
        self.buttonTestW4.setFixedSize(150, 40)
        self.buttonTestW4.setStyleSheet('color: white; font-size: 14px; font-family: Verdana; background-color: MidnightBlue')
        self.buttonTestW4.clicked.connect(self.OpenTestTransp)

    def OpenMainWindow(self):
        self.MainWindow = MainWindow()
        self.MainWindow.show()
        self.close()

    def OpenTestTransp(self):
        self.MainWindow = WindowMatricesTest()
        self.MainWindow.show()
        self.close()

class WindowOperations(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet('background-color: #464168')
        self.setGeometry(300, 50, 800, 650)
        self.setWindowTitle('Операции с матрицами')
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
        self.setWindowTitle('Метод Крамера')
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