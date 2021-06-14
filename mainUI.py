# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CipherSystem(object):
    def setupUi(self, CipherSystem):
        CipherSystem.setObjectName("CipherSystem")
        CipherSystem.resize(1155, 899)
        self.centralwidget = QtWidgets.QWidget(CipherSystem)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 1131, 351))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.inputPlainTextEdit = QtWidgets.QPlainTextEdit(self.layoutWidget)
        self.inputPlainTextEdit.setObjectName("inputPlainTextEdit")
        self.verticalLayout.addWidget(self.inputPlainTextEdit)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 530, 1131, 301))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.outputText = QtWidgets.QTextEdit(self.layoutWidget1)
        self.outputText.setReadOnly(True)
        self.outputText.setObjectName("outputText")
        self.verticalLayout_2.addWidget(self.outputText)
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 480, 771, 30))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.inputKey = QtWidgets.QLineEdit(self.layoutWidget2)
        self.inputKey.setObjectName("inputKey")
        self.horizontalLayout.addWidget(self.inputKey)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.inputKey2 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.inputKey2.setObjectName("inputKey2")
        self.horizontalLayout.addWidget(self.inputKey2)
        self.layoutWidget3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget3.setGeometry(QtCore.QRect(10, 380, 491, 30))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.lineEditFile = QtWidgets.QLineEdit(self.layoutWidget3)
        self.lineEditFile.setEnabled(True)
        self.lineEditFile.setReadOnly(True)
        self.lineEditFile.setObjectName("lineEditFile")
        self.horizontalLayout_2.addWidget(self.lineEditFile)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.inputFileButton = QtWidgets.QPushButton(self.layoutWidget3)
        self.inputFileButton.setEnabled(False)
        self.inputFileButton.setObjectName("inputFileButton")
        self.horizontalLayout_2.addWidget(self.inputFileButton)
        self.layoutWidget4 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget4.setGeometry(QtCore.QRect(10, 430, 491, 30))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget4)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.lineEditOutFile = QtWidgets.QLineEdit(self.layoutWidget4)
        self.lineEditOutFile.setReadOnly(True)
        self.lineEditOutFile.setObjectName("lineEditOutFile")
        self.horizontalLayout_3.addWidget(self.lineEditOutFile)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.outputFileButton = QtWidgets.QPushButton(self.layoutWidget4)
        self.outputFileButton.setEnabled(False)
        self.outputFileButton.setObjectName("outputFileButton")
        self.horizontalLayout_3.addWidget(self.outputFileButton)
        self.layoutWidget5 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget5.setGeometry(QtCore.QRect(580, 430, 123, 21))
        self.layoutWidget5.setObjectName("layoutWidget5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget5)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.encryptButton = QtWidgets.QRadioButton(self.layoutWidget5)
        self.encryptButton.setChecked(True)
        self.encryptButton.setObjectName("encryptButton")
        self.horizontalLayout_4.addWidget(self.encryptButton)
        self.decryptButton = QtWidgets.QRadioButton(self.layoutWidget5)
        self.decryptButton.setChecked(False)
        self.decryptButton.setObjectName("decryptButton")
        self.horizontalLayout_4.addWidget(self.decryptButton)
        self.layoutWidget6 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget6.setGeometry(QtCore.QRect(580, 390, 123, 21))
        self.layoutWidget6.setObjectName("layoutWidget6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget6)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.textModeButton = QtWidgets.QRadioButton(self.layoutWidget6)
        self.textModeButton.setChecked(True)
        self.textModeButton.setObjectName("textModeButton")
        self.horizontalLayout_5.addWidget(self.textModeButton)
        self.fileModeButton = QtWidgets.QRadioButton(self.layoutWidget6)
        self.fileModeButton.setObjectName("fileModeButton")
        self.horizontalLayout_5.addWidget(self.fileModeButton)
        self.layoutWidget7 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget7.setGeometry(QtCore.QRect(820, 380, 291, 141))
        self.layoutWidget7.setObjectName("layoutWidget7")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget7)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.replaceOutToInput = QtWidgets.QPushButton(self.layoutWidget7)
        self.replaceOutToInput.setObjectName("replaceOutToInput")
        self.gridLayout.addWidget(self.replaceOutToInput, 0, 1, 1, 1)
        self.saveOutputButton = QtWidgets.QPushButton(self.layoutWidget7)
        self.saveOutputButton.setObjectName("saveOutputButton")
        self.gridLayout.addWidget(self.saveOutputButton, 1, 1, 1, 1)
        self.resetText = QtWidgets.QPushButton(self.layoutWidget7)
        self.resetText.setObjectName("resetText")
        self.gridLayout.addWidget(self.resetText, 1, 0, 1, 1)
        self.rsaKeyGen = QtWidgets.QPushButton(self.layoutWidget7)
        self.rsaKeyGen.setObjectName("rsaKeyGen")
        self.gridLayout.addWidget(self.rsaKeyGen, 0, 0, 1, 1)
        self.dhModeButton = QtWidgets.QPushButton(self.layoutWidget7)
        self.dhModeButton.setObjectName("dhModeButton")
        self.gridLayout.addWidget(self.dhModeButton, 2, 0, 1, 1)
        CipherSystem.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CipherSystem)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1155, 26))
        self.menubar.setObjectName("menubar")
        self.Monoalphabetic = QtWidgets.QMenu(self.menubar)
        self.Monoalphabetic.setObjectName("Monoalphabetic")
        self.Polyalphabetic = QtWidgets.QMenu(self.menubar)
        self.Polyalphabetic.setObjectName("Polyalphabetic")
        self.Polygraphic = QtWidgets.QMenu(self.menubar)
        self.Polygraphic.setObjectName("Polygraphic")
        self.Transposition = QtWidgets.QMenu(self.menubar)
        self.Transposition.setObjectName("Transposition")
        self.Stream = QtWidgets.QMenu(self.menubar)
        self.Stream.setObjectName("Stream")
        self.Block = QtWidgets.QMenu(self.menubar)
        self.Block.setObjectName("Block")
        self.PublicKey = QtWidgets.QMenu(self.menubar)
        self.PublicKey.setObjectName("PublicKey")
        CipherSystem.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CipherSystem)
        self.statusbar.setObjectName("statusbar")
        CipherSystem.setStatusBar(self.statusbar)
        self.actionCaesar = QtWidgets.QAction(CipherSystem)
        self.actionCaesar.setEnabled(True)
        self.actionCaesar.setIconVisibleInMenu(True)
        self.actionCaesar.setShortcutVisibleInContextMenu(False)
        self.actionCaesar.setObjectName("actionCaesar")
        self.actionCaesarDecrypt = QtWidgets.QAction(CipherSystem)
        self.actionCaesarDecrypt.setObjectName("actionCaesarDecrypt")
        self.actionKeyword = QtWidgets.QAction(CipherSystem)
        self.actionKeyword.setObjectName("actionKeyword")
        self.actionKeywordDecrypt = QtWidgets.QAction(CipherSystem)
        self.actionKeywordDecrypt.setObjectName("actionKeywordDecrypt")
        self.actionVigenere = QtWidgets.QAction(CipherSystem)
        self.actionVigenere.setObjectName("actionVigenere")
        self.actionVigenereDecrypt = QtWidgets.QAction(CipherSystem)
        self.actionVigenereDecrypt.setObjectName("actionVigenereDecrypt")
        self.actionAutokeyCiphertext = QtWidgets.QAction(CipherSystem)
        self.actionAutokeyCiphertext.setObjectName("actionAutokeyCiphertext")
        self.actionPlayfair = QtWidgets.QAction(CipherSystem)
        self.actionPlayfair.setObjectName("actionPlayfair")
        self.actionPermutation = QtWidgets.QAction(CipherSystem)
        self.actionPermutation.setObjectName("actionPermutation")
        self.actionPermutationDecrypt = QtWidgets.QAction(CipherSystem)
        self.actionPermutationDecrypt.setObjectName("actionPermutationDecrypt")
        self.actionCPermutation = QtWidgets.QAction(CipherSystem)
        self.actionCPermutation.setObjectName("actionCPermutation")
        self.actionRC4 = QtWidgets.QAction(CipherSystem)
        self.actionRC4.setObjectName("actionRC4")
        self.actionRC4Decrypt = QtWidgets.QAction(CipherSystem)
        self.actionRC4Decrypt.setObjectName("actionRC4Decrypt")
        self.actionDES = QtWidgets.QAction(CipherSystem)
        self.actionDES.setObjectName("actionDES")
        self.actionDESDecrypt = QtWidgets.QAction(CipherSystem)
        self.actionDESDecrypt.setObjectName("actionDESDecrypt")
        self.actionRSA = QtWidgets.QAction(CipherSystem)
        self.actionRSA.setObjectName("actionRSA")
        self.actionAffine = QtWidgets.QAction(CipherSystem)
        self.actionAffine.setObjectName("actionAffine")
        self.actionAffineDecrypt = QtWidgets.QAction(CipherSystem)
        self.actionAffineDecrypt.setObjectName("actionAffineDecrypt")
        self.actionMultiliteral = QtWidgets.QAction(CipherSystem)
        self.actionMultiliteral.setObjectName("actionMultiliteral")
        self.actionMultiliteralDecrypt = QtWidgets.QAction(CipherSystem)
        self.actionMultiliteralDecrypt.setObjectName("actionMultiliteralDecrypt")
        self.actionPlayfairDecrypt = QtWidgets.QAction(CipherSystem)
        self.actionPlayfairDecrypt.setObjectName("actionPlayfairDecrypt")
        self.actionAutokeyCiphertextDecrypt = QtWidgets.QAction(CipherSystem)
        self.actionAutokeyCiphertextDecrypt.setObjectName("actionAutokeyCiphertextDecrypt")
        self.actionAutokeyPlaintext = QtWidgets.QAction(CipherSystem)
        self.actionAutokeyPlaintext.setObjectName("actionAutokeyPlaintext")
        self.actionCPermutationDecrypt = QtWidgets.QAction(CipherSystem)
        self.actionCPermutationDecrypt.setObjectName("actionCPermutationDecrypt")
        self.actionDoubleTransposition = QtWidgets.QAction(CipherSystem)
        self.actionDoubleTransposition.setObjectName("actionDoubleTransposition")
        self.actionDoubleTranspositionDecrypt = QtWidgets.QAction(CipherSystem)
        self.actionDoubleTranspositionDecrypt.setObjectName("actionDoubleTranspositionDecrypt")
        self.actionCA = QtWidgets.QAction(CipherSystem)
        self.actionCA.setObjectName("actionCA")
        self.actionCADecrypt = QtWidgets.QAction(CipherSystem)
        self.actionCADecrypt.setObjectName("actionCADecrypt")
        self.actionAES = QtWidgets.QAction(CipherSystem)
        self.actionAES.setObjectName("actionAES")
        self.actionAESDecrypt = QtWidgets.QAction(CipherSystem)
        self.actionAESDecrypt.setObjectName("actionAESDecrypt")
        self.actionRSADecrypt = QtWidgets.QAction(CipherSystem)
        self.actionRSADecrypt.setObjectName("actionRSADecrypt")
        self.actionAutokeyPlaintextDecrypt = QtWidgets.QAction(CipherSystem)
        self.actionAutokeyPlaintextDecrypt.setObjectName("actionAutokeyPlaintextDecrypt")
        self.actionDH_Mode = QtWidgets.QAction(CipherSystem)
        self.actionDH_Mode.setObjectName("actionDH_Mode")
        self.Monoalphabetic.addAction(self.actionCaesar)
        self.Monoalphabetic.addAction(self.actionKeyword)
        self.Monoalphabetic.addAction(self.actionAffine)
        self.Monoalphabetic.addAction(self.actionMultiliteral)
        self.Polyalphabetic.addAction(self.actionVigenere)
        self.Polyalphabetic.addAction(self.actionAutokeyCiphertext)
        self.Polyalphabetic.addAction(self.actionAutokeyPlaintext)
        self.Polygraphic.addAction(self.actionPlayfair)
        self.Transposition.addAction(self.actionPermutation)
        self.Transposition.addAction(self.actionCPermutation)
        self.Transposition.addAction(self.actionDoubleTransposition)
        self.Stream.addAction(self.actionRC4)
        self.Stream.addAction(self.actionCA)
        self.Block.addAction(self.actionDES)
        self.Block.addAction(self.actionAES)
        self.PublicKey.addAction(self.actionRSA)
        self.menubar.addAction(self.Monoalphabetic.menuAction())
        self.menubar.addAction(self.Polyalphabetic.menuAction())
        self.menubar.addAction(self.Polygraphic.menuAction())
        self.menubar.addAction(self.Transposition.menuAction())
        self.menubar.addAction(self.Stream.menuAction())
        self.menubar.addAction(self.Block.menuAction())
        self.menubar.addAction(self.PublicKey.menuAction())

        self.retranslateUi(CipherSystem)
        QtCore.QMetaObject.connectSlotsByName(CipherSystem)

    def retranslateUi(self, CipherSystem):
        _translate = QtCore.QCoreApplication.translate
        CipherSystem.setWindowTitle(_translate("CipherSystem", "密码学加解密软件"))
        self.label.setText(_translate("CipherSystem", "文本（明文或密文）"))
        self.label_4.setText(_translate("CipherSystem", "文本（密文或明文）"))
        self.outputText.setHtml(_translate("CipherSystem", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">文件加解密暂时仅支持单表替代、多表替代密码和多图替代密码，且仅支持Text files(*.txt)文件</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">playfair加密中，将会把‘j’替换成‘i’</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">在置换密码中，对于一些位数不齐的明文，将会在明文末尾附加‘X’</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">permutation加解密中，key以空格隔开输入，例：3 4 1 5 2</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">密钥2是在key需要两个参数的时候使用，例如：Affine中(a,b)；RSA中(p,q)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">流密码支持中文字符加解密</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">因为流密码和分块密码生成的密文有不可见字符，所以流密码的密文以base64形式，分块密码以16进制形式表现</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">RSA密钥生成默认生成1024位大素数</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">RSA中e的默认值为65537，暂不支持修改</p></body></html>"))
        self.label_2.setText(_translate("CipherSystem", "密钥："))
        self.label_6.setText(_translate("CipherSystem", "密钥2："))
        self.label_3.setText(_translate("CipherSystem", "输入文件："))
        self.inputFileButton.setText(_translate("CipherSystem", "选择文件"))
        self.label_5.setText(_translate("CipherSystem", "输出文件："))
        self.outputFileButton.setText(_translate("CipherSystem", "选择文件"))
        self.encryptButton.setText(_translate("CipherSystem", "加密"))
        self.decryptButton.setText(_translate("CipherSystem", "解密"))
        self.textModeButton.setText(_translate("CipherSystem", "文本"))
        self.fileModeButton.setText(_translate("CipherSystem", "文件"))
        self.replaceOutToInput.setText(_translate("CipherSystem", "复制输出到输入"))
        self.saveOutputButton.setText(_translate("CipherSystem", "将输出保存至文件"))
        self.resetText.setText(_translate("CipherSystem", "清空"))
        self.rsaKeyGen.setText(_translate("CipherSystem", "RSA密钥生成"))
        self.dhModeButton.setText(_translate("CipherSystem", "DH算法演示"))
        self.Monoalphabetic.setTitle(_translate("CipherSystem", "单表替代密码"))
        self.Polyalphabetic.setTitle(_translate("CipherSystem", " 多表替代密码"))
        self.Polygraphic.setTitle(_translate("CipherSystem", " 多图替代密码"))
        self.Transposition.setTitle(_translate("CipherSystem", " 置换密码"))
        self.Stream.setTitle(_translate("CipherSystem", "流密码"))
        self.Block.setTitle(_translate("CipherSystem", "分块密码"))
        self.PublicKey.setTitle(_translate("CipherSystem", "公钥密码"))
        self.actionCaesar.setText(_translate("CipherSystem", "Caesar Cipher"))
        self.actionCaesarDecrypt.setText(_translate("CipherSystem", "Caesar Cipher Decrypt"))
        self.actionKeyword.setText(_translate("CipherSystem", "Keyword Cipher"))
        self.actionKeywordDecrypt.setText(_translate("CipherSystem", "Keyword Cipher Decrypt"))
        self.actionVigenere.setText(_translate("CipherSystem", "Vigenere Cipher"))
        self.actionVigenereDecrypt.setText(_translate("CipherSystem", "Vigenere Cipher Decrypt"))
        self.actionAutokeyCiphertext.setText(_translate("CipherSystem", "Autokey Ciphertext"))
        self.actionPlayfair.setText(_translate("CipherSystem", "Playfair Cipher"))
        self.actionPermutation.setText(_translate("CipherSystem", "Permutation Cipher"))
        self.actionPermutationDecrypt.setText(_translate("CipherSystem", "Permutation Cipher Decrypt"))
        self.actionCPermutation.setText(_translate("CipherSystem", "Column permutation Cipher"))
        self.actionRC4.setText(_translate("CipherSystem", "RC4"))
        self.actionRC4Decrypt.setText(_translate("CipherSystem", "RC4 Decrypt"))
        self.actionDES.setText(_translate("CipherSystem", "DES"))
        self.actionDESDecrypt.setText(_translate("CipherSystem", "DES Decrypt"))
        self.actionRSA.setText(_translate("CipherSystem", "RSA"))
        self.actionAffine.setText(_translate("CipherSystem", "Affine Cipher"))
        self.actionAffineDecrypt.setText(_translate("CipherSystem", "Affine Cipher Decrypt"))
        self.actionMultiliteral.setText(_translate("CipherSystem", "Multiliteral Cipher"))
        self.actionMultiliteralDecrypt.setText(_translate("CipherSystem", "Multiliteral Cipher Decrypt"))
        self.actionPlayfairDecrypt.setText(_translate("CipherSystem", "Playfair Cipher Decrypt"))
        self.actionAutokeyCiphertextDecrypt.setText(_translate("CipherSystem", "Autokey Ciphertext Decrypt"))
        self.actionAutokeyPlaintext.setText(_translate("CipherSystem", "Autokey Plaintext"))
        self.actionCPermutationDecrypt.setText(_translate("CipherSystem", "Column permutation Cipher Decrypt"))
        self.actionDoubleTransposition.setText(_translate("CipherSystem", "Double-Transposition Cipher"))
        self.actionDoubleTranspositionDecrypt.setText(_translate("CipherSystem", "Double-Transposition Cipher Decrypt"))
        self.actionCA.setText(_translate("CipherSystem", "CA"))
        self.actionCADecrypt.setText(_translate("CipherSystem", "CA Decrypt"))
        self.actionAES.setText(_translate("CipherSystem", "AES"))
        self.actionAESDecrypt.setText(_translate("CipherSystem", "AES Decrypt"))
        self.actionRSADecrypt.setText(_translate("CipherSystem", "RSA Decrypt"))
        self.actionAutokeyPlaintextDecrypt.setText(_translate("CipherSystem", "Autokey Plaintext Decrypt"))
        self.actionDH_Mode.setText(_translate("CipherSystem", "DH Mode"))
