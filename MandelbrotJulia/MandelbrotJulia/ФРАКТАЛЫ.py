from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, \
    QSlider, QStyle, QSizePolicy, QFileDialog
import sys
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtGui import QIcon, QPalette
from PyQt5.QtCore import Qt, QUrl

sizef = 1.0/2

def mandelbrot(amin, amax, apoints, bmin, bmax, bpoints, n, max_iterations=300, infinity_border=10):
    image = np.zeros((apoints, bpoints))
    a, b = np.mgrid[amin:amax:(apoints*1j), bmin:bmax:(bpoints*1j)]
    c = a + 1j*b
    z = np.zeros_like(c)
    for k in range(max_iterations):
        z = z**n + c
        mask = (np.abs(z) > infinity_border) & (image == 0)
        image[mask] = k
        z[mask] = np.nan

    return -image.T

fig = plt.figure(figsize=(10, 10))

def zoommandelbrot(i, x0, y0, n):
    amin, amax, bmin, bmax = -2.5, 1.5, -2, 2
    a_center, b_center = x0, y0
    scalefactor = 1 / i
    amin_ = (amin - a_center) * scalefactor + a_center
    bmin_ = (bmin - b_center) * scalefactor + b_center
    amax_ = (amax - a_center) * scalefactor + a_center
    bmax_ = (bmax - b_center) * scalefactor + b_center
    # ax = plt.gca()
    # plt.axis([-2.5, 1.5, -2, 2])
    image = mandelbrot(amin_, amax_, 500, bmin_, bmax_, 500, n)
    # ax = plt.gca()
    # plt.axis([-2.5, 1.5, -2, 2])
    plt.imshow(image, cmap='ocean', vmin=-500, vmax=0,extent=(amin_, amax_, bmin_, bmax_))
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    # plt.axis([-2.5, 1.5, -2, 2])
    plt.savefig('картинки/imagem.png')

def julia(amin, amax, apoints, bmin, bmax, bpoints, cre, cim, max_iterations=300, infinity_border=10):
    image = np.zeros((apoints, bpoints))
    a, b = np.mgrid[amin:amax:(apoints*1j), bmin:bmax:(bpoints*1j)]
    z = a + 1j*b
    c = (cre+cim*1j)*np.ones_like(z)
    for k in range(max_iterations):
        z = z**2 + c
        mask = (np.abs(z) > infinity_border) & (image == 0)
        image[mask] = k
        z[mask] = np.nan
    return -image.T

def zoomjulia(i, x0, y0, cre, cim):
    amin, amax, bmin, bmax = -2, 2, -2, 2
    a_center, b_center = x0, y0
    scalefactor = 1 / i
    amin_ = (amin - a_center) * scalefactor + a_center
    bmin_ = (bmin - b_center) * scalefactor + b_center
    amax_ = (amax - a_center) * scalefactor + a_center
    bmax_ = (bmax - b_center) * scalefactor + b_center
    # plt.axis([amin_, amax_, bmin_, bmax_])
    # fig = plt.figure(figsize=(10, 10))
    image = julia(amin_, amax_, 500, bmin_, bmax_, 500, cre, cim)
    plt.imshow(image, cmap='ocean', vmin=-100, vmax=0,extent=(amin_, amax_, bmin_, bmax_))
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.savefig('картинки/imagej.png')

def resize(width, height, image):
    img = Image.open(image)
    resized_img = img.resize((width, height), Image.ANTIALIAS)
    resized_img.save(image)

