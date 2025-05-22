from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")


        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 60, 1062, 600))
        self.label.setMaximumSize(QtCore.QSize(1920, 1000))
        self.label.setObjectName("label")
        self.label.setMovie(self, "C:/Users/novta/Desktop/python/save_wave.gif")

        #self.label.setPixmap(QtGui.QPixmap("gif.gif"))             # ---
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Фракталы.Меню"))

class ExampleApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        path='gif.gif'
        gif = QtGui.QMovie("C:/Users/novta/Desktop/python/save_wave.gif")                     # !!!
        self.label.setMovie(gif)
        gif.start()

        print('Gif label')


if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    sys.exit(app.exec_())
