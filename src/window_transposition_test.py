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

class Window_transposition_test(QWidget):
    def __init__(self, username):
        super().__init__()
        self.username = username
        self.questions = self.load_questions()
        self.selectedAnswers = [None] * len(self.questions)
        self.initUI()

    def load_questions(self):
        questions = [{
            'question_text': 'Вопрос: Что такое n в матрицах?',
            'question_image': None,  
            'answers': [
                {'text': 'Буква', 'image': None},
                {'text': 'Случайное число', 'image': None},
                {'text': 'Количество столбцов', 'image': None}
            ],
            'correct': 'Количество столбцов'
        }, {
            'question_text': 'Вопрос: Что такое m в матрицах?',
            'question_image': None,  
            'answers': [
                {'text': '13 буква в алфавите', 'image': None},
                {'text': 'Количество строк', 'image': None},
                {'text': 'Что-то', 'image': None}
            ],
            'correct': 'Количество строк'
        }, {
            'question_text': 'Вопрос: Что такое траспонирвоание матриц?',
            'question_image': None,  
            'answers': [
                {'text': 'Перестановка строк и столбцов', 'image': None},
                {'text': 'Фонетический разбор', 'image': None},
                {'text': 'Раскрытие скобок', 'image': None}
            ],
            'correct': 'Перестановка строк и столбцов'
        }, {
            'question_text': 'Вопрос: Какой буквой обозначается транспонирование матриц?',
            'question_image': None,  
            'answers': [
                {'text': 'Латинскими', 'image': None},
                {'text': 'T', 'image': None},
                {'text': 'A', 'image': None}
            ],
            'correct': 'T'
        }, {
            'question_text': 'Вопрос: Сколько будет строк в матрице после транспонирования?',
            'question_image': './data/WindowTranspTest_photoes_Matric.png',  
            'answers': [
                {'text': '2', 'image': None},
                {'text': '5', 'image': None},
                {'text': '4', 'image': None}
            ],
            'correct': '2'
        }, {
            'question_text': 'Вопрос: Сколько будет строк в матрице после транспонирования?',
            'question_image': './data/WindowTranspTest_photoes_Matric2.png',  
            'answers': [
                {'text': '8', 'image': None},
                {'text': '5', 'image': None},
                {'text': '3', 'image': None}
            ],
            'correct': '5'
        }, {
            'question_text': 'Вопрос: Сколько будет столбцов в матрице после транспонирования??',
            'question_image': './data/WindowTranspTest_photoes_Matric3.png',  
            'answers': [
                {'text': '3', 'image': None},
                {'text': '4', 'image': None},
                {'text': '8', 'image': None}
            ],
            'correct': '3'
        }, {
            'question_text': 'Вопрос: Если в матрице 4 строки и 5 столбцов. Какое число отвечает за m?',
            'question_image': None,  
            'answers': [
                {'text': '4', 'image': None},
                {'text': '5', 'image': None},
                {'text': '3', 'image': None}
            ],
            'correct': '4'
        }, {
            'question_text': 'Вопрос: Если в матрице 6 строки и 25 столбцов. Какое число отвечает за m?',
            'question_image': None,  
            'answers': [
                {'text': '2', 'image': None},
                {'text': '6', 'image': None},
                {'text': '25', 'image': None}
            ],
            'correct': '25'
        }, {
            'question_text': 'Вопрос: Если в матрице 12 строки и 2 столбцов. Какое число отвечает за n?',
            'question_image': None,  
            'answers': [
                {'text': '12', 'image': None},
                {'text': '1', 'image': None},
                {'text': '2', 'image': None}
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