class Ui_Start(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        resize(18, 18, 'картинки/icon.PNG')
        MainWindow.setWindowIcon(QtGui.QIcon('картинки/icon.PNG'))
        MainWindow.resize(1200*sizef, 800*sizef)
        MainWindow.setMinimumSize(QtCore.QSize(400, 400))
        MainWindow.setMaximumSize(QtCore.QSize(1920, 1180))
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(0, 170, 255, 255));\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(540*sizef, 940*sizef, 362*sizef, 102*sizef))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80*sizef, 60*sizef, 1062*sizef, 600*sizef))
        self.label.setMaximumSize(QtCore.QSize(1920, 1000))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80*sizef, 662*sizef, 562*sizef, 82*sizef))
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(960*sizef, 660*sizef, 182*sizef, 82*sizef))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12*sizef)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label.raise_()
        self.pushButton.raise_()
        self.label_2.raise_()
        self.pushButton_2.raise_()
        self.pushButton_2.clicked.connect(self.start)
        # self.c = Communicate()
        # self.c.closeApp.connect(self.close)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def start(self):
        MainWindow.close()
        a2.setupUi(MainWindow)
        MainWindow.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Фракталы"))
        self.pushButton.setText(_translate("MainWindow", "Чтобы войти в программу нажмите эту кнопку"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:(18*sizef)pt; font-weight:600; vertical-align:super;\">Институт системного анализа и управления</span></p><p align=\"center\"><span style=\" font-size:(18*sizef)pt; font-weight:600; vertical-align:super;\">Кафедра распределенных информационно-вычислительных систем</span></p><p align=\"center\"><span style=\" font-size:(18*sizef)pt; font-weight:600; vertical-align:super;\">Курсовая работа по ПЯВУ</span></p><p align=\"center\"><span style=\" font-size:(18*sizef)pt; font-weight:600; vertical-align:super;\">Тема: Фракталы</span></p><p><br/></p><p><br/></p><p align=\"right\"><span style=\" font-size:(18*sizef)pt; font-weight:600; vertical-align:super;\">Выполнила: студентка группы № 1181</span></p><p align=\"right\"><span style=\" font-size:(18*sizef)pt; font-weight:600; vertical-align:super;\">Новикова Татьяна Сергеевна</span></p><p align=\"right\"><span style=\" font-size:(18*sizef)pt; font-weight:600; vertical-align:super;\">Руководитель: старший преподаватель </span></p><p align=\"right\"><span style=\" font-size:(18*sizef)pt; font-weight:600; vertical-align:super;\">Булякова Ирина Александровна</span></p><p><span style=\" font-weight:600;\"><br/></span></p><p><span style=\" font-weight:600;\"><br/></span></p><p align=\"center\"><span style=\" font-weight:600;\"><br/></span></p><p align=\"center\"><span style=\" font-size:(18*sizef)pt; font-weight:600; vertical-align:super;\">Дубна, 2021</span></p><p><br/></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:(12*sizef)pt; font-weight:600;\">Чтобы начать знакомство с динамическими </span></p><p><span style=\" font-size:(12*sizef)pt; font-weight:600;\">фракталами - нажмите на кнопку -&gt;</span></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "Приступить"))

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200*sizef, 800*sizef)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(0, 170, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(490*sizef, 200*sizef, 370*sizef, 34*sizef))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.openmandelbrot)
        self.pushButtonvm = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonvm.setGeometry(QtCore.QRect(500*sizef, 250*sizef, 270*sizef, 34*sizef))
        self.pushButtonvm.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButtonvm.setObjectName("pushButton")
        self.pushButtonvm.clicked.connect(self.videomandelbrot)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(200*sizef, 560*sizef, 370*sizef, 34*sizef))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.openjulia)
        self.pushButton_2vj = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2vj.setGeometry(QtCore.QRect(210*sizef, 510*sizef, 270*sizef, 34*sizef))
        self.pushButton_2vj.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_2vj.setObjectName("pushButton_2")
        self.pushButton_2vj.clicked.connect(self.videojulia)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(340*sizef, 0*sizef, 182*sizef, 182*sizef))
        self.label.setText("")
        resize(int(182*sizef), int(182*sizef), 'картинки/м12.PNG')
        self.label.setPixmap(QtGui.QPixmap("картинки/м12.PNG"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0*sizef, 40*sizef, 322*sizef, 322*sizef))
        self.label_2.setText("")
        resize(int(322*sizef), int(322*sizef), 'картинки/м2.PNG')
        self.label_2.setPixmap(QtGui.QPixmap("картинки/м2.PNG"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(860*sizef, 20*sizef, 342*sizef, 342*sizef))
        self.label_3.setText("")
        resize(int(342*sizef), int(342*sizef), 'картинки/м3.PNG')
        self.label_3.setPixmap(QtGui.QPixmap("картинки/м3.PNG"))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(1000*sizef, 380*sizef, 202*sizef, 202*sizef))
        self.label_4.setText("")
        resize(int(202*sizef), int(202*sizef), 'картинки/julia12.png')
        self.label_4.setPixmap(QtGui.QPixmap("картинки/julia12.png"))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(0*sizef, 500*sizef, 202*sizef, 202*sizef))
        self.label_5.setText("")
        resize(int(202*sizef), int(202*sizef), 'картинки/julia21.png')
        self.label_5.setPixmap(QtGui.QPixmap("картинки/julia21.png"))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(220*sizef, 600*sizef, 202*sizef, 202*sizef))
        self.label_6.setText("")
        resize(int(202*sizef), int(202*sizef), 'картинки/julia31.png')
        self.label_6.setPixmap(QtGui.QPixmap("картинки/julia31.png"))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(780*sizef, 460*sizef, 202*sizef, 202*sizef))
        self.label_7.setText("")
        resize(int(202*sizef), int(202*sizef), 'картинки/julia41.png')
        self.label_7.setPixmap(QtGui.QPixmap("картинки/julia41.png"))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(560*sizef, 400*sizef, 202*sizef, 202*sizef))
        self.label_8.setText("")
        resize(int(202*sizef), int(202*sizef), 'картинки/julia51.png')
        self.label_8.setPixmap(QtGui.QPixmap("картинки/julia51.png"))
        self.label_8.setObjectName("label_8")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(560*sizef, 720*sizef, 112*sizef, 34*sizef))
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(960*sizef, 720*sizef, 112*sizef, 34*sizef))
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.label_2.raise_()
        self.label.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.pushButton_3.raise_()
        self.pushButton_3.clicked.connect(self.backtostart)
        self.pushButton_4.raise_()
        self.pushButton_4.clicked.connect(self.closewindow)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12*sizef)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_3.setFont(font)
        self.pushButton_4.setFont(font)
        self.pushButton.setFont(font)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def openmandelbrot(self):
        MainWindow.close()
        m.setupUi(MainWindow)
        MainWindow.show()

    def videomandelbrot(self):
        vm.show()

    def videojulia(self):
        vj.show()
    #     window = Video()
    #     window.__init__()
    #     window.show()

    def openjulia(self):
        MainWindow.close()
        j.setupUi(MainWindow)
        MainWindow.show()

    def closewindow(self):
        MainWindow.close()
        # sys.exit(app.exec_())

    def backtostart(self):
        MainWindow.close()
        ui.setupUi(MainWindow)
        MainWindow.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Фракталы.Меню"))
        self.pushButton.setText(_translate("MainWindow", "Хочу узнать о множестве Мандельброта"))
        self.pushButtonvm.setText(_translate("MainWindow", "Анимация Мандельброта"))
        self.pushButton_2.setText(_translate("MainWindow", "Хочу узнать о множествах Жюлиа"))
        self.pushButton_2vj.setText(_translate("MainWindow", "Анимация Жюлиа"))
        self.pushButton_3.setText(_translate("MainWindow", "Назад"))
        self.pushButton_4.setText(_translate("MainWindow", "Выход"))

