from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia
import sys
# import os
# os.system("python 2.py")
from two import Ui_MainWindow

class Ui_Start(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        MainWindow.setMinimumSize(QtCore.QSize(200, 200))
        MainWindow.setMaximumSize(QtCore.QSize(1920, 1180))
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(0, 170, 255, 255));\n"
"")
        # self.video = QtWidgets.QMediaPlayer(self.centralwidget)
        # self.mediaPlayer = QtMultimedia.QMediaPlayer()
        # self.mediaPlayer.setVideoOutput(self)
        # fileName = "C:/Users/novta/Desktop/python/mandelbrot1.mp4"
        # url = QtCore.QUrl.fromLocalFile(fileName)
        # # url = QtCore.QUrl("http://clips.vorwaerts-gmbh.de/VfE_html5.mp4")
        # self.mediaPlayer.setMedia(QtMultimedia.QMediaContent(url))
        # self.mediaPlayer.play()

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(270, 470, 181, 51))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 30, 531, 251))
        self.label.setMaximumSize(QtCore.QSize(1920, 1000))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 330, 281, 41))
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(480, 330, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label.raise_()
        self.pushButton.raise_()
        self.label_2.raise_()
        self.pushButton_2.raise_()
        self.pushButton_2.clicked.connect(self.t)
        # self.c = Communicate()
        # self.c.closeApp.connect(self.close)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    # global window2
    # window2 = None
    def t(self):
        MainWindow.close()
        # if __name__ == "__main__":
        #
        #     app = QtWidgets.QApplication(sys.argv)
        #     MainWindow = QtWidgets.QMainWindow()
        #     ui = Ui_MainWindow()
        #     ui.setupUi(MainWindow)
        #     MainWindow.show()
        #     sys.exit(app.exec_())
        #MainWindow1 = QtWidgets.QMainWindow()
        # a=Ui_MainWindow()
        a2.setupUi(MainWindow)
        MainWindow.show()
        #sys.exit(app.exec_())
        #app = QtWidgets.QApplication(sys.argv)
        # MainWindow2 = QtWidgets.QMainWindow()
        # ui = Ui_MainWindow()
        # ui.setupUi(MainWindow2)
        # MainWindow2.show()
        # app.exec()

        # if window2 is None:
        # self.close()
        # self.destroy()
        # window2 = QtWidgets.QMainWindow()
        # ui = Ui_MainWindow()
        # ui.setupUi(window2)
        # window2.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Фракталы"))
        self.pushButton.setText(_translate("MainWindow", "Чтобы войти в программу нажмите эту кнопку"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; vertical-align:super;\">Институт системного анализа и управления</span></p><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; vertical-align:super;\">Кафедра распределенных информационно-вычислительных систем</span></p><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; vertical-align:super;\">Курсовая работа по ПЯВУ</span></p><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; vertical-align:super;\">Тема: Фракталы</span></p><p><br/></p><p><br/></p><p align=\"right\"><span style=\" font-size:18pt; font-weight:600; vertical-align:super;\">Выполнила: студентка группы № 1181</span></p><p align=\"right\"><span style=\" font-size:18pt; font-weight:600; vertical-align:super;\">Новикова Татьяна Сергеевна</span></p><p align=\"right\"><span style=\" font-size:18pt; font-weight:600; vertical-align:super;\">Руководитель: старший преподаватель </span></p><p align=\"right\"><span style=\" font-size:18pt; font-weight:600; vertical-align:super;\">Булякова Ирина Александровна</span></p><p><span style=\" font-weight:600;\"><br/></span></p><p><span style=\" font-weight:600;\"><br/></span></p><p align=\"center\"><span style=\" font-weight:600;\"><br/></span></p><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; vertical-align:super;\">Дубна, 2021</span></p><p><br/></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Чтобы начать знакомство с динамическими </span></p><p><span style=\" font-size:12pt; font-weight:600;\">фракталами - нажмите на кнопку -&gt;</span></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "Приступить"))

# class MyForm(QtWidgets.QMainWindow):
#     def __init__(self, parent = None):
#         super(MyForm, self).__init__(parent)
#         self.form = Ui_MainWindow()
#         self.form.setupUi(self)

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Start()
    a2=Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()


    sys.exit(app.exec_())
