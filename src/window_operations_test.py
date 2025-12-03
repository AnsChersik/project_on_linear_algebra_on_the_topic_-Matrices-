import sqlite3
from datetime import datetime
from PyQt6.QtWidgets import (
    QWidget, QLabel, QVBoxLayout, QRadioButton, QButtonGroup,
    QPushButton, QScrollArea, QHBoxLayout
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap

conn = sqlite3.connect('CoursLineMath.sql')
cursor = conn.cursor()

class Window_operations_test(QWidget):
    def __init__(self, username):
        super().__init__()
        self.username = username
        self.questions = self.load_questions()
        self.selectedAnswers = [None] * len(self.questions)
        self.initUI()

    def load_questions(self):
        questions = [{
            'question_text': 'Вопрос: Что нельзя выполнять с матрицами?',
            'question_image': None,  
            'answers': [
                {'text': 'Вычитание', 'image': None},
                {'text': 'Слажение', 'image': None},
                {'text': 'Деление', 'image': None}
            ],
            'correct': 'Деление'
        }, {
            'question_text': 'Вопрос: Какое есть условие на сложение и вычитание?',
            'question_image': None,  
            'answers': [
                {'text': 'Они все квадратыне', 'image': None},
                {'text': 'Называются одинаеово', 'image': None},
                {'text': 'Имеют одинаковы размер', 'image': None}
            ],
            'correct': 'Имеют одинаковы размер'
        }, {
            'question_text': 'Вопрос: Какие матрицы можно сложить?',
            'question_image': None,  
            'answers': [
                {'text': '2x2 3x3', 'image': None},
                {'text': '3x3 3x3', 'image': None},
                {'text': '2x3 3x2', 'image': None}
            ],
            'correct': '3x3 3x3'
        }, {
            'question_text': 'Вопрос: Какие матрицы можно вычитать?',
            'question_image': None,  
            'answers': [
                {'text': '2x4 4x2', 'image': None},
                {'text': '6x9 6x9', 'image': None},
                {'text': '2x2 3x2', 'image': None}
            ],
            'correct': '6x9 6x9'
        }, {
            'question_text': 'Вопрос: Сколько будет строк в матрице после транспонирования?',
            'question_image': None,  
            'answers': [
                {'text': '2', 'image': None},
                {'text': '5', 'image': None},
                {'text': '4', 'image': None}
            ],
            'correct': '2'
        }, {
            'question_text': 'Вопрос: Чтобы сложить матрицы в первой строке что будет?',
            'question_image': None,  
            'answers': [
                {'text': 'a11+b11 a21+b21 a31+b31', 'image': None},
                {'text': 'a11+b11 a22+b22 a33+b33', 'image': None},
                {'text': 'a11+b11 a12+b12 a13+b13', 'image': None}
            ],
            'correct': 'a11+b11 a21+b21 a31+b31'
        }, {
            'question_text': 'Вопрос: Чтобы сложить матрицы в третьей строке что будет?',
            'question_image': None,  
            'answers': [
                {'text': 'a11+b31 a21+b31 a31+b31', 'image': None},
                {'text': 'a11+b11 a22+b22 a33+b33', 'image': None},
                {'text': 'a31+b31 a32+b32 a33+b33', 'image': None}
            ],
            'correct': 'a31+b31 a32+b32 a33+b33'
        }, {
            'question_text': 'Вопрос: Что нужно делать чтобы умножить матрицу на число?',
            'question_image': None,  
            'answers': [
                {'text': 'Умножить каждый элемент на число', 'image': None},
                {'text': 'Умножить тольцо диагональ', 'image': None},
                {'text': 'Умножить на количество строк и столбцов число', 'image': None}
            ],
            'correct': 'Умножить каждый элемент на число'
        }, {
            'question_text': 'Вопрос: Какой буквой обозначаеться число на которое усножают?',
            'question_image': None,  
            'answers': [
                {'text': 'K', 'image': None},
                {'text': 'C', 'image': None},
                {'text': 'A', 'image': None}
            ],
            'correct': 'K'
        }, {
            'question_text': 'Вопрос: Где правильный ответ?',
            'question_image': './data/WindowOperationsTest_photoes_OperationUmnNaNum.png',  
            'answers': [
                {'text': '1', 'image': './data/WindowOperationsTest_photoes_OperationNumUncorr.png'},
                {'text': '2', 'image': './data/WindowOperationsTest_photoes_OperationNumCorr.png'},
                {'text': '3', 'image': './data/WindowOperationsTest_photoes_OperationNumUncorr2.png'}
            ],
            'correct': '2'
        }]
        return questions

    def initUI(self):
        self.setMinimumSize(600, 600)
        self.setWindowTitle('Тест')

        self.mainLayoutTest = QVBoxLayout(self)

        self.scrollA = QScrollArea()
        self.scrollA.setWidgetResizable(True)
        self.mainWidget = QWidget()
        self.boxLayout = QVBoxLayout(self.mainWidget)
        self.scrollA.setWidget(self.mainWidget)

        self.buttonBack = QPushButton('Назад', self)
        self.buttonBack.move(10, 10)
        self.buttonBack.setFixedSize(80, 40)
        self.buttonBack.setStyleSheet('color: white; font-size: 14px; font-family: Verdana; background-color: MidnightBlue')
        self.buttonBack.clicked.connect(self.open_main_window)
        self.boxLayout.addWidget(self.buttonBack)

        self.mainLayoutTest.addWidget(self.scrollA)

        self.questionsWid = []

        self.render_questions()

        self.buttonTestFinish = QPushButton('Завершить тест')
        self.buttonTestFinish.clicked.connect(self.render_results)
        self.boxLayout.addWidget(self.buttonTestFinish)



    def render_questions(self):
        for i, q in enumerate(self.questions):
            quesWidget = QWidget()
            quesLayout = QVBoxLayout(quesWidget)

            quesLabel = QLabel(f"{i+1}. {q['question_text']}")
            quesLayout.addWidget(quesLabel)
            if q['question_image']:
                pixmap = QPixmap(q['question_image'])
                imgLabelTest = QLabel()
                imgLabelTest.setPixmap(pixmap.scaledToWidth(500))
                quesLayout.addWidget(imgLabelTest)

            answerGroupButton = QButtonGroup(quesWidget)
            answerGroupButton.setExclusive(True)
            answerWidgets = []

            for answer in q['answers']:
                answerWidget = QWidget()
                answerLayout = QHBoxLayout(answerWidget)

                radioButton = QRadioButton(answer['text'])
                answerGroupButton.addButton(radioButton)
                answerLayout.addWidget(radioButton)

                if answer['image']:
                    pixmapAns = QPixmap(answer['image'])
                    imgAnswerLabel = QLabel()
                    imgAnswerLabel.setPixmap(pixmapAns.scaledToWidth(100))
                    answerLayout.addWidget(imgAnswerLabel)

                quesLayout.addWidget(answerWidget)
                answerWidgets.append((radioButton, answer['text']))

            self.boxLayout.addWidget(quesWidget)
            self.questionsWid.append({
                'question': q,
                'answer_group': answerGroupButton,
                'answer_widgets': answerWidgets
            })

    def render_results(self):
        score = 0
        for i, quesWidget in enumerate(self.questionsWid):
            selectedButton = quesWidget['answer_group'].checkedButton()
            if selectedButton:
                answerQuesText = selectedButton.text()
                self.selectedAnswers[i] = answerQuesText
                if answerQuesText == quesWidget['question']['correct']:
                    score += 1
            else:
                self.selectedAnswers[i] = None

        total = len(self.questions)
        self.clear_layout(self.boxLayout)

        resultLabel = QLabel(f'Вы набрали {score} из {total}')
        resultLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.boxLayout.addWidget(resultLabel)

        for i, q in enumerate(self.questions):
            quesLabel = QLabel(f"Вопрос {i+1}: {q['question_text']}")
            self.boxLayout.addWidget(quesLabel)
            if q['question_image']:
                pixmapQues = QPixmap(q['question_image'])
                imgQuesLabel = QLabel()
                imgQuesLabel.setPixmap(pixmapQues.scaledToWidth(500))
                self.boxLayout.addWidget(imgQuesLabel)

            answerUser = self.selectedAnswers[i]
            answerCorrect = q['correct']

            for answer in q['answers']:
                answerQuesText = answer['text']
                answerLabel = QLabel(answerQuesText)
                if answerQuesText == answerCorrect:
                    answerLabel.setStyleSheet("color: green;")
                if answerQuesText == answerUser and answerQuesText != answerCorrect:
                    answerLabel.setStyleSheet("color: red;")
                self.boxLayout.addWidget(answerLabel)
                if answer['image']:
                    pixmapAns = QPixmap(answer['image'])
                    imgAnswerLabel = QLabel()
                    imgAnswerLabel.setPixmap(pixmapAns.scaledToWidth(100))
                    self.boxLayout.addWidget(imgAnswerLabel)

        date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute(
            'INSERT INTO Results (username, id_topic, score, max, date) VALUES ( ?, ?, ?, ?, ?)',
            ( self.username, 2, score, total, date_str)
        )
        conn.commit()

        restartButtonTest = QPushButton('Пройти тест снова')
        restartButtonTest.clicked.connect(self.restart_test)
        self.boxLayout.addWidget(restartButtonTest)

    def restart_test(self):
        self.clear_layout(self.boxLayout)
        self.selectedAnswers = [None] * len(self.questions)
        self.render_questions()
        self.buttonTestFinish = QPushButton('Завершить тест')
        self.buttonTestFinish.clicked.connect(self.render_results)
        self.boxLayout.addWidget(self.buttonTestFinish)

    def clear_layout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget:
                    widget.deleteLater()

    def open_main_window(self):
        from window_matrices import Window_matrices
        self.MainWindow = Window_matrices()
        self.MainWindow.show()
        self.close()