class Ui_Mandelbrot(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200*sizef, 800*sizef)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(0, 170, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(80*sizef, 102*sizef, 262*sizef, 32*sizef))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.teory)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(320*sizef, 20*sizef, 582*sizef, 62*sizef))
        self.label.setObjectName("label")
        self.labeld = QtWidgets.QLabel(self.centralwidget)
        self.labeld.setGeometry(QtCore.QRect(20*sizef, 230*sizef, 200*sizef, 60*sizef))
        self.labeld.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(520*sizef, 120*sizef, 650*sizef, 650*sizef))
        self.label_2.setText("")
        resize(int(650*sizef), int(650*sizef), 'картинки/man.png')
        self.label_2.setPixmap(QtGui.QPixmap("картинки/man.PNG"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20*sizef, 140*sizef, 382*sizef, 82*sizef))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0*sizef, 320*sizef, 422*sizef, 42*sizef))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(60*sizef, 384*sizef, 82*sizef, 32*sizef))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(60*sizef, 446*sizef, 82*sizef, 32*sizef))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20*sizef, 500*sizef, 402*sizef, 82*sizef))
        self.label_7.setObjectName("label_7")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(140*sizef, 600*sizef, 182*sizef, 44*sizef))
        self.spinBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.spinBox.setObjectName("spinBox")
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(1000000)
        self.spinBox2 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox2.setGeometry(QtCore.QRect(240*sizef, 240*sizef, 182*sizef, 44*sizef))
        self.spinBox2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.spinBox2.setObjectName("spinBox")
        self.spinBox2.setMinimum(2)
        self.spinBox2.setMaximum(10)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(80*sizef, 660*sizef, 262*sizef, 32*sizef))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.create)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(20*sizef, 720*sizef, 162*sizef, 32*sizef))
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.backtostart)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(260*sizef, 720*sizef, 162*sizef, 32*sizef))
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.closewindow)
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_2.setMinimum(-2.50)
        self.doubleSpinBox_2.setMaximum(1.50)
        self.doubleSpinBox_2.setSingleStep(0.01)
        self.doubleSpinBox_2.setGeometry(QtCore.QRect(200*sizef, 380*sizef, 182*sizef, 44*sizef))
        self.doubleSpinBox_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.doubleSpinBox_2.setObjectName("spinBox_2")
        self.doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_3.setGeometry(QtCore.QRect(200*sizef, 440*sizef, 182*sizef, 44*sizef))
        self.doubleSpinBox_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.doubleSpinBox_3.setObjectName("spinBox_3")
        self.doubleSpinBox_3.setMinimum(-2.00)
        self.doubleSpinBox_3.setMaximum(2.00)
        self.doubleSpinBox_3.setSingleStep(0.01)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12*sizef)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_3.setFont(font)
        self.pushButton_4.setFont(font)
        self.pushButton.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def create(self):
        x = self.doubleSpinBox_2.value()
        y = -self.doubleSpinBox_3.value()
        z = self.spinBox.value()
        n = self.spinBox2.value()

        zoommandelbrot(z, x, y, n)
        resize(int(650*sizef), int(650*sizef), 'картинки/imagem.png')
        self.label_2.setPixmap(QtGui.QPixmap("картинки/imagem.PNG"))

    def teory(self):
        a = QtWidgets.QMessageBox()
        a.setWindowTitle("Алгоритм")
        a.setWindowIcon(QtGui.QIcon('картинки/icon.PNG'))
        a.setText("Множество Мандельброта — это множество точек c на комплексной плоскости, "+
        "для которых последовательность zn, определяемая итерациями z0 = 0, z1 = z02 + с, ..., zn+1 = zn2 + c, "+
        "конечна (то есть не уходит в бесконечность). \n"+
        "Доказано, что всё множество целиком расположено внутри круга радиуса 2 на плоскости. "+
        "Поэтому будем считать, что если для точки c последовательность итераций функции fc = z^2 + c с начальным значением "+
        "z = 0 после некоторого большого их числа N (скажем, 100) не вышла за пределы этого круга, "+
        "то точка принадлежит множеству и красится в черный цвет. Соответственно, если на каком-то этапе, "+
        "меньшем N, элемент последовательности по модулю стал больше 2, то точка множеству не принадлежит и остается " +
        "белой. \nТаким образом, можно получить черно-белое изображение множества, которое и было получено Мандельбротом. "+
        "Чтобы сделать его цветным, можно, например, каждую точку не из множества красить в цвет, соответствующий номеру"+
        " итерации, на котором ее последовательность вышла за пределы круга.")
        a.setStandardButtons(a.Ok)
        a.exec_()
    def closewindow(self):
        MainWindow.close()
    def backtostart(self):
        MainWindow.close()
        a2.setupUi(MainWindow)
        MainWindow.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Фракталы.Мандельброт"))
        self.pushButton.setText(_translate("MainWindow", "Теоретическая справка"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:(18*sizef)pt; font-weight:600;\">Множество Мандельброта</span></p></body></html>"))
        self.labeld.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:(10*sizef)pt; text-decoration: underline;\">Степень = </span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:(14*sizef)pt; font-weight:600;\">Построение мнижества</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:(10*sizef)pt; text-decoration: underline;\">Введите координаты точки увеличения</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:(10*sizef)pt; font-weight:600;\">x = </span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:(10*sizef)pt; font-weight:600;\">y = </span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:(10*sizef)pt; text-decoration: underline;\">Введите во сколько раз нужно </span></p><p align=\"center\"><span style=\" font-size:(10*sizef)pt; text-decoration: underline;\">приблизить фрактал</span></p><p align=\"center\"><br/></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "Построить"))
        self.pushButton_3.setText(_translate("MainWindow", "Меню"))
        self.pushButton_4.setText(_translate("MainWindow", "Выход"))

