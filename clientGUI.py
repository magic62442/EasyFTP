# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'client.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import re
import sys

from PyQt5.QtGui import QIntValidator

import clientUtil
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QLineEdit


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(501, 651)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("文件夹.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolTip("")
        MainWindow.setAutoFillBackground(False)
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 61, 16))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.IPlineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.IPlineEdit.setGeometry(QtCore.QRect(70, 10, 125, 21))
        self.IPlineEdit.setObjectName("IPlineEdit")
        #self.IPlineEdit.setInputMask('000.000.000.000;_')
        self.portlineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.portlineEdit.setGeometry(QtCore.QRect(264, 10, 87, 21))
        self.portlineEdit.setObjectName("portlineEdit")
        pIntvalidator = QIntValidator(self.portlineEdit)
        self.portlineEdit.setValidator(pIntvalidator)
        self.connectButton = QtWidgets.QPushButton(self.centralwidget)
        self.connectButton.setGeometry(QtCore.QRect(360, 10, 61, 21))
        self.connectButton.setObjectName("connectButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(204, 10, 51, 16))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 40, 61, 16))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(204, 40, 41, 16))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.loginButton = QtWidgets.QPushButton(self.centralwidget)
        self.loginButton.setGeometry(QtCore.QRect(360, 40, 61, 21))
        self.loginButton.setObjectName("loginButton")
        self.usernamelineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.usernamelineEdit.setGeometry(QtCore.QRect(70, 40, 125, 21))
        self.usernamelineEdit.setObjectName("usernamelineEdit")
        self.passwordlineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordlineEdit.setGeometry(QtCore.QRect(255, 40, 97, 21))
        self.passwordlineEdit.setObjectName("passwordlineEdit")
        self.passwordlineEdit.setEchoMode(QLineEdit.Password)
        self.disconnectButton = QtWidgets.QPushButton(self.centralwidget)
        self.disconnectButton.setGeometry(QtCore.QRect(430, 10, 51, 51))
        self.disconnectButton.setObjectName("disconnectButton")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 150, 81, 16))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 80, 81, 16))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.cmdlineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.cmdlineEdit.setGeometry(QtCore.QRect(10, 100, 411, 31))
        self.cmdlineEdit.setObjectName("cmdlineEdit")
        self.sendButton = QtWidgets.QPushButton(self.centralwidget)
        self.sendButton.setGeometry(QtCore.QRect(430, 100, 51, 31))
        self.sendButton.setObjectName("sendButton")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 170, 471, 101))
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 280, 81, 16))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.localtableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.localtableWidget.setGeometry(QtCore.QRect(10, 300, 471, 121))
        self.localtableWidget.setAutoFillBackground(False)
        self.localtableWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.localtableWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.localtableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.localtableWidget.setShowGrid(False)
        self.localtableWidget.setRowCount(20)
        self.localtableWidget.setColumnCount(3)
        self.localtableWidget.setObjectName("localtableWidget")
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        item.setFont(font)
        item.setBackground(QtGui.QColor(153, 199, 213))
        self.localtableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(153, 199, 213))
        self.localtableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(153, 199, 213))
        self.localtableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.localtableWidget.setItem(1, 1, item)
        self.localtableWidget.horizontalHeader().setVisible(True)
        self.localtableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.localtableWidget.horizontalHeader().setDefaultSectionSize(140)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 430, 81, 16))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.remotetableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.remotetableWidget.setGeometry(QtCore.QRect(10, 450, 471, 121))
        self.remotetableWidget.setAutoFillBackground(False)
        self.remotetableWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.remotetableWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.remotetableWidget.setShowGrid(False)
        self.remotetableWidget.setRowCount(20)
        self.remotetableWidget.setColumnCount(3)
        self.remotetableWidget.setObjectName("remotetableWidget")
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        item.setFont(font)
        item.setBackground(QtGui.QColor(153, 199, 213))
        self.remotetableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(153, 199, 213))
        self.remotetableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(153, 199, 213))
        self.remotetableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.remotetableWidget.setItem(1, 1, item)
        self.remotetableWidget.horizontalHeader().setVisible(True)
        self.remotetableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.remotetableWidget.horizontalHeader().setDefaultSectionSize(140)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(120, 590, 311, 16))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 590, 111, 16))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.pauseButton = QtWidgets.QPushButton(self.centralwidget)
        self.pauseButton.setGeometry(QtCore.QRect(430, 580, 51, 31))
        self.pauseButton.setObjectName("pauseButton")
        self.dirButton = QtWidgets.QPushButton(self.centralwidget)
        self.dirButton.setGeometry(QtCore.QRect(450, 280, 31, 21))
        self.dirButton.setObjectName("dirButton")
        self.refreshButton = QtWidgets.QPushButton(self.centralwidget)
        self.refreshButton.setGeometry(QtCore.QRect(460, 430, 21, 21))
        self.refreshButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("刷新.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.refreshButton.setIcon(icon1)
        self.refreshButton.setObjectName("refreshButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.isConnect = False
        self.set_signal_slot()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FTPClient"))
        self.label.setText(_translate("MainWindow", "IP 地址:"))
        self.connectButton.setText(_translate("MainWindow", "连接"))
        self.label_2.setText(_translate("MainWindow", "端口号："))
        self.label_3.setText(_translate("MainWindow", "用户名："))
        self.label_4.setText(_translate("MainWindow", "密码："))
        self.loginButton.setText(_translate("MainWindow", "登录"))
        self.disconnectButton.setText(_translate("MainWindow", "断开"))
        self.label_5.setText(_translate("MainWindow", "信息显示："))
        self.label_6.setText(_translate("MainWindow", "命令输入："))
        self.sendButton.setText(_translate("MainWindow", "发送"))
        self.label_7.setText(_translate("MainWindow", "本地文件："))
        item = self.localtableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.localtableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Type"))
        item = self.localtableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Size"))
        __sortingEnabled = self.localtableWidget.isSortingEnabled()
        self.localtableWidget.setSortingEnabled(False)
        self.localtableWidget.setSortingEnabled(__sortingEnabled)
        self.label_8.setText(_translate("MainWindow", "远程文件："))
        item = self.remotetableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.remotetableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Type"))
        item = self.remotetableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Size"))
        __sortingEnabled = self.remotetableWidget.isSortingEnabled()
        self.remotetableWidget.setSortingEnabled(False)
        self.remotetableWidget.setSortingEnabled(__sortingEnabled)
        self.label_9.setText(_translate("MainWindow", "当前任务进度"))
        self.pauseButton.setText(_translate("MainWindow", "暂停"))
        self.dirButton.setText(_translate("MainWindow", "..."))

    def set_signal_slot(self):
        self.connectButton.clicked.connect(self.establish_connect)
        self.loginButton.clicked.connect(self.user_login)
        self.sendButton.clicked.connect(self.send_cmd)

    def establish_connect(self):
        '''
        1.get IP and PORT
        2.because of the IPlineEdit mask, IP's legality is guaranteed
        3.new a FTP, establish the connect
        '''
        IPaddr = self.IPlineEdit.text()
        ip_pattern = r'(\d{1,3}).(\d{1,3}).(\d{1,3}).(\d{1,3})'
        if not re.match(ip_pattern, IPaddr):
            QtWidgets.QMessageBox.information(self.connectButton, 'Warning', 'Illegal IPaddr', QMessageBox.Ok)
            return

        port = self.portlineEdit.text()
        if len(port) < 1 or len(port) > 5:
            QtWidgets.QMessageBox.information(self.connectButton, 'Warning', 'Illegal PORT', QMessageBox.Ok)
            return
        port = int(port)
        if port > 65535:
            QtWidgets.QMessageBox.information(self.connectButton, 'Warning', 'Illegal PORT', QMessageBox.Ok)
            return
        msg = "正在连接：" + IPaddr
        self.textEdit.append(msg)
        self.ftp = clientUtil.FTP()
        self.ftp.response_sig.connect(self.get_response)
        self.ftp.error_sig.connect(self.error_response)
        self.ftp.connect_establish(IPaddr, port)
        self.isConnect = True

    def user_login(self):
        if not self.isConnect:
            QtWidgets.QMessageBox.information(self.connectButton, 'Warning', 'Connect server first', QMessageBox.Ok)
            return
        username = self.usernamelineEdit.text()
        password = self.passwordlineEdit.text()
        newCmdUser = "USER " + username
        self.ftp.send_cmd(newCmdUser)
        newCmdPass = "PASS " + password
        self.ftp.send_cmd(newCmdPass)

    def send_cmd(self):
        cmd = self.cmdlineEdit.text()
        self.ftp.send_cmd(cmd)
        pass


    def get_response(self, response):
        msg = "响应：" + response
        self.textEdit.append(msg)

    def error_response(self, error):
        msg = "Error：" + error
        self.textEdit.append(msg)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())