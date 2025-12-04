import sqlite3
from datetime import datetime
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QTextEdit, QPushButton, QLabel, QLineEdit
)
from PyQt6.QtGui import QTextCharFormat, QTextCursor, QFont
from PyQt6.QtCore import Qt

def init_db():
    conn = sqlite3.connect('CoursLineMath.sql')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Reviews (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nickname TEXT,
            topic TEXT,
            review TEXT,
            date TEXT
        )
    ''')
    conn.commit()
    conn.close()

class Window_review(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet('background-color: #464168')
        self.setWindowTitle("Отзыв пользователя")
        self.resize(600, 500)
        self.init_ui()
        self.currentReviewId = None 

    def init_ui(self):
        self.layout = QVBoxLayout()

        topLayout = QHBoxLayout()
        self.back_button = QPushButton("Назад")
        self.back_button.setStyleSheet('color: white; font-size: 14px; font-family: Verdana; background-color: MidnightBlue')
        self.back_button.clicked.connect(self.open_main_window)  
        topLayout.addWidget(self.back_button, alignment=Qt.AlignmentFlag.AlignLeft)
        topLayout.addStretch() 
        self.layout.addLayout(topLayout)

        self.inputNik = QLineEdit()
        self.inputNik.setPlaceholderText("Введите ник")
        self.inputNik.setStyleSheet('color: white; font-size: 14px; font-family: Verdana')
        self.inputNik.setMaxLength(50)

        self.inputTopic = QLineEdit()
        self.inputTopic.setPlaceholderText("Введите тему отзыва")
        self.inputTopic.setStyleSheet('color: white; font-size: 14px; font-family: Verdana')
        self.inputTopic.setMaxLength(50)

        self.layout.addWidget(self.inputNik)
        self.layout.addWidget(self.inputTopic)

        buttonLayout = QHBoxLayout()

        self.buttonBold = QPushButton("Жирный")
        self.buttonBold.setStyleSheet('color: white; font-size: 14px; font-family: Verdana; background-color: MidnightBlue')
       
        self.buttonItalic = QPushButton("Курсив")
        self.buttonItalic.setStyleSheet('color: white; font-size: 14px; font-family: Verdana; background-color: MidnightBlue')
        
        self.buttonUnderline = QPushButton("Подчеркнутый")
        self.buttonUnderline.setStyleSheet('color: white; font-size: 14px; font-family: Verdana; background-color: MidnightBlue')
        
        self.buttonSend = QPushButton("Отправить")
        self.buttonSend.setStyleSheet('color: white; font-size: 14px; font-family: Verdana; background-color: MidnightBlue')
        
        self.buttonEdit = QPushButton("Редактировать")
        self.buttonEdit.setStyleSheet('color: white; font-size: 14px; font-family: Verdana; background-color: MidnightBlue')
        
        self.buttonEdit.setEnabled(False) 

        buttonLayout.addWidget(self.buttonBold)
        buttonLayout.addWidget(self.buttonItalic)
        buttonLayout.addWidget(self.buttonUnderline)
        buttonLayout.addWidget(self.buttonSend)
        buttonLayout.addWidget(self.buttonEdit)

        self.buttonBold.clicked.connect(self.make_bold)
        self.buttonItalic.clicked.connect(self.make_italic)
        self.buttonUnderline.clicked.connect(self.make_underline)
        self.buttonSend.clicked.connect(self.send_review)
        self.buttonEdit.clicked.connect(self.edit_review)

        self.layout.addLayout(buttonLayout)

        self.textEdit = QTextEdit()
        self.textEdit.setStyleSheet('color: white; font-size: 14px; font-family: Verdana')
        self.textEdit.setPlaceholderText("Введите ваш отзыв")
        self.textEdit.textChanged.connect(self.limit_text_length)

        self.charCountLabel = QLabel("0/200 символов")
        self.charCountLabel.setStyleSheet('color: white; font-size: 14px; font-family: Verdana')
        self.charCountLabel.setAlignment(Qt.AlignmentFlag.AlignRight)

        self.layout.addWidget(self.textEdit)
        self.layout.addWidget(self.charCountLabel)

        self.TYlabel = QLabel("Спасибо за отзыв!")
        self.TYlabel.setStyleSheet('color: white; font-size: 14px; font-family: Verdana')
        self.TYlabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.TYlabel.hide()  

        self.layout.addWidget(self.TYlabel)

        self.setLayout(self.layout)

        self.storedReviewText = ""

    def limit_text_length(self):
        text = self.textEdit.toPlainText()
        if len(text) > 200:
            self.textEdit.blockSignals(True)
            self.textEdit.setPlainText(text[:200])
            self.textEdit.blockSignals(False)
            cursor = self.textEdit.textCursor()
            cursor.movePosition(QTextCursor.MoveOperation.End)
            self.textEdit.setTextCursor(cursor)
        self.charCountLabel.setText(f"{len(self.textEdit.toPlainText())}/200 символов")

    def make_bold(self):
        self.apply_formatting('bold')

    def make_italic(self):
        self.apply_formatting('italic')

    def make_underline(self):
        self.apply_formatting('underline')

    def apply_formatting(self, fmtType):
        cursor = self.textEdit.textCursor()
        if not cursor.hasSelection():
            return
        fmt = QTextCharFormat()
        if fmtType == 'bold':
            currentWeight = cursor.charFormat().fontWeight()
            if currentWeight == QFont.Weight.Bold:
                fmt.setFontWeight(QFont.Weight.Normal)
            else:
                fmt.setFontWeight(QFont.Weight.Bold)
        elif fmtType == 'italic':
            currentItalic = cursor.charFormat().fontItalic()
            fmt.setFontItalic(not currentItalic)
        elif fmtType == 'underline':
            currentUnderline = cursor.charFormat().fontUnderline()
            fmt.setFontUnderline(not currentUnderline)
        cursor.mergeCharFormat(fmt)
        self.textEdit.mergeCurrentCharFormat(fmt)

    def send_review(self):
        nickname = self.inputNik.text().strip()
        topic = self.inputTopic.text().strip()
        review = self.textEdit.toPlainText()

        if not nickname or not topic or not review:
            return

        date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        conn = sqlite3.connect('CoursLineMath.sql')
        cursor = conn.cursor()

        if self.currentReviewId is None:
            cursor.execute('''
                INSERT INTO Reviews (nickname, topic, review, date)
                VALUES (?, ?, ?, ?)
            ''', (nickname, topic, review, date_str))
            self.currentReviewId = cursor.lastrowid
        else:
            cursor.execute('''
                UPDATE Reviews SET nickname=?, topic=?, review=?, date=? WHERE id=?
            ''', (nickname, topic, review, date_str, self.currentReviewId))
        conn.commit()
        conn.close()

        self.input_container_hide_show(hide=True)
        self.TYlabel.show()
        self.buttonEdit.setEnabled(True)

    def input_container_hide_show(self, hide=True):
        if hide:
            self.textEdit.hide()
            self.charCountLabel.hide()
        else:
            self.textEdit.show()
            self.charCountLabel.show()

    def edit_review(self):
        if self.currentReviewId is None:
            return
        conn = sqlite3.connect('CoursLineMath.sql')
        cursor = conn.cursor()
        cursor.execute('SELECT nickname, topic, review FROM Reviews WHERE id=?', (self.currentReviewId,))
        row = cursor.fetchone()
        conn.close()
        if row:
            nickname, topic, review = row
            self.inputNik.setText(nickname)
            self.inputTopic.setText(topic)
            self.textEdit.setPlainText(review)
            self.input_container_hide_show(hide=False)
            self.TYlabel.hide()

    def open_main_window(self):
        from main_window import Main_window
        self.main_window = Main_window()
        self.main_window.show()
        self.close()