class Ui_Julia(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200*sizef, 800*sizef)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(0, 170, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(80*sizef, 86*sizef, 262*sizef, 32*sizef))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.teory)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(320*sizef, 20*sizef, 582*sizef, 62*sizef))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(520*sizef, 120*sizef, 650*sizef, 650*sizef))
        self.label_2.setText("")
        resize(int(650*sizef), int(650*sizef), 'картинки/jul.png')
        self.label_2.setPixmap(QtGui.QPixmap("картинки/jul.png"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40*sizef, 120*sizef, 382*sizef, 82*sizef))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0*sizef, 320*sizef, 422*sizef, 42*sizef))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(60*sizef, 384*sizef, 82*sizef, 32*sizef))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(60*sizef, 446*sizef, 82*sizef, 32*sizef))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20*sizef, 500*sizef, 402*sizef, 82*sizef))
        self.label_7.setObjectName("label_7")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(140*sizef, 600*sizef, 182*sizef, 44*sizef))
        self.spinBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.spinBox.setObjectName("spinBox")
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(1000000)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(80*sizef, 660*sizef, 262*sizef, 32*sizef))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.create)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(20*sizef, 720*sizef, 162*sizef, 32*sizef))
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.backtostart)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(260*sizef, 720*sizef, 162*sizef, 32*sizef))
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.closewindow)
        self.doublespinBox_2 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doublespinBox_2.setGeometry(QtCore.QRect(200*sizef, 380*sizef, 182*sizef, 44*sizef))
        self.doublespinBox_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.doublespinBox_2.setMinimum(-2)
        self.doublespinBox_2.setMaximum(2)
        self.doublespinBox_2.setSingleStep(0.01)
        self.doublespinBox_2.setObjectName("spinBox_2")
        self.doublespinBox_3 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doublespinBox_3.setGeometry(QtCore.QRect(200*sizef, 440*sizef, 182*sizef, 44*sizef))
        self.doublespinBox_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.doublespinBox_3.setMinimum(-2)
        self.doublespinBox_3.setMaximum(2)
        self.doublespinBox_3.setSingleStep(0.01)
        self.doublespinBox_3.setObjectName("spinBox_3")
        self.doublespinBox_4 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doublespinBox_4.setGeometry(QtCore.QRect(96*sizef, 270*sizef, 122*sizef, 44*sizef))
        self.doublespinBox_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.doublespinBox_4.setMinimum(-10)
        self.doublespinBox_4.setMaximum(10)
        self.doublespinBox_4.setSingleStep(0.01)
        self.doublespinBox_4.setObjectName("spinBox_4")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10*sizef, 280*sizef, 82*sizef, 32*sizef))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(0*sizef, 220*sizef, 422*sizef, 42*sizef))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(230*sizef, 280*sizef, 32*sizef, 32*sizef))
        self.label_10.setObjectName("label_10")
        self.doublespinBox_5 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doublespinBox_5.setGeometry(QtCore.QRect(276*sizef, 270*sizef, 122*sizef, 44*sizef))
        self.doublespinBox_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.doublespinBox_5.setMinimum(-10)
        self.doublespinBox_5.setMaximum(10)
        self.doublespinBox_5.setSingleStep(0.01)
        self.doublespinBox_5.setObjectName("spinBox_5")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(410*sizef, 280*sizef, 32*sizef, 32*sizef))
        self.label_11.setObjectName("label_11")
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12*sizef)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_3.setFont(font)
        self.pushButton_4.setFont(font)
        self.pushButton.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def create(self):
        cr = self.doublespinBox_4.value()
        ci = -self.doublespinBox_5.value()
        x = self.doublespinBox_2.value()
        y = -self.doublespinBox_3.value()
        z = self.spinBox.value()

        zoomjulia(z, x, y, cr, ci)
        resize(int(650*sizef), int(650*sizef), 'картинки/imagej.png')
        # self.label.setText(str(z))
    # def t(self):
        self.label_2.setPixmap(QtGui.QPixmap("картинки/imagej.PNG"))

    def teory(self):
        a = QtWidgets.QMessageBox()#создание предупреждения
        a.setWindowTitle("Алгоритм")
        a.setWindowIcon(QtGui.QIcon('картинки/icon.PNG'))
        a.setText("Опишем в общих чертах процедуру рисования множества Жюлиа многочлена z^2 + c "+
        "для конкретного значения комплексного параметра c = p + iq. \n"+
        "Будем считать, что экран прямоугольный и состоит из a × b точек и что изображение будет покрашено"+
        " в K + 1 цвет (то есть цвета пронумерованы от 0 до K, причем цвет номер 0 — черный, а для других цветов"+
        " условимся, что чем больше номер цвета, тем быстрее «убегает на бесконечность» точка, которую мы покрасим "+
        "в этот цвет). Еще необходимо выбрать область плоскости, которую выведем на экран (для начала подойдет "+
        "квадрат {|Re z| ≤ 2, |Im z| ≤ 2}; его нужно разрезать на a × b прямоугольников, каждый из которых будет "+
        "выступать в роли точки экрана), и радиус R круга D, точки снаружи которого будем считать «бесконечно далекими»"+
        " (можно взять R = 10). \nДля каждой точки z0 = (x0; y0) экрана (то есть центра соответствующего прямоугольника)"+
        " нужно в цикле последовательно вычислять zk+1 по zk, используя формулу. Признаком остановки цикла является "+
        "выполнение одного из двух условий: либо на k-м шаге точка zk вышла из круга D (то есть верно неравенство, "+
        "и тогда точку z0 нужно покрасить в цвет номер k, либо оказалось, что k = K + 1, тогда мы считаем, что точка "+
        "z0 лежит внутри множества Жюлиа, и красим ее в черный. В результате работы программы на экран будет выведена"+
        " квадратная область комплексной плоскости {|Re z| ≤ 2, |Im z| ≤ 2}, на которой черным цветом будет изображено"+
        " множество Жюлиа многочлена z^2 + c для выбранного параметра c = p + iq, а остальные точки будут раскрашены"+
        " в K цветов. \nУвеличивая числа a и b, можно повышать разрешение экрана и тем самым улучшать качество"+
        " изображения. Меняя K и подбирая соответствие между цветами и их номерами, можно добиться довольно красивых"+
        " картинок.")
        a.setStandardButtons(a.Ok)
        a.exec_()

    def closewindow(self):
        MainWindow.close()
    def backtostart(self):
        MainWindow.close()
        a2.setupUi(MainWindow)
        MainWindow.show()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Фракталы.Жюлиа"))
        self.pushButton.setText(_translate("MainWindow", "Теоретическая справка"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:(18*sizef)pt; font-weight:600;\">Множество Жюлиа</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:(14*sizef)pt; font-weight:600;\">Построение мнижества</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:(10*sizef)pt; text-decoration: underline;\">Введите координаты точки увеличения</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:(10*sizef)pt; font-weight:600;\">x = </span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:(10*sizef)pt; font-weight:600;\">y = </span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:(10*sizef)pt; text-decoration: underline;\">Введите во сколько раз нужно </span></p><p align=\"center\"><span style=\" font-size:(10*sizef)pt; text-decoration: underline;\">приблизить фрактал</span></p><p align=\"center\"><br/></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "Построить"))
        self.pushButton_3.setText(_translate("MainWindow", "Меню"))
        self.pushButton_4.setText(_translate("MainWindow", "Выход"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:(10*sizef)pt; font-weight:600;\">с = </span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:(10*sizef)pt; text-decoration: underline;\">Введите параметр с</span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">+</span></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">*i</span></p></body></html>"))

class Video(QWidget):
    def __init__(self, filename):
        self.filename=filename
        super().__init__()
        self.setWindowTitle("Анимация")
        self.setWindowIcon(QtGui.QIcon('картинки/icon.PNG'))
        self.setGeometry(0*sizef, 0*sizef, 900*sizef, 1000*sizef)
        p =self.palette()
        p.setColor(QPalette.Window, Qt.white)
        self.setPalette(p)
        self.init_ui()
    def init_ui(self):
        #create media player object
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        #create videowidget object
        videowidget = QVideoWidget()
        #create open button
        openBtn = QPushButton('Open Video')
        openBtn.clicked.connect(self.open_file)
        #create button for playing
        self.playBtn = QPushButton()
        self.playBtn.setEnabled(False)
        self.playBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playBtn.clicked.connect(self.play_video)
        #create slider
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0,0)
        self.slider.sliderMoved.connect(self.set_position)
        #create label
        self.label = QLabel()
        self.label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        #create hbox layout
        hboxLayout = QHBoxLayout()
        hboxLayout.setContentsMargins(0,0,0,0)
        #set widgets to the hbox layout
        hboxLayout.addWidget(openBtn)
        hboxLayout.addWidget(self.playBtn)
        hboxLayout.addWidget(self.slider)
        #create vbox layout
        vboxLayout = QVBoxLayout()
        vboxLayout.addWidget(videowidget)
        vboxLayout.addLayout(hboxLayout)
        vboxLayout.addWidget(self.label)
        self.setLayout(vboxLayout)
        self.mediaPlayer.setVideoOutput(videowidget)
        #media player signals
        self.mediaPlayer.stateChanged.connect(self.mediastate_changed)
        self.mediaPlayer.positionChanged.connect(self.position_changed)
        self.mediaPlayer.durationChanged.connect(self.duration_changed)

    def open_file(self):
        self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(self.filename)))
        self.playBtn.setEnabled(True)
    def play_video(self):


        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()

    def mediastate_changed(self, state):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.playBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.playBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))

    def position_changed(self, position):
        self.slider.setValue(position)

    def duration_changed(self, duration):
        self.slider.setRange(0, duration)

    def set_position(self, position):
        self.mediaPlayer.setPosition(position)

    def handle_errors(self):
        self.playBtn.setEnabled(False)
        self.label.setText("Error: " + self.mediaPlayer.errorString())

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Start()
    a2=Ui_MainWindow()
    m=Ui_Mandelbrot()
    j=Ui_Julia()
    vj=Video('анимация/julia.gif')
    vm=Video('анимация/mandelbrot1.gif')
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
