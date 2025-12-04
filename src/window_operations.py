import sys 
import shutil
import os
from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QMessageBox
from PyQt6.QtGui import QPixmap



class Window_operations(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet('background-color: #464168')
        self.setGeometry(100, 40, 1200, 750)
        self.setWindowTitle('Операции с матрицами')
        self.initUI()
        self.show()

    def initUI(self):
        self.buttonNewWind4 = QPushButton('Назад', self)
        self.buttonNewWind4.move(10, 10)
        self.buttonNewWind4.setFixedSize(80, 40)
        self.buttonNewWind4.setStyleSheet('color: white; font-size: 14px; font-family: Verdana; background-color: MidnightBlue')
        self.buttonNewWind4.clicked.connect(self.open_main_window)

        self.buttonDownload = QPushButton('Скачать теорию', self)
        self.buttonDownload.move(1040, 10)
        self.buttonDownload.setFixedSize(150, 40)
        self.buttonDownload.setStyleSheet('color: white; font-size: 14px; font-family: Verdana; background-color: MidnightBlue')
        self.buttonDownload.clicked.connect(self.download)

        self.h1LabelWO = QLabel('Операции с матрицами', self)
        self.h1LabelWO.move(450, 10)
        self.h1LabelWO.setStyleSheet('color: white; font-size: 24px; font-family: Verdana')

        self.pLabelWO1 = QLabel('С матрицами можно выполнять такие операции, как сложение, вычитание и умножение на число.', self)
        self.pLabelWO1.move(60, 60)
        self.pLabelWO1.setStyleSheet('color: white; font-size: 20px; font-family: Verdana')

        self.pLabelWO2 = QLabel('Все матрицы можно складывать или вычитать при условии, что они имеют одинаковый размер.', self)
        self.pLabelWO2.move(60, 120)
        self.pLabelWO2.setStyleSheet('color: white; font-size: 20px; font-family: Verdana')

        self.pLabelWO2 = QLabel('Для выполнения операций сложения или вычитания необходимо сложить или вычесть соответствующие', self)
        self.pLabelWO2.move(60, 165)
        self.pLabelWO2.setStyleSheet('color: white; font-size: 20px; font-family: Verdana')

        self.pLabelWO3 = QLabel('элементы обеих матриц, то есть элементы, расположенные в одинаковых позициях.', self)
        self.pLabelWO3.move(60, 190)
        self.pLabelWO3.setStyleSheet('color: white; font-size: 20px; font-family: Verdana')

        self.imageWOMatric = './data/WindowOperations_photoes_OperationSumVich.png'
        self.imageLabel = QLabel(self)
        self.imageLabel.move(410, 230)
        self.imageLabel.setStyleSheet('border: 2px solid black')

        self.imagePixmap = QPixmap(self.imageWOMatric)
        self.imageLabel.setPixmap(self.imagePixmap)

        self.pLabelWO4 = QLabel('Чтобы умножить матрицу на число, нужно умножить на это число каждый её элемент.', self)
        self.pLabelWO4.move(60, 475)
        self.pLabelWO4.setStyleSheet('color: white; font-size: 20px; font-family: Verdana')

        self.imageWOMultiplication = './data/WindowOperations_photoes_OperationUmnNaNum.png'
        self.imageLabel2 = QLabel(self)
        self.imageLabel2.move(480, 520)
        self.imageLabel2.setStyleSheet('border: 2px solid black')

        self.imagePixmap = QPixmap(self.imageWOMultiplication)
        self.imageLabel2.setPixmap(self.imagePixmap)

        self.buttonTestW3 = QPushButton('Перейти к тесту', self)
        self.buttonTestW3.move(10, 700)
        self.buttonTestW3.setFixedSize(150, 40)
        self.buttonTestW3.setStyleSheet('color: white; font-size: 14px; font-family: Verdana; background-color: MidnightBlue')
        self.buttonTestW3.clicked.connect(self.open_test_operations)

        self.buttonCalculW3 = QPushButton('Перейти к калькулятору', self)
        self.buttonCalculW3.move(200, 700)
        self.buttonCalculW3.setFixedSize(200, 40)
        self.buttonCalculW3.setStyleSheet('color: white; font-size: 14px; font-family: Verdana; background-color: MidnightBlue')
        self.buttonCalculW3.clicked.connect(self.open_calculator_operations)

    def open_main_window(self):
        from main_window import Main_window
        self.main_window = Main_window()
        self.main_window.show()
        self.close()

    def open_calculator_operations(self):
        from window_operations_calculator import Window_operations_calculator
        self.main_window = Window_operations_calculator()
        self.main_window.show()
        self.close()

    def download(self):
        directoruaScr = os.path.dirname(os.path.abspath(__file__))
        directoruaPar = os.path.dirname(directoruaScr)
        file = os.path.join(directoruaPar, 'data/ФайлТеории_Операции.txt')
        saveFile = "Теория_операций_с_матрицами.txt"

        try:
            if not os.path.exists(file):
                QMessageBox.critical(self, "Ошибка", f"Файл не найден.")
                return
            shutil.copy(file, saveFile)
            QMessageBox.information(self, "Получилось", f"Файл скачан в папку")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось скачать файл")

    def open_test_operations(self):
        from window_authorization_operations import Window_authorization_operations
        self.MainWindow = Window_authorization_operations()
        self.MainWindow.show()
        self.close()