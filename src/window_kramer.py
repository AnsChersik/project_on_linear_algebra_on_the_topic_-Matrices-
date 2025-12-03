from PyQt6.QtWidgets import QWidget, QLabel, QPushButton
from PyQt6.QtGui import QPixmap



class Window_kramer(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet('background-color: #464168')
        self.setGeometry(100, 40, 1200, 750)
        self.setWindowTitle('Метод Крамера')
        self.initUI()
        self.show()

    def initUI(self):
        self.buttonNewWind4 = QPushButton('Назад', self)
        self.buttonNewWind4.move(10, 10)
        self.buttonNewWind4.setFixedSize(80, 40)
        self.buttonNewWind4.setStyleSheet('color: white; font-size: 14px; font-family: Verdana; background-color: MidnightBlue')
        self.buttonNewWind4.clicked.connect(self.open_main_window)

        self.h1LabelWO = QLabel('Метод Крамера', self)
        self.h1LabelWO.move(490, 10)
        self.h1LabelWO.setStyleSheet('color: white; font-size: 24px; font-family: Verdana')

        self.pLabelWO1 = QLabel('Для решения системы уравнений методом Крамера сначала нужно найти определитель основной матрицы.', self)
        self.pLabelWO1.move(60, 60)
        self.pLabelWO1.setStyleSheet('color: white; font-size: 20px; font-family: Verdana')

        self.pLabelWO2 = QLabel('Определитель ищется по формуле:', self)
        self.pLabelWO2.move(60, 85)
        self.pLabelWO2.setStyleSheet('color: white; font-size: 20px; font-family: Verdana')

        
        self.imageWOMatric = './data/WindowKramer_photoes_CalculationKramera.png'
        self.imageLabel = QLabel(self)
        self.imageLabel.move(300, 115)
        self.imageLabel.setStyleSheet('border: 2px solid black')

        self.imagePixmap = QPixmap(self.imageWOMatric)
        self.imageLabel.setPixmap(self.imagePixmap)

        self.pLabelWO2 = QLabel('Затем для каждого неизвестного заменяем соответствующий столбец в матрице на столбец свободных', self)
        self.pLabelWO2.move(60, 230)
        self.pLabelWO2.setStyleSheet('color: white; font-size: 20px; font-family: Verdana')

        self.pLabelWO3 = QLabel('членов и вычисляем определитель полученной матрицы.', self)
        self.pLabelWO3.move(60, 255)
        self.pLabelWO3.setStyleSheet('color: white; font-size: 20px; font-family: Verdana')

        self.pLabelWO4 = QLabel('После этого делим каждый из этих определителей на общий определитель — так мы получаем', self)
        self.pLabelWO4.move(60, 290)
        self.pLabelWO4.setStyleSheet('color: white; font-size: 20px; font-family: Verdana')

        self.pLabelWO5 = QLabel('значения переменных.', self)
        self.pLabelWO5.move(60, 315)
        self.pLabelWO5.setStyleSheet('color: white; font-size: 20px; font-family: Verdana')


        self.imageWOMatric = './data/WindowKramer_photoes_TeoremaKramera.png'
        self.imageLabel = QLabel(self)
        self.imageLabel.move(60, 350)
        self.imageLabel.setStyleSheet('border: 2px solid black')

        self.imagePixmap = QPixmap(self.imageWOMatric)
        self.imageLabel.setPixmap(self.imagePixmap)


        self.imageWOMatricc = './data/WindowKramer_photoes_PrimerKramera.png'
        self.imageLabe2 = QLabel(self)
        self.imageLabe2.move(650, 350)
        self.imageLabe2.setStyleSheet('border: 2px solid black')

        self.imagePixmap = QPixmap(self.imageWOMatricc)
        self.imageLabe2.setPixmap(self.imagePixmap)

        self.buttonTestW3 = QPushButton('Перейти к тесту', self)
        self.buttonTestW3.move(10, 700)
        self.buttonTestW3.setFixedSize(150, 40)
        self.buttonTestW3.setStyleSheet('color: white; font-size: 14px; font-family: Verdana; background-color: MidnightBlue')
        self.buttonTestW3.clicked.connect(self.open_test_kramer)

    def open_main_window(self):
        from main_window import Main_window
        self.main_window = Main_window()
        self.main_window.show()
        self.close()

    def open_test_kramer(self):
        from window_authorization_kramer import Window_authorization_kramer
        self.MainWindow = Window_authorization_kramer()
        self.MainWindow.show()
        self.close()