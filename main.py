from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QListWidgetItem, QTableWidgetItem
import requests
import psutil
from cryptography.fernet import Fernet
import cryptography
import os
import ctypes
import pickle
import pyperclip
from threading import Timer
import random
import string


class Api():
    def __init__(self, baseUrl):
        self.baseUrl = baseUrl
        self.token = ""
        self.expectedStatus = [200, 400, 500]

    def register(self, email, password):
        url = self.baseUrl + '/auth/register'
        data = {'email': email, 'password': password}
        response = requests.post(url, json=data)
        if response.status_code in self.expectedStatus:
            return response.json()
        raise Exception("Erro interno no servidor")

    def login(self, email, password):
        url = self.baseUrl + '/auth/login'
        data = {'email': email, 'password': password}
        response = requests.post(url, json=data)
        if response.status_code in self.expectedStatus:
            return response.json()
        raise Exception("Erro interno no servidor")

    def savePassword(self, dataHash):
        url = self.baseUrl + '/password'
        data = {'hashs': [dataHash]}
        headers = {'token': self.token}
        response = requests.post(url, json=data, headers=headers)
        if response.status_code in self.expectedStatus:
            return response.json()
        raise Exception("Erro interno no servidor")

    def getPasswords(self):
        url = self.baseUrl + '/password'
        headers = {'token': self.token}
        response = requests.get(url=url, headers=headers)
        if response.status_code in self.expectedStatus:
            return response.json()
        raise Exception("Erro interno no servidor")


