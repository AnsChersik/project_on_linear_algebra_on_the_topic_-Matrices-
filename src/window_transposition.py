from PyQt6.QtWidgets import QWidget, QLabel, QPushButton
from PyQt6.QtGui import QPixmap


class Window_transposition(QWidget):
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
        self.buttonWT.clicked.connect(self.open_main_window)
           
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
        self.buttonTestW4.clicked.connect(self.open_test_transposition)

    def open_main_window(self):
        from main_window import Main_window
        self.main_window = Main_window()
        self.main_window.show()
        self.close()

    def open_test_transposition(self):
        from window_matrices_test import Window_matrices_test
        self.test_window = Window_matrices_test()
        self.test_window.show()
        self.close()