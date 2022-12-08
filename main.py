from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QListWidgetItem
import requests
import psutil
from cryptography.fernet import Fernet
import os
import ctypes

class Api():
    def __init__(self, baseUrl):
        self.baseUrl = baseUrl
        self.token = ""

    def register(self, email, password):
        url = self.baseUrl + '/auth/register'
        data = {'email': email, 'password': password}
        response = requests.post(url, json=data)
        return response.json()
    
    def login(self, email, password):
        url = self.baseUrl + '/auth/login'
        data = {'email': email, 'password': password}
        response = requests.post(url, json=data)
        return response.json()

class Ui_MainWindow(object):
    def __init__(self):
        self.api = Api("http://pysword.onrender.com")

    def showFrame(self, frameName):
        for name, frame in self.frames.items():
            if name == frameName:
                frame.show()
            else:
                frame.hide()

    #----------------UI----------------

    def setupUI(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(226, 298)
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

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.showFrame("home")
        self.updateDriveList()

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
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.home_pushButton_2.setText(_translate("MainWindow", "CADASTRAR"))
        self.home_label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">PySword</span></p></body></html>"))
        self.home_pushButton.setText(_translate("MainWindow", "ENTRAR"))
        self.home_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">BEM VINDO</p></body></html>"))

        self.frames["home"] = self.home_frame
    
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
        self.login_label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">PySword</span></p></body></html>"))
        self.login_pushButton_4.setText(_translate("MainWindow", "ENTRAR"))
        self.login_label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">LOGIN</p></body></html>"))
        self.login_lineEdit.setText(_translate("MainWindow", "USUÁRIO"))
        self.login_lineEdit_2.setText(_translate("MainWindow", "SENHA"))

        self.frames["login"] = self.login_frame
    
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
        self.cadastro_pushButton_4 = QtWidgets.QPushButton(self.cadastro_frame_2)
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

        self.cadastro_label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">PySword</span></p></body></html>"))
        self.cadastro_pushButton_4.setText(_translate("MainWindow", "CADASTRAR"))
        self.cadastro_label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">CADASTRO</p></body></html>"))
        self.cadastro_lineEdit_2.setText(_translate("MainWindow", "SENHA"))
        self.cadastro_lineEdit.setText(_translate("MainWindow", "USUÁRIO"))
        self.cadastro_lineEdit_3.setText(_translate("MainWindow", "REPETIR SENHA"))

        self.frames["cadastro"] = self.cadastro_frame_2
    
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
        self.selectdrive_pushButton_4 = QtWidgets.QPushButton(self.selectdrive_frame_2)
        self.selectdrive_pushButton_4.setGeometry(QtCore.QRect(30, 230, 151, 31))
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
        self.selectdrive_listWidget = QtWidgets.QListWidget(self.selectdrive_frame_2)
        self.selectdrive_listWidget.setGeometry(QtCore.QRect(10, 70, 181, 151))
        self.selectdrive_listWidget.setObjectName("listWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.selectdrive_statusbar = QtWidgets.QStatusBar(MainWindow)
        self.selectdrive_statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.selectdrive_statusbar)

        _translate = QtCore.QCoreApplication.translate
        self.selectdrive_label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">PySword</span></p></body></html>"))
        self.selectdrive_pushButton_4.setText(_translate("MainWindow", "CRIAR CHAVE"))
        self.selectdrive_label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">CADASTRO</p></body></html>"))

        self.frames["selectDrive"] = self.selectdrive_frame_2

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
        self.keygenerated_pushButton_5 = QtWidgets.QPushButton(self.keygenerated_frame_3)
        self.keygenerated_pushButton_5.setGeometry(QtCore.QRect(30, 230, 151, 31))
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
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.keygenerated_label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">PySword</span></p></body></html>"))
        self.keygenerated_pushButton_5.setText(_translate("MainWindow", "ENTRAR"))
        self.keygenerated_label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">CADASTRO</p></body></html>"))
        self.keygenerated_label.setPixmap(QPixmap(os.path.join(os.path.dirname(__file__), 'assets/check.png')))
        self.keygenerated_label_2.setText(_translate("MainWindow", "CHAVE CRIADA COM SUCESSO"))

        self.frames["keyGenerated"] = self.keygenerated_frame_3
    
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
        self.getKey_statusbar = QtWidgets.QStatusBar(MainWindow)
        self.getKey_statusbar.setObjectName("statusbar")

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.getKey_label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">PySword</span></p></body></html>"))
        self.getKey_pushButton_4.setText(_translate("MainWindow", "VERIFICAR CHAVE"))
        self.getKey_label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">LOGIN</p></body></html>"))
        self.getKey_label.setPixmap(QPixmap(os.path.join(os.path.dirname(__file__), 'assets/pendrive.png')))

        self.frames["getKey"] = self.getKey_frame_2

    #----------------EVENTOS----------------

    def setupEvents(self):
        self.setupHomeEvents()
        self.setupRegisterEvents()
        self.setupLoginEvents()
        self.setupDriveSelectEvents()
        self.setupVerifyKeyEvents()

    def setupHomeEvents(self):
        self.home_pushButton_2.clicked.connect(lambda: self.showFrame("cadastro"))
        self.home_pushButton.clicked.connect(lambda: self.showFrame("login"))
    
    def setupRegisterEvents(self):
        self.cadastro_pushButton_4.clicked.connect(self.register)
    
    def setupLoginEvents(self):
        self.login_pushButton_4.clicked.connect(self.login)
    
    def setupDriveSelectEvents(self):
        self.selectdrive_pushButton_4.clicked.connect(self.generateKey)

    def setupVerifyKeyEvents(self):
        self.getKey_pushButton_4.clicked.connect(self.verifyKey)

    #----------------METODOS----------------
    def register(self):
        email = self.cadastro_lineEdit.text()
        password = self.cadastro_lineEdit_2.text()
        password_verify = self.cadastro_lineEdit_3.text()
        response = self.api.register(email, password)
        print(response)
        if response == "Created with success":
            self.showFrame("selectDrive")
    
    def login(self):
        email = self.login_lineEdit.text()
        password = self.login_lineEdit_2.text()
        response = self.api.login(email, password)
        print(response)
        if "token" in response:
            self.api.token = response["token"]
            self.showFrame("getKey")
    
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

            #arquivo oculto
            prefix = '.' if os.name != 'nt' else ''
            path = prefix + path

            if not os.path.exists(path):
                try:
                    with open(path, 'w+') as file:
                        file.write(key.decode('utf-8'))

                    if os.name == 'nt':
                        ret = ctypes.windll.kernel32.SetFileAttributesW(path, 0x02)
                        if not ret:
                            raise ctypes.WinError()
                        self.showFrame("keyGenerated")
                except Exception as e:
                    print("Erro ao gravar chave no dispositivo: ", e)
            else:
                print("Já existe uma chave salva no dispositivo")
    
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
                        except:
                            print("Chave inválida")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUI(MainWindow)
    ui.setupEvents()
    MainWindow.show()
    sys.exit(app.exec_())
