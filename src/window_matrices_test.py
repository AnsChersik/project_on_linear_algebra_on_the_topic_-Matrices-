import sys
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

class Window_matrices_test(QWidget):
    def __init__(self, username):
        super().__init__()
        self.username = username
        self.questions = self.load_questions()
        self.selectedAnswers = [None] * len(self.questions)
        self.initUI()

    def load_questions(self):
        questions = [{
            'question_text': 'Вопрос: Матрица - это?...',
            'question_image': './data/WindowMatricesTest_photoes_Matric.png',  
            'answers': [
                {'text': 'Таблица', 'image': None},
                {'text': 'Фильм', 'image': None},
                {'text': 'Слово', 'image': None}
            ],
            'correct': 'Таблица'
        }, {
            'question_text': 'Вопрос: Из чего состоит матрица?',
            'question_image': None,  
            'answers': [
                {'text': 'Из букв', 'image': None},
                {'text': 'Из звуков', 'image': None},
                {'text': 'Из чисел', 'image': None}
            ],
            'correct': 'Из чисел'
        }, {
            'question_text': 'Вопрос: Что это?',
            'question_image': './data/WindowMatricesTest_photoes_Matric2.png',  
            'answers': [
                {'text': 'Фотография', 'image': None},
                {'text': 'Матрица', 'image': None},
                {'text': 'Прямоугольник', 'image': None}
            ],
            'correct': 'Матрица'
        }, {
            'question_text': 'Вопрос: Какими буквами называют матрицы?',
            'question_image': None,  
            'answers': [
                {'text': 'Латинскими', 'image': None},
                {'text': 'Заглавными', 'image': None},
                {'text': 'Латинскими заглавными', 'image': None}
            ],
            'correct': 'Латинскими заглавными'
        }, {
            'question_text': 'Вопрос: Как можно назвать матрицу?',
            'question_image': None,  
            'answers': [
                {'text': 'a', 'image': None},
                {'text': 'A', 'image': None},
                {'text': 'A0A0A0A0A)', 'image': None}
            ],
            'correct': 'A'
        }, {
            'question_text': 'Вопрос: Как называется матрица с равными количествами строк и столбцов?',
            'question_image': './data/WindowMatricesTest_photoes_MatricKvadrat.png',  
            'answers': [
                {'text': 'Квадратная', 'image': None},
                {'text': 'Равносторонняя', 'image': None},
                {'text': 'Кубическая', 'image': None}
            ],
            'correct': 'Квадратная'
        }, {
            'question_text': 'Вопрос: Как называеют матрицу с одной строкой?',
            'question_image': None,  
            'answers': [
                {'text': 'Лучами', 'image': None},
                {'text': 'Векторами', 'image': None},
                {'text': 'Прямой', 'image': None}
            ],
            'correct': 'Векторами'
        }, {
            'question_text': 'Вопрос: Как называеют матрицу с одним столбцом?',
            'question_image': None,  
            'answers': [
                {'text': 'Прямой', 'image': None},
                {'text': 'Лучами', 'image': None},
                {'text': 'Векторами', 'image': None}
            ],
            'correct': 'Векторами'
        }, {
            'question_text': 'Вопрос: Что не являеться преимуществом матриц?',
            'question_image': None,  
            'answers': [
                {'text': 'Высокая скорость обработки', 'image': None},
                {'text': 'Форма', 'image': None},
                {'text': 'Масштабируемость', 'image': None}
            ],
            'correct': 'Форма'
        }, {
            'question_text': 'Вопрос: Кто способен быстро обрабатывать и работать с матрицами?',
            'question_image': None,  
            'answers': [
                {'text': 'Компьютер', 'image': None},
                {'text': 'Гений', 'image': None},
                {'text': 'Миллиардер', 'image': None}
            ],
            'correct': 'Компьютер'
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
            ( self.username, 1, score, total, date_str)
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

# class window_authorization(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('Введите имя')
#         self.setMinimumSize(300, 100)
#         layout = QVBoxLayout(self)

#         self.label = QLabel('Пожалуйста, введите ваше имя:')
#         layout.addWidget(self.label)

#         self.input = QLineEdit()
#         layout.addWidget(self.input)

#         self.startButton = QPushButton('Начать тест')
#         self.startButton.clicked.connect(self.start_test)
#         layout.addWidget(self.startButton)

#     def start_test(self):
#         name = self.input.text().strip()
#         if not name:
#             QMessageBox.warning(self, 'Ошибка', 'Пожалуйста, введите имя')
#             return
#         self.close()
#         self.testWindow = Test_window(name)
#         self.testWindow.show()

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = window_authorization()
#     window.show()
#     sys.exit(app.exec())