class Ui_MainWindow(object):
    def __init__(self):
        #self.api = Api("http://pysword.onrender.com")
        self.api = Api("http://152.67.61.229:5000")
        #self.api = Api("http://localhost:5000")
        self.passwordData = []
        self.key = None
        self.stopClipBoardClear = False

    def showFrame(self, frameName):
        for name, frame in self.frames.items():
            if name == frameName:
                frame["frame"].show()
                if frame["callback"] is not None:
                    frame["callback"]()
            else:
                frame["frame"].hide()

    def registerFrame(self, name, frame, callback=None):
        self.frames[name] = {"frame": frame, "callback": callback}

    # ----------------UI----------------

    def setupUI(self, MainWindow):
        MainWindow.setObjectName("PySword")
        MainWindow.setFixedSize(226,298)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)

        self.frames = {}

        self.setupHomeUI(MainWindow)
        self.setupLoginUI(MainWindow)
        self.setupCadastroUI(MainWindow)
        self.setupSelectDriveUI(MainWindow)
        self.setupKeyGeneratedUI(MainWindow)
        self.setupGetKeyUI(MainWindow)
        self.setupMainUI(MainWindow)
        self.setupNewPasswordUI(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.showFrame("home")

    def setupHomeUI(self, MainWindow):
        self.home_frame = QtWidgets.QFrame(self.centralwidget)
        self.home_frame.setEnabled(True)
        self.home_frame.setGeometry(QtCore.QRect(10, 10, 201, 261))
        self.home_frame.setAutoFillBackground(False)
        self.home_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.home_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.home_frame.setObjectName("frame")
        self.home_pushButton_2 = QtWidgets.QPushButton(self.home_frame)
        self.home_pushButton_2.setGeometry(QtCore.QRect(40, 230, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.home_pushButton_2.setFont(font)
        self.home_pushButton_2.setObjectName("pushButton_2")
        self.home_label_2 = QtWidgets.QLabel(self.home_frame)
        self.home_label_2.setGeometry(QtCore.QRect(0, 0, 71, 21))
        self.home_label_2.setObjectName("label_2")
        self.home_pushButton = QtWidgets.QPushButton(self.home_frame)
        self.home_pushButton.setGeometry(QtCore.QRect(40, 190, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.home_pushButton.setFont(font)
        self.home_pushButton.setObjectName("pushButton")
        self.home_label = QtWidgets.QLabel(self.home_frame)
        self.home_label.setGeometry(QtCore.QRect(40, 50, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.home_label.setFont(font)
        self.home_label.setAlignment(QtCore.Qt.AlignCenter)
        self.home_label.setObjectName("label")
        self.home_statusbar = QtWidgets.QStatusBar(MainWindow)
        self.home_statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.home_statusbar)

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("PySword", "PySword"))
        self.home_pushButton_2.setText(_translate("PySword", "CADASTRAR"))
        self.home_label_2.setText(_translate(
            "PySword", "<html><head/><body><p><span style=\" font-size:12pt;\">PySword</span></p></body></html>"))
        self.home_pushButton.setText(_translate("PySword", "ENTRAR"))
        self.home_label.setText(_translate(
            "PySword", "<html><head/><body><p align=\"center\">BEM VINDO</p></body></html>"))

        self.registerFrame("home", self.home_frame)

    def setupLoginUI(self, MainWindow):
        self.login_frame = QtWidgets.QFrame(self.centralwidget)
        self.login_frame.setEnabled(True)
        self.login_frame.setGeometry(QtCore.QRect(10, 10, 201, 261))
        self.login_frame.setAutoFillBackground(False)
        self.login_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.login_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.login_frame.setObjectName("frame_2")
        self.login_label_3 = QtWidgets.QLabel(self.login_frame)
        self.login_label_3.setGeometry(QtCore.QRect(0, 0, 71, 21))
        self.login_label_3.setObjectName("label_3")
        self.login_pushButton_4 = QtWidgets.QPushButton(self.login_frame)
        self.login_pushButton_4.setGeometry(QtCore.QRect(40, 230, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.login_pushButton_4.setFont(font)
        self.login_pushButton_4.setObjectName("pushButton_4")
        self.login_label_4 = QtWidgets.QLabel(self.login_frame)
        self.login_label_4.setGeometry(QtCore.QRect(40, 30, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.login_label_4.setFont(font)
        self.login_label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.login_label_4.setObjectName("label_4")
        self.login_lineEdit = QtWidgets.QLineEdit(self.login_frame)
        self.login_lineEdit.setGeometry(QtCore.QRect(30, 110, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.login_lineEdit.setFont(font)
        self.login_lineEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.login_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.login_lineEdit.setObjectName("lineEdit")
        self.login_lineEdit_2 = QtWidgets.QLineEdit(self.login_frame)
        self.login_lineEdit_2.setGeometry(QtCore.QRect(30, 140, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.login_lineEdit_2.setFont(font)
        self.login_lineEdit_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.login_lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.login_lineEdit_2.setObjectName("lineEdit_2")
        self.login_statusbar = QtWidgets.QStatusBar(MainWindow)
        self.login_statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.login_statusbar)

        _translate = QtCore.QCoreApplication.translate
        self.login_label_3.setText(_translate(
            "PySword", "<html><head/><body><p><span style=\" font-size:12pt;\">PySword</span></p></body></html>"))
        self.login_pushButton_4.setText(_translate("PySword", "ENTRAR"))
        self.login_label_4.setText(_translate(
            "PySword", "<html><head/><body><p align=\"center\">LOGIN</p></body></html>"))
        self.login_lineEdit.setText(_translate("PySword", "USUÁRIO"))
        self.login_lineEdit_2.setText(_translate("PySword", "SENHA"))

        self.registerFrame("login", self.login_frame)

    def setupCadastroUI(self, MainWindow):
        self.cadastro_frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.cadastro_frame_2.setEnabled(True)
        self.cadastro_frame_2.setGeometry(QtCore.QRect(10, 10, 201, 261))
        self.cadastro_frame_2.setAutoFillBackground(False)
        self.cadastro_frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.cadastro_frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cadastro_frame_2.setObjectName("frame_2")
        self.cadastro_label_3 = QtWidgets.QLabel(self.cadastro_frame_2)
        self.cadastro_label_3.setGeometry(QtCore.QRect(0, 0, 71, 21))
        self.cadastro_label_3.setObjectName("label_3")
        self.cadastro_pushButton_4 = QtWidgets.QPushButton(
            self.cadastro_frame_2)
        self.cadastro_pushButton_4.setGeometry(QtCore.QRect(40, 230, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cadastro_pushButton_4.setFont(font)
        self.cadastro_pushButton_4.setObjectName("pushButton_4")
        self.cadastro_label_4 = QtWidgets.QLabel(self.cadastro_frame_2)
        self.cadastro_label_4.setGeometry(QtCore.QRect(40, 30, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.cadastro_label_4.setFont(font)
        self.cadastro_label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.cadastro_label_4.setObjectName("label_4")
        self.cadastro_lineEdit_2 = QtWidgets.QLineEdit(self.cadastro_frame_2)
        self.cadastro_lineEdit_2.setGeometry(QtCore.QRect(30, 140, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cadastro_lineEdit_2.setFont(font)
        self.cadastro_lineEdit_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cadastro_lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.cadastro_lineEdit_2.setClearButtonEnabled(False)
        self.cadastro_lineEdit_2.setObjectName("lineEdit_2")
        self.cadastro_lineEdit = QtWidgets.QLineEdit(self.cadastro_frame_2)
        self.cadastro_lineEdit.setGeometry(QtCore.QRect(30, 110, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cadastro_lineEdit.setFont(font)
        self.cadastro_lineEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cadastro_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.cadastro_lineEdit.setObjectName("lineEdit")
        self.cadastro_lineEdit_3 = QtWidgets.QLineEdit(self.cadastro_frame_2)
        self.cadastro_lineEdit_3.setGeometry(QtCore.QRect(30, 170, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cadastro_lineEdit_3.setFont(font)
        self.cadastro_lineEdit_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cadastro_lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.cadastro_lineEdit_3.setObjectName("lineEdit_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.cadastro_statusbar = QtWidgets.QStatusBar(MainWindow)
        self.cadastro_statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.cadastro_statusbar)
        _translate = QtCore.QCoreApplication.translate

        self.cadastro_label_3.setText(_translate(
            "PySword", "<html><head/><body><p><span style=\" font-size:12pt;\">PySword</span></p></body></html>"))
        self.cadastro_pushButton_4.setText(_translate("PySword", "CADASTRAR"))
        self.cadastro_label_4.setText(_translate(
            "PySword", "<html><head/><body><p align=\"center\">CADASTRO</p></body></html>"))
        self.cadastro_lineEdit_2.setText(_translate("PySword", "SENHA"))
        self.cadastro_lineEdit.setText(_translate("PySword", "USUÁRIO"))
        self.cadastro_lineEdit_3.setText(
            _translate("PySword", "REPETIR SENHA"))

        self.registerFrame("cadastro", self.cadastro_frame_2)

    def setupSelectDriveUI(self, MainWindow):
        self.selectdrive_frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.selectdrive_frame_2.setEnabled(True)
        self.selectdrive_frame_2.setGeometry(QtCore.QRect(10, 10, 201, 261))
        self.selectdrive_frame_2.setAutoFillBackground(False)
        self.selectdrive_frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.selectdrive_frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.selectdrive_frame_2.setObjectName("frame_2")
        self.selectdrive_label_3 = QtWidgets.QLabel(self.selectdrive_frame_2)
        self.selectdrive_label_3.setGeometry(QtCore.QRect(0, 0, 71, 21))
        self.selectdrive_label_3.setObjectName("label_3")
        self.selectdrive_pushButton_4 = QtWidgets.QPushButton(
            self.selectdrive_frame_2)
        self.selectdrive_pushButton_4.setGeometry(
            QtCore.QRect(30, 230, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.selectdrive_pushButton_4.setFont(font)
        self.selectdrive_pushButton_4.setObjectName("pushButton_4")
        self.selectdrive_label_4 = QtWidgets.QLabel(self.selectdrive_frame_2)
        self.selectdrive_label_4.setGeometry(QtCore.QRect(40, 30, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.selectdrive_label_4.setFont(font)
        self.selectdrive_label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.selectdrive_label_4.setObjectName("label_4")
        self.selectdrive_listWidget = QtWidgets.QListWidget(
            self.selectdrive_frame_2)
        self.selectdrive_listWidget.setGeometry(QtCore.QRect(10, 70, 181, 151))
        self.selectdrive_listWidget.setObjectName("listWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.selectdrive_statusbar = QtWidgets.QStatusBar(MainWindow)
        self.selectdrive_statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.selectdrive_statusbar)

        _translate = QtCore.QCoreApplication.translate
        self.selectdrive_label_3.setText(_translate(
            "PySword", "<html><head/><body><p><span style=\" font-size:12pt;\">PySword</span></p></body></html>"))
        self.selectdrive_pushButton_4.setText(
            _translate("PySword", "CRIAR CHAVE"))
        self.selectdrive_label_4.setText(_translate(
            "PySword", "<html><head/><body><p align=\"center\">CADASTRO</p></body></html>"))

        self.registerFrame("selectDrive", self.selectdrive_frame_2, self.updateDriveList)

    def setupKeyGeneratedUI(self, MainWindow):
        self.keygenerated_frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.keygenerated_frame_3.setEnabled(True)
        self.keygenerated_frame_3.setGeometry(QtCore.QRect(10, 10, 201, 261))
        self.keygenerated_frame_3.setAutoFillBackground(False)
        self.keygenerated_frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.keygenerated_frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.keygenerated_frame_3.setObjectName("frame_3")
        self.keygenerated_label_5 = QtWidgets.QLabel(self.keygenerated_frame_3)
        self.keygenerated_label_5.setGeometry(QtCore.QRect(0, 0, 71, 21))
        self.keygenerated_label_5.setObjectName("label_5")
        self.keygenerated_pushButton_5 = QtWidgets.QPushButton(
            self.keygenerated_frame_3)
        self.keygenerated_pushButton_5.setGeometry(
            QtCore.QRect(30, 230, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.keygenerated_pushButton_5.setFont(font)
        self.keygenerated_pushButton_5.setObjectName("pushButton_5")
        self.keygenerated_label_6 = QtWidgets.QLabel(self.keygenerated_frame_3)
        self.keygenerated_label_6.setGeometry(QtCore.QRect(40, 30, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.keygenerated_label_6.setFont(font)
        self.keygenerated_label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.keygenerated_label_6.setObjectName("label_6")
        self.keygenerated_label = QtWidgets.QLabel(self.keygenerated_frame_3)
        self.keygenerated_label.setGeometry(QtCore.QRect(30, 70, 151, 151))
        self.keygenerated_label.setObjectName("label")
        self.keygenerated_label_2 = QtWidgets.QLabel(self.keygenerated_frame_3)
        self.keygenerated_label_2.setGeometry(QtCore.QRect(30, 210, 151, 20))
        self.keygenerated_label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.keygenerated_statusbar = QtWidgets.QStatusBar(MainWindow)
        self.keygenerated_statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.keygenerated_statusbar)

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("PySword", "PySword"))
        self.keygenerated_label_5.setText(_translate(
            "PySword", "<html><head/><body><p><span style=\" font-size:12pt;\">PySword</span></p></body></html>"))
        self.keygenerated_pushButton_5.setText(_translate("PySword", "ENTRAR"))
        self.keygenerated_label_6.setText(_translate(
            "PySword", "<html><head/><body><p align=\"center\">CADASTRO</p></body></html>"))
        self.keygenerated_label.setPixmap(
            QPixmap(os.path.join(os.path.dirname(__file__), 'assets/check.png')))
        self.keygenerated_label_2.setText(
            _translate("PySword", "CHAVE CRIADA COM SUCESSO"))

        self.registerFrame("keyGenerated", self.keygenerated_frame_3)

    def setupGetKeyUI(self, MainWindow):
        self.getKey_frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.getKey_frame_2.setEnabled(True)
        self.getKey_frame_2.setGeometry(QtCore.QRect(10, 10, 201, 261))
        self.getKey_frame_2.setAutoFillBackground(False)
        self.getKey_frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.getKey_frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.getKey_frame_2.setObjectName("frame_2")
        self.getKey_label_3 = QtWidgets.QLabel(self.getKey_frame_2)
        self.getKey_label_3.setGeometry(QtCore.QRect(0, 0, 71, 21))
        self.getKey_label_3.setObjectName("label_3")
        self.getKey_pushButton_4 = QtWidgets.QPushButton(self.getKey_frame_2)
        self.getKey_pushButton_4.setGeometry(QtCore.QRect(20, 230, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.getKey_pushButton_4.setFont(font)
        self.getKey_pushButton_4.setObjectName("pushButton_4")
        self.getKey_label_4 = QtWidgets.QLabel(self.getKey_frame_2)
        self.getKey_label_4.setGeometry(QtCore.QRect(40, 30, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.getKey_label_4.setFont(font)
        self.getKey_label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.getKey_label_4.setObjectName("label_4")
        self.getKey_label = QtWidgets.QLabel(self.getKey_frame_2)
        self.getKey_label.setGeometry(QtCore.QRect(30, 60, 151, 161))
        self.getKey_label.setObjectName("label")
        self.getKey_label.raise_()
        self.getKey_label_3.raise_()
        self.getKey_pushButton_4.raise_()
        self.getKey_label_4.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        _translate = QtCore.QCoreApplication.translate
        self.getKey_label_3.setText(_translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">PySword</span></p></body></html>"))
        self.getKey_pushButton_4.setText(
            _translate("MainWindow", "VERIFICAR CHAVE"))
        self.getKey_label_4.setText(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\">LOGIN</p></body></html>"))
        self.getKey_label.setPixmap(QPixmap(os.path.join(
            os.path.dirname(__file__), 'assets/pendrive.png')))

        self.registerFrame("getKey", self.getKey_frame_2)

    def setupMainUI(self, MainWindow):
        self.main_frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.main_frame_2.setEnabled(True)
        self.main_frame_2.setGeometry(QtCore.QRect(10, 10, 201, 271))
        self.main_frame_2.setAutoFillBackground(False)
        self.main_frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame_2.setObjectName("frame_2")
        self.main_label_3 = QtWidgets.QLabel(self.main_frame_2)
        self.main_label_3.setGeometry(QtCore.QRect(0, 0, 71, 21))
        self.main_label_3.setObjectName("label_3")
        self.main_label_5 = QtWidgets.QLabel(self.main_frame_2)
        self.main_label_5.setGeometry(QtCore.QRect(130, 0, 71, 21))
        self.main_label_5.setObjectName("label_5")
        self.main_pushButton_4 = QtWidgets.QPushButton(self.main_frame_2)
        self.main_pushButton_4.setGeometry(QtCore.QRect(0, 240, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.main_pushButton_4.setFont(font)
        self.main_pushButton_4.setObjectName("pushButton_4")
        self.main_tableWidget = QtWidgets.QTableWidget(self.main_frame_2)
        self.main_tableWidget.setGeometry(QtCore.QRect(0, 30, 201, 201))
        self.main_tableWidget.setObjectName("tableWidget")
        self.main_tableWidget.setColumnCount(2)
        self.main_tableWidget.setHorizontalHeaderLabels(["Site", "Email"])
        self.main_tableWidget.verticalHeader().hide()
        self.main_tableWidget.setRowCount(0)
        self.main_tableWidget.horizontalScrollBar().hide()
        self.main_tableWidget.horizontalScrollBar().setDisabled(True)
        self.main_tableWidget.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOn)
        MainWindow.setCentralWidget(self.centralwidget)
        self.main_statusbar = QtWidgets.QStatusBar(MainWindow)
        self.main_statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.main_statusbar)

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.main_label_3.setText(_translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">PySword</span></p></body></html>"))
        self.main_label_5.setText(_translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">USUÁRIO</span></p></body></html>"))
        self.main_pushButton_4.setText(
            _translate("MainWindow", "ADICIONAR CONTA"))

        self.registerFrame("main", self.main_frame_2, self.getPasswords)

    def setupNewPasswordUI(self, MainWindow):
        self.newPassword_frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.newPassword_frame_2.setEnabled(True)
        self.newPassword_frame_2.setGeometry(QtCore.QRect(10, 10, 201, 271))
        self.newPassword_frame_2.setAutoFillBackground(False)
        self.newPassword_frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.newPassword_frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.newPassword_frame_2.setObjectName("frame_2")
        self.newPassword_label_3 = QtWidgets.QLabel(self.newPassword_frame_2)
        self.newPassword_label_3.setGeometry(QtCore.QRect(0, 0, 71, 21))
        self.newPassword_label_3.setObjectName("label_3")
        self.newPassword_pushButton_4 = QtWidgets.QPushButton(self.newPassword_frame_2)
        self.newPassword_pushButton_4.setGeometry(QtCore.QRect(30, 240, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.newPassword_pushButton_4.setFont(font)
        self.newPassword_pushButton_4.setObjectName("pushButton_4")
        self.newPassword_label_4 = QtWidgets.QLabel(self.newPassword_frame_2)
        self.newPassword_label_4.setGeometry(QtCore.QRect(0, 30, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.newPassword_label_4.setFont(font)
        self.newPassword_label_4.setObjectName("label_4")
        self.newPassword_lineEdit_2 = QtWidgets.QLineEdit(self.newPassword_frame_2)
        self.newPassword_lineEdit_2.setGeometry(QtCore.QRect(30, 190, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.newPassword_lineEdit_2.setFont(font)
        self.newPassword_lineEdit_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.newPassword_lineEdit_2.setText("")
        self.newPassword_lineEdit_2.setClearButtonEnabled(False)
        self.newPassword_lineEdit_2.setObjectName("lineEdit_2")
        self.newPassword_lineEdit = QtWidgets.QLineEdit(self.newPassword_frame_2)
        self.newPassword_lineEdit.setGeometry(QtCore.QRect(30, 140, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.newPassword_lineEdit.setFont(font)
        self.newPassword_lineEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.newPassword_lineEdit.setText("")
        self.newPassword_lineEdit.setObjectName("lineEdit")
        self.newPassword_pushButton_5 = QtWidgets.QPushButton(self.newPassword_frame_2)
        self.newPassword_pushButton_5.setGeometry(QtCore.QRect(60, 210, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.newPassword_pushButton_5.setFont(font)
        self.newPassword_pushButton_5.setObjectName("pushButton_5")
        self.newPassword_lineEdit_3 = QtWidgets.QLineEdit(self.newPassword_frame_2)
        self.newPassword_lineEdit_3.setGeometry(QtCore.QRect(30, 90, 151, 20))
        self.newPassword_lineEdit_3.setObjectName("lineEdit_3")
        self.newPassword_label = QtWidgets.QLabel(self.newPassword_frame_2)
        self.newPassword_label.setGeometry(QtCore.QRect(30, 70, 47, 13))
        self.newPassword_label.setObjectName("label")
        self.newPassword_label_2 = QtWidgets.QLabel(self.newPassword_frame_2)
        self.newPassword_label_2.setGeometry(QtCore.QRect(30, 120, 47, 13))
        self.newPassword_label_2.setObjectName("label_2")
        self.newPassword_label_5 = QtWidgets.QLabel(self.newPassword_frame_2)
        self.newPassword_label_5.setGeometry(QtCore.QRect(30, 170, 47, 13))
        self.newPassword_label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.newPassword_statusbar = QtWidgets.QStatusBar(MainWindow)
        self.newPassword_statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.newPassword_statusbar)

        _translate = QtCore.QCoreApplication.translate
        self.newPassword_label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">PySword</span></p></body></html>"))
        self.newPassword_pushButton_4.setText(_translate("MainWindow", "SALVAR"))
        self.newPassword_label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">ADICIONAR CONTA</p></body></html>"))
        self.newPassword_pushButton_5.setText(_translate("MainWindow", "GERAR SENHA"))
        self.newPassword_label.setText(_translate("MainWindow", "SITE"))
        self.newPassword_label_2.setText(_translate("MainWindow", "EMAIL"))
        self.newPassword_label_5.setText(_translate("MainWindow", "SENHA"))

        #self.frames["newPassword"] = self.newPassword_frame_2
        self.registerFrame("newPassword", self.newPassword_frame_2)

    # ----------------EVENTOS----------------

    def setupEvents(self):
        # home
        self.home_pushButton_2.clicked.connect(
            lambda: self.showFrame("cadastro"))
        self.home_pushButton.clicked.connect(lambda: self.showFrame("login"))

        # cadastro
        self.cadastro_pushButton_4.clicked.connect(self.register)

        # login
        self.login_pushButton_4.clicked.connect(self.login)

        # selecionar dispositivo
        self.selectdrive_pushButton_4.clicked.connect(self.generateKey)

        # verificar chave
        self.getKey_pushButton_4.clicked.connect(self.verifyKey)

        # chave gerada
        self.keygenerated_pushButton_5.clicked.connect(
            lambda: self.showFrame("main"))

        # senhas
        self.main_pushButton_4.clicked.connect(
            lambda: self.showFrame("newPassword"))
        self.main_tableWidget.cellDoubleClicked.connect(self.copyPassword)

        # nova senha
        self.newPassword_pushButton_4.clicked.connect(self.createPassword)

        # gerar senha "aleatória"
        self.newPassword_pushButton_5.clicked.connect(
            self.createRandomPassword)

    # ----------------METODOS----------------
    def register(self):
        email = self.cadastro_lineEdit.text()
        password = self.cadastro_lineEdit_2.text()
        password_verify = self.cadastro_lineEdit_3.text()
        if password == password_verify:
            response = self.api.register(email, password)
        else:
            self.showMessageDialog("Senhas inseridas não são iguais")
            return
        if response == "Created with success":
            response = self.api.login(email, password)
            if "token" in response:
                self.api.token = response["token"]
                _translate = QtCore.QCoreApplication.translate
                self.main_label_5.setText(_translate(
                    "MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">{}</span></p></body></html>".format(email)))
                self.showMessageDialog("Usuário criado com sucesso")
                self.showFrame("selectDrive")
            else:
                self.showMessageDialogError("Erro ao cadastrar")
        elif response == "User already exists":
            self.showMessageDialogError("Usuário já existe")

    def login(self):
        email = self.login_lineEdit.text()
        password = self.login_lineEdit_2.text()
        response = self.api.login(email, password)
        if "token" in response:
            self.showMessageDialog("Logado com sucesso")
            self.api.token = response["token"]
            self.showFrame("getKey")
            _translate = QtCore.QCoreApplication.translate
            self.main_label_5.setText(_translate(
                "MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">{}</span></p></body></html>".format(email)))
        else:
            self.showMessageDialogError("Falha no login")

    def createPassword(self):
        password = self.newPassword_lineEdit_2.text()
        site = self.newPassword_lineEdit_3.text()
        email = self.newPassword_lineEdit.text()
        dataDict = {'password': password, 'site': site, 'email': email}
        serialized = pickle.dumps(dataDict)
        encrypted = Fernet(self.key).encrypt(serialized).decode('utf-8')
        response = self.api.savePassword(encrypted)
        if len(response) > 0:
            if "hash" in response[0]:
                self.showFrame("main")
                self.newPassword_lineEdit_2.setText('')
                self.newPassword_lineEdit_3.setText('')
                self.newPassword_lineEdit.setText('')

    def getPasswords(self):
        response = self.api.getPasswords()
        rows = []
        for entry in response:
            encrypted = entry['hash']
            try:
                serialized = Fernet(self.key).decrypt(encrypted.encode('utf-8'))
                data = pickle.loads(serialized)
                rows.append(data)
            except cryptography.fernet.InvalidToken:
                rows.append({"error": "Chave incorreta"})            
            
        self.passwordData = rows
        self.main_tableWidget.clearContents()
        self.main_tableWidget.setRowCount(len(rows))
        self.main_tableWidget.setColumnCount(2)
        for index, row in enumerate(rows):
            if "password" in row and "site" in row and "email" in row:
                email = row["email"]
                site = row["site"]
                site_item = QTableWidgetItem(site)
                email_item = QTableWidgetItem(email)
                site_item.setFlags(QtCore.Qt.ItemIsEnabled)
                email_item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.main_tableWidget.setItem(index, 0, site_item)
                self.main_tableWidget.setItem(index, 1, email_item)
            elif "error" in row:
                error_item = QTableWidgetItem(row["error"])
                error_item.setFlags(QtCore.Qt.ItemIsEnabled)
                empty_item = QTableWidgetItem()
                empty_item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.main_tableWidget.setItem(index, 0, error_item)
                self.main_tableWidget.setItem(index, 1, empty_item)

    def copyPassword(self, row, column):
        if "password" in self.passwordData[row]:
            self.stopClipBoardClear = True
            self.queueClearClipboard()
            pyperclip.copy(self.passwordData[row]['password'])
            self.showMessageDialog("Senha copiada para a área de transferência")

    def queueClearClipboard(self):
        t = Timer(30, self.fillClipboard)
        t.start()

    def fillClipboard(self, counter=0):
        if counter == 0:
            self.stopClipBoardClear = False
        if (counter < 50 and not self.stopClipBoardClear):
            pyperclip.copy(str(counter))
            t = Timer(0.25, lambda: self.fillClipboard(counter+1))
            t.start()

    def updateDriveList(self):
        self.drives = psutil.disk_partitions()
        self.selectdrive_listWidget.clear()
        for drive in sorted(self.drives, key=lambda d: d.device):
            item = QListWidgetItem(drive.device)
            self.selectdrive_listWidget.addItem(item)

    def generateKey(self):
        selected = self.selectdrive_listWidget.selectedItems()
        if len(selected) > 0:
            driveName = selected[0].text()
            drive = next(d for d in self.drives if d.device == driveName)
            key = Fernet.generate_key()
            path = os.path.join(drive.mountpoint, 'pysword_secret')

            # arquivo oculto
            prefix = '.' if os.name != 'nt' else ''
            path = prefix + path

            if not os.path.exists(path):
                try:
                    with open(path, 'w+') as file:
                        file.write(key.decode('utf-8'))

                    if os.name == 'nt':
                        ret = ctypes.windll.kernel32.SetFileAttributesW(
                            path, 0x02)
                        if not ret:
                            raise ctypes.WinError()
                    self.key = key
                    self.showFrame("keyGenerated")
                except Exception as e:
                    self.showMessageDialogError("Erro ao gravar chave no dispositivo")
            else:
                self.showMessageDialogError(
                    "Já existe uma chave salva no dispositivo")

    def verifyKey(self):
        drives = psutil.disk_partitions()
        for drive in drives:
            pathOptions = ['pysword_secret', '.pysowrd_secret']
            for path in pathOptions:
                fullPath = os.path.join(drive.mountpoint, path)
                if os.path.exists(fullPath):
                    with open(fullPath, 'r') as file:
                        key = file.read().encode('utf-8')
                        try:
                            f = Fernet(key)
                            self.key = key
                            self.showFrame("main")
                            return
                        except Exception as e:
                            self.showMessageDialogError("Chave inválida")
                            return
        if self.key is None:
            self.showMessageDialog("Nenhuma chave encontrada")

    def showMessageDialog(self, message):
        msg = QtWidgets.QMessageBox()
        msg.setText(message)
        msg.setWindowTitle("PySword")
        msg.exec_()

    def showMessageDialogError(self, message):
        msg = QtWidgets.QMessageBox()
        msg.setText(message)
        msg.setWindowTitle("ERRO")
        msg.exec_()

    def createRandomPassword(self):
        str1 = ''.join((random.choice(string.ascii_letters) for x in range(4)))
        str1 += ''.join((random.choice(string.digits) for x in range(4)))

        sam_list = list(str1)
        random.shuffle(sam_list)
        final_string = ''.join(sam_list)

        self.newPassword_lineEdit_2.setText(final_string)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUI(MainWindow)
    ui.setupEvents()
    MainWindow.show()
    sys.exit(app.exec_())
