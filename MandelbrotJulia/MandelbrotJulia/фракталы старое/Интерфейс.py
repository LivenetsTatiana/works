
# =============================================================================
#import PyQt5
# =============================================================================
# from PyQt5.QtWidgets import QLabel, QApplication
# app = QApplication([])
# label = QLabel('Hello World!')
# label.show()
# app.exec()
# =============================================================================
# =============================================================================
# from PyQt5.QtCore import Qt
# from PyQt5.QtGui import QPalette
# from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
# app = QApplication([])
# app.setStyleSheet("QPushButton { margin: 10ex; }")
# app.setStyle('Windows')
# palette = QPalette()
# palette.setColor(QPalette.ButtonText, Qt.blue)
# app.setPalette(palette)
# window = QWidget()
# layout = QVBoxLayout()
# layout.addWidget(QPushButton('Top'))
# layout.addWidget(QPushButton('Bottom'))
# window.setLayout(layout)
# window.show()
# app.exec()
# =============================================================================
# =============================================================================
# from PyQt5.QtWidgets import QApplication, QPushButton, QMessageBox
# app = QApplication([])
# button = QPushButton('Click')
# def on_button_clicked():
#     alert = QMessageBox()
#     alert.setText('You clicked the button!')
#     alert.exec()
#
# button.clicked.connect(on_button_clicked)
# button.show()
# app.exec()
# =============================================================================
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
import sys

class Window(QMainWindow):
    def __init__(self):#конструктор
        super(Window, self).__init__()

        self.setWindowTitle("Фракталы")
        self.setGeometry(300, 250, 350, 200)

        self.new_text = QtWidgets.QLabel(self)

        self.main_text = QtWidgets.QLabel(self)
        self.main_text.setText("Надпись")
        self.main_text.move(150, 100)
        self.main_text.adjustSize()

        self.btn = QtWidgets.QPushButton(self)
        self.btn.move(70, 150)
        self.btn.setText("Нажми на меня")
        self.btn.setFixedWidth(200)
        self.btn.clicked.connect(self.add_label)

    def add_label(self):
        self.new_text.setText("Пока")
        self.new_text.move(150, 50)
        self.new_text.adjustSize()
        error = QMessageBox()#создание предупреждения
        error.setWindowTitle("Error")
        error.setText("We can not do it.")
        error.setIcon(QMessageBox.Warning)
        error.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
        error.setDefaultButton(QMessageBox.Ok)#подсвечивает кнопку(по умолчанию первая)
        error.setInformativeText("Два раза действие не выполнить")
        error.setDetailedText("Детали")
        error.exec_()

def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())

application()
