import sys 
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QPixmap


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(300, 50, 800, 800)
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

        self.imageCours = './MainWindow_photoes_Matric.jpg'
        self.imageLabel = QLabel(self)
        self.imageLabel.move(190, 100)
        self.imageLabel.setStyleSheet('border: 2px solid black')

        self.imagePixmap = QPixmap(self.imageCours)
        self.imageLabel.setPixmap(self.imagePixmap)



           

















if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())