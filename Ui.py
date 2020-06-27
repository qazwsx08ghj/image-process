# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\UI.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import numpy as np


class image_process:
    def __init__(self):
        pass

    def image_smoothing(self, **kwargs):
        salt = self.add_salt(kwargs['img'], kwargs['n'])
        if kwargs['method'] == "中值" or kwargs['method'] == "方法":
            return self.alter_to_Qimage_datatype(cv2.medianBlur(salt, 5))
        elif kwargs['method'] == "均值":
            return self.alter_to_Qimage_datatype(cv2.blur(salt, (5, 5)))
        elif kwargs['method'] == "高斯":
            return self.alter_to_Qimage_datatype(cv2.GaussianBlur(salt, (5, 5), 0))
        elif kwargs['method'] == "雙邊":
            return self.alter_to_Qimage_datatype(cv2.bilateralFilter(salt, 9, 75, 75))

    def edge_detection(self, **kwargs):

        if kwargs['method'] == "方法":
            lap = cv2.Laplacian(kwargs['img'], cv2.CV_64F)
            lap = np.uint8(np.absolute(lap))
            return self.alter_to_Qimage_datatype(lap)
        elif kwargs['method'] == 'Sobel':
            sobelX = cv2.Sobel(kwargs['img'], cv2.CV_64F, 1, 0)
            sobelY = cv2.Sobel(kwargs['img'], cv2.CV_64F, 0, 1)
            sobelX = np.uint8(np.absolute(sobelX))
            sobelY = np.uint8(np.absolute(sobelY))
            sobelCombined = cv2.bitwise_or(sobelX, sobelY)
            return self.alter_to_Qimage_datatype(sobelCombined)
        elif kwargs['method'] == 'Canny':
            canny = cv2.Canny(kwargs['img'], 30, 150)
            return self.alter_to_Qimage_datatype(canny)

        elif kwargs['method'] == '拉普拉斯':
            lap = cv2.Laplacian(kwargs['img'], cv2.CV_64F)
            lap = np.uint8(np.absolute(lap))
            return self.alter_to_Qimage_datatype(lap)

    def lighten(self, **kwargs):
        M = np.ones(kwargs['img'].shape, dtype="uint8") * 100
        if kwargs['method'] == "方法" or kwargs['method'] == "調亮":
            return self.alter_to_Qimage_datatype(cv2.add(kwargs['img'], M))
        elif kwargs['method'] == '調暗':
            cv2.subtract(kwargs['img'], M)
            return self.alter_to_Qimage_datatype(cv2.subtract(kwargs['img'], M))

    def add_salt(self, img, n):

        m = int((img.shape[0] * img.shape[1]) * n)
        for a in range(m):
            i = int(np.random.random() * img.shape[1])
            j = int(np.random.random() * img.shape[0])
            if img.ndim == 2:
                img[j, i] = 255
            elif img.ndim == 3:
                img[j, i, 0] = 255
                img[j, i, 1] = 255
                img[j, i, 2] = 255
        for b in range(m):
            i = int(np.random.random() * img.shape[1])
            j = int(np.random.random() * img.shape[0])
            if img.ndim == 2:
                img[j, i] = 0
            elif img.ndim == 3:
                img[j, i, 0] = 0
                img[j, i, 1] = 0
                img[j, i, 2] = 0
        return img

    def contrast_enhancement(self, **kwargs):
        # N = np.ones(args[0].shape, dtype="uint8") * 4
        # mult = cv2.multiply(args[0], N)
        # Div = cv2.divide(args[0], N)
        # i = np.hstack((mult, Div))
        N = np.ones(kwargs['img'].shape, dtype="uint8") * 4
        if kwargs['method'] == "方法" or kwargs['method'] == "增加":
            return self.alter_to_Qimage_datatype(cv2.multiply(kwargs['img'], N))
        elif kwargs['method'] == '減少':
            return self.alter_to_Qimage_datatype(cv2.divide(kwargs['img'], N))

    def alter_to_Qimage_datatype(self, img):
        try:
            height, width, channel = img.shape
            bytesPerLine = 3 * width
            img = QtGui.QImage(img.data, width, height, bytesPerLine,
                               QtGui.QImage.Format_RGB888).rgbSwapped()
            return img
        except ValueError:
            '''
            This error because when you do canny function it turn to bin status so 
            need to turn the result to BGR result and qtimage only can let BGR turn to 
            RGP 
            '''
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
            height, width, channel = img.shape
            bytesPerLine = 3 * width
            img = QtGui.QImage(img.data, width, height, bytesPerLine,
                               QtGui.QImage.Format_RGB888).rgbSwapped()
            # height, width = img.shape
            # bytesPerLine = 3 * width
            # img = QtGui.QImage(img.data, width, height, bytesPerLine,
            #                    QtGui.QImage.Format_RGB888).rgbSwapped()
            return img


image_process = image_process()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(947, 721)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 921, 571))
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setText("")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 590, 341, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(360, 590, 21, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.openfile)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(740, 640, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.image_smoothing)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(470, 640, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.lighten)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(560, 640, 75, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.edge_detection)
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(650, 640, 75, 23))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.contrast_enhancement)
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(560, 610, 71, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(740, 610, 71, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_4 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_4.setGeometry(QtCore.QRect(470, 610, 71, 22))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_5 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_5.setGeometry(QtCore.QRect(650, 610, 71, 22))
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 947, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "..."))
        self.pushButton_2.setText(_translate("MainWindow", "模糊化"))
        self.pushButton_4.setText(_translate("MainWindow", "亮度調整"))
        self.pushButton_5.setText(_translate("MainWindow", "邊緣偵測"))
        self.pushButton_6.setText(_translate("MainWindow", "對比度調整"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "方法"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "拉普拉斯"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Sobel"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "Canny"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "方法"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "中值"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "均值"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "高斯"))
        self.comboBox_3.setItemText(4, _translate("MainWindow", "雙邊"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "方法"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "調亮"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "調暗"))
        self.comboBox_5.setItemText(0, _translate("MainWindow", "方法"))
        self.comboBox_5.setItemText(1, _translate("MainWindow", "增加"))
        self.comboBox_5.setItemText(2, _translate("MainWindow", "減少"))

    def openfile(self):
        filename = QtWidgets.QFileDialog.getOpenFileName()
        self.img_path = filename[0]
        self.lineEdit.setText(self.img_path)
        pix_map = QtGui.QPixmap(self.img_path)
        self.label.setPixmap(QtGui.QPixmap(pix_map))
        self.label.resize(pix_map.width(), pix_map.height())

    def image_smoothing(self):
        self.img = cv2.imread(self.img_path)
        method = str(self.comboBox_3.currentText())
        self.img = image_process.image_smoothing(img=self.img, method=method, n=0.02)
        self.label.setPixmap(QtGui.QPixmap.fromImage(self.img))

    def edge_detection(self):
        img = cv2.imread(self.img_path)
        self.img = img
        method = str(self.comboBox_2.currentText())
        self.label.setPixmap(QtGui.QPixmap.fromImage(image_process.edge_detection(img=img, method=method)))

    def lighten(self):
        img = cv2.imread(self.img_path)
        method = str(self.comboBox_4.currentText())
        image_process.lighten(img=img, method=method)
        self.label.setPixmap(QtGui.QPixmap.fromImage(image_process.lighten(img=img, method=method)))

    def contrast_enhancement(self):
        img = cv2.imread(self.img_path)
        method = str(self.comboBox_5.currentText())
        image_process.contrast_enhancement(img=img, method=method)
        self.label.setPixmap(QtGui.QPixmap.fromImage(image_process.contrast_enhancement(img=img, method=method)))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
