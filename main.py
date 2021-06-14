# -*- coding: UTF-8 -*-
# @File: main.py
# @Author: SCERush
# @Contact: 1037920609@qq.com
# @Datetime: 20/7/1 13:40
# @Software: PyCharm
"""
文件说明：系统主程序
"""

import sys

from mainUI import *
from DiffieHellmanMode import *

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import tools
import caesar
import keywordCipher as kw
import affine
import multiliteral
import vigenere
import autokey
import playfair
import permutation
import columnPermutation
import doubleTransposition
import rc4
import myDes
import myRsa
from RabinMiller import isPrime, generateLargePrime


class MainWindow(QMainWindow, Ui_CipherSystem):
    # def __init__(self, parent=None):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        # super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        self.setWindowIcon(QIcon('1207136.icon'))
        self.initUI()

    #   '''    =================================   功   能   初   始   化   =================================    '''
    def initUI(self):
        # 单表替代密码
        self.actionCaesar.triggered.connect(self.caesarCipher)
        self.actionKeyword.triggered.connect(self.keywordCipher)
        self.actionAffine.triggered.connect(self.affineCipher)
        self.actionMultiliteral.triggered.connect(self.multilieralCipher)

        # 多表替代密码
        self.actionVigenere.triggered.connect(self.vigenereCipher)
        self.actionAutokeyCiphertext.triggered.connect(self.autokeyCipher)
        self.actionAutokeyPlaintext.triggered.connect(self.autokeyPlain)

        # 多图替代密码
        self.actionPlayfair.triggered.connect(self.playfairCipher)

        # 置换密码
        self.actionPermutation.triggered.connect(self.permutationCipher)
        self.actionCPermutation.triggered.connect(self.columnPerCipher)
        self.actionDoubleTransposition.triggered.connect(self.doubleTransCipher)

        # 流密码
        self.actionRC4.triggered.connect(self.rc4Cipher)
        self.actionCA.triggered.connect(self.showMessage)

        # 分块密码
        self.actionDES.triggered.connect(self.desCipher)
        self.actionAES.triggered.connect(self.showMessage)

        # 公钥密码
        self.actionRSA.triggered.connect(self.rsaCipher)

        # bottom 动作
        # 单选按钮：选择输入文本或打开文件
        self.textModeButton.clicked.connect(self.changeTextMode)
        self.fileModeButton.clicked.connect(self.changeFileMode)

        # 获取文件加解密的文件路径
        self.inputFileButton.clicked.connect(self.inputFilePath)
        self.outputFileButton.clicked.connect(self.outputFilePath)

        # 将所有输入输出框清空
        self.resetText.clicked.connect(self.clearText)

        # 将输出框的内容复制到输入框中
        self.replaceOutToInput.clicked.connect(self.outToInput)

        # 生成RSA密钥
        self.rsaKeyGen.clicked.connect(self.genRSAKey)

        # 将输出框内容保存
        self.saveOutputButton.clicked.connect(self.saveFile)

    #   '''    ==============================   其   它   按   钮   功   能   ==============================    '''

    # 将输出框的内容复制到输入框中
    def outToInput(self):
        text = self.outputText.toPlainText()
        self.inputPlainTextEdit.setPlainText(text)
        self.outputText.clear()

    # 将所有输入输出框清空
    def clearText(self):
        self.inputPlainTextEdit.clear()
        self.lineEditFile.clear()
        self.lineEditOutFile.clear()
        self.inputKey.clear()
        self.inputKey2.clear()
        self.outputText.clear()

    def changeTextMode(self):
        if self.textModeButton.isChecked():
            self.inputFileButton.setEnabled(False)
            self.outputFileButton.setEnabled(False)
            self.lineEditFile.clear()
            self.lineEditOutFile.clear()

    def changeFileMode(self):
        if self.fileModeButton.isChecked():
            self.inputFileButton.setEnabled(True)
            self.outputFileButton.setEnabled(True)

    def fileButtonAction(self):
        pass

    #   '''    ===================================   文   件   操   作   ===================================    '''
    # 设置打开文件路径
    def inputFilePath(self):
        fileName0 = QFileDialog.getOpenFileName(self, "打开文件", "./", "Text files(*.txt)")
        if not fileName0[0] == '':
            self.lineEditFile.setText(fileName0[0])
            with open(fileName0[0], 'r', encoding='UTF-8') as f:
                text = f.read()
                self.inputPlainTextEdit.setPlainText(text)
                f.close()

    # 设置保存文件路径
    def outputFilePath(self):
        fileName0 = QFileDialog.getOpenFileName(self, "保存文件", "./", "Text files(*.txt)")
        if not fileName0[0] == '':
            self.lineEditOutFile.setText(fileName0[0])

    # 按下按钮将输出框中的文本保存
    def saveFile(self):
        fileName0 = QFileDialog.getSaveFileName(self, "保存文件", "./", "Text files(*.txt)")
        if not fileName0[0] == '':
            with open(fileName0[0], 'w', encoding='UTF-8') as f:
                text = self.outputText.toPlainText()
                f.write(text)
                f.close()

    # 文件模式下保存文件
    def fileModeSaveFile(self):
        filePath = self.lineEditOutFile.text()
        with open(filePath, 'w', encoding='UTF-8') as f:
            text = self.outputText.toPlainText()
            f.write(text)
            f.close()

    #   '''    ===================================   提   示   信   息   ===================================    '''

    # 未完成
    def showMessage(self):
        QMessageBox.information(self, "提示", "正在施工中。。。")

    # affine密钥错误提示
    def showAffineKeyError(self):
        QMessageBox.information(self, "提示", "Affine加解密中，应确定gcd(a,b)=1")

    # 未输入明文或密文
    def showNoTextError(self):
        QMessageBox.warning(self, "警告", "未输入明文或密文\n或未选择输入输出文件")

    # 未输入密钥
    def showNoKeyError(self):
        QMessageBox.warning(self, "警告", "未输入密钥")

    # 输入有误
    def showError(self):
        QMessageBox.warning(self, "警告", "输入有误")

    # 不支持文件加密
    def showNoSupportError(self):
        QMessageBox.warning(self, "警告", "该密码暂不支持文件加密")

    # 输入密钥有误
    def showKeyError(self):
        QMessageBox.warning(self, "警告", "key应该全为字母")

    # 解密错误
    def showDecryptError(self):
        QMessageBox.warning(self, "警告", "解密出错，请检查输入")

    #   '''    ===============================   获   取   输   入   信   息   ===============================    '''
    # 检查输入
    def checkInput(self):
        if self.textModeButton.isChecked():  # 文本加解密
            text = self.inputPlainTextEdit.toPlainText()
            key = self.inputKey.text()
            if text == "":  # 未输入明文或密文
                return -1
            elif key == "":  # 未输入密钥
                return -2
            else:
                return 0
        else:  # 文件加解密
            inFilePath = self.lineEditFile.text()
            outFilePath = self.lineEditOutFile.text()
            key = self.inputKey.text()
            if inFilePath == "" or outFilePath == "":  # 未选择输入或输出文件
                return -1
            elif key == "":
                return -2
            else:
                return 1

    # 获取信息
    def getInformation(self):
        key = self.inputKey.text()
        if self.textModeButton.isChecked():
            text = self.inputPlainTextEdit.toPlainText()
            if self.encryptButton.isChecked():
                return text, key, 1
            else:
                return text, key, 2
        else:
            inFilePath = self.lineEditFile.text()
            with open(inFilePath, 'r', encoding='UTF-8') as f:
                text = f.read()
            f.close()
            if self.encryptButton.isChecked():
                return text, key, 1
            else:
                return text, key, 2

    # 双密钥
    def getInformation2(self):
        key1 = self.inputKey.text()
        key2 = self.inputKey2.text()
        if self.textModeButton.isChecked():
            text = self.inputPlainTextEdit.toPlainText()
            if self.encryptButton.isChecked():
                return text, key1, key2, 1
            else:
                return text, key1, key2, 2
        else:
            inFilePath = self.lineEditFile.text()
            with open(inFilePath, 'r', encoding='UTF-8') as f:
                text = f.read()
            f.close()
            if self.encryptButton.isChecked():
                return text, key1, key2, 1
            else:
                return text, key1, key2, 2

    #   '''    ===================================   加   解   密   部   分   ===================================    '''

    #   '''    ==============================   单   表   替   代   加   解   密   ==============================    '''

    # 凯撒密码
    def caesarCipher(self):
        a = self.checkInput()
        if a == -1:
            self.showNoTextError()
        elif a == -2:
            self.showNoKeyError()
        elif a == 0 or a == 1:
            text, key, s = self.getInformation()
            try:
                key = int(key)
            except ValueError:
                self.showError()
            else:
                if 0 <= key <= 26:
                    if s == 1:
                        m = caesar.encrypt(text, key)
                    else:
                        m = caesar.decrypt(text, key)
                    self.outputText.setText(m)
                    if a == 1:
                        self.fileModeSaveFile()
                else:
                    self.showError()

    # keyword密码
    def keywordCipher(self):
        a = self.checkInput()
        if a == -1:
            self.showNoTextError()
        elif a == -2:
            self.showNoKeyError()
        elif a == 0 or a == 1:
            text, key, s = self.getInformation()
            if tools.checkKey(key):
                if s == 1:
                    m = kw.encrypt(text, key)
                else:
                    m = kw.decrypt(text, key)
                self.outputText.setText(m)
                if a == 1:
                    self.fileModeSaveFile()
            else:
                self.showKeyError()

    # Affine密码
    def affineCipher(self):
        a = self.checkInput()
        if a == -1:
            self.showNoTextError()
        elif a == -2:
            self.showNoKeyError()
        elif a == 0 or a == 1:
            text, a, b, s = self.getInformation2()
            try:
                a = int(a)
                b = int(b)
            except ValueError:
                self.showError()
            else:
                if 1 <= a <= 25 and 0 <= b <= 25:
                    if affine.gcd(a, b) == 1:
                        if s == 1:
                            m = affine.encrypt(text, a, b)
                        else:
                            m = affine.decrypt(text, a, b)
                        self.outputText.setText(m)
                        if a == 1:
                            self.fileModeSaveFile()
                    else:
                        self.showAffineKeyError()
                else:
                    self.showError()

    # Multilieral密码
    def multilieralCipher(self):
        a = self.checkInput()
        if a == -1:
            self.showNoTextError()
        elif a == -2:
            self.showNoKeyError()
        elif a == 0 or a == 1:
            text, key, s = self.getInformation()
            if tools.checkKey(key) or len(key) != 5:
                if s == 1:
                    m = multiliteral.encrypt(text, key)
                else:
                    m = multiliteral.decrypt(text, key)
                self.outputText.setText(m)
                if a == 1:
                    self.fileModeSaveFile()
            else:
                self.showKeyError()

    #   '''    ==============================   多   表   替   代   加   解   密   ==============================    '''
    # Vigenere密码
    def vigenereCipher(self):
        a = self.checkInput()
        if a == -1:
            self.showNoTextError()
        elif a == -2:
            self.showNoKeyError()
        elif a == 0 or a == 1:
            text, key, s = self.getInformation()
            if tools.checkKey(key):
                if s == 1:
                    m = vigenere.encrypt(text, key)
                else:
                    m = vigenere.decrypt(text, key)
                self.outputText.setText(m)
                if a == 1:
                    self.fileModeSaveFile()
            else:
                self.showKeyError()

    # Autokey Cipher
    def autokeyCipher(self):
        a = self.checkInput()
        if a == -1:
            self.showNoTextError()
        elif a == -2:
            self.showNoKeyError()
        elif a == 0 or a == 1:
            text, key, s = self.getInformation()
            if tools.checkKey(key):
                if s == 1:
                    m = autokey.encryptCipher(text, key)
                else:
                    m = autokey.decryptCipher(text, key)
                self.outputText.setText(m)
                if a == 1:
                    self.fileModeSaveFile()
            else:
                self.showKeyError()

    # Autokey Cipher
    def autokeyPlain(self):
        a = self.checkInput()
        if a == -1:
            self.showNoTextError()
        elif a == -2:
            self.showNoKeyError()
        elif a == 0 or a == 1:
            text, key, s = self.getInformation()
            if tools.checkKey(key):
                if s == 1:
                    m = autokey.encryptPlain(text, key)
                else:
                    m = autokey.decryptPlain(text, key)
                self.outputText.setText(m)
                if a == 1:
                    self.fileModeSaveFile()
            else:
                self.showKeyError()

    #   '''    ==============================   多   图   替   代   加   解   密   ==============================    '''
    # playfair密码
    def playfairCipher(self):
        a = self.checkInput()
        if a == -1:
            self.showNoTextError()
        elif a == -2:
            self.showNoKeyError()
        elif a == 0 or a == 1:
            text, key, s = self.getInformation()
            if tools.checkKey(key):
                if s == 1:
                    m = playfair.encrypt(text, key)
                else:
                    m = playfair.decrypt(text, key)
                self.outputText.setText(m)
                if a == 1:
                    self.fileModeSaveFile()
            else:
                self.showKeyError()

    #   '''    =====================================   置   换   密   码   =====================================    '''
    # Permutation密码
    def permutationCipher(self):
        a = self.checkInput()
        if a == -1:
            self.showNoTextError()
        elif a == -2:
            self.showNoKeyError()
        elif a == 1:
            self.showNoSupportError()
        elif a == 0:
            text, key, s = self.getInformation()
            if tools.checkText(text):
                key = tools.strToList(key)
                if key != -1:
                    if s == 1:
                        m = permutation.encrypt(text, key)
                    else:
                        m = permutation.decrypt(text, key)
                    self.outputText.setText(m)
                else:
                    self.showError()
            else:
                self.showError()

    # ColumnPermutation
    def columnPerCipher(self):
        a = self.checkInput()
        if a == -1:
            self.showNoTextError()
        elif a == -2:
            self.showNoKeyError()
        elif a == 1:
            self.showNoSupportError()
        elif a == 0:
            text, key, s = self.getInformation()
            if tools.checkKey(key):
                if s == 1:
                    m = columnPermutation.encrypt(text, key)
                else:
                    m = columnPermutation.decrypt(text, key)
                self.outputText.setText(m)
            else:
                self.showKeyError()

    # Double-Transposition
    def doubleTransCipher(self):
        a = self.checkInput()
        if a == -1:
            self.showNoTextError()
        elif a == -2:
            self.showNoKeyError()
        elif a == 1:
            self.showNoSupportError()
        elif a == 0:
            text, key1, key2, s = self.getInformation2()
            if tools.checkKey(key1) and tools.checkKey(key2):
                if s == 1:
                    m = doubleTransposition.encrypt(text, key1, key2)
                else:
                    m = doubleTransposition.decrypt(text, key1, key2)
                self.outputText.setText(m)
            else:
                self.showKeyError()

    #   '''    ================================   流   密   码   加   解   密   ================================    '''
    # RC4
    def rc4Cipher(self):
        a = self.checkInput()
        if a == -1:
            self.showNoTextError()
        elif a == -2:
            self.showNoKeyError()
        elif a == 1:
            self.showNoSupportError()
        elif a == 0:
            text, key, s = self.getInformation()
            if s == 1:
                m = rc4.encrypt(text, key)
                self.outputText.setText(m)
            else:
                m = rc4.decrypt(text, key)
                if m == -1:
                    self.showDecryptError()
                else:
                    self.outputText.setText(m)

    #   '''    ==============================   分   块   密   码   加   解   密   ==============================    '''
    # DES加解密
    def desCipher(self):
        a = self.checkInput()
        if a == -1:
            self.showNoTextError()
        elif a == -2:
            self.showNoKeyError()
        elif a == 1:
            self.showNoSupportError()
        elif a == 0:
            text, key, s = self.getInformation()
            if s == 1:
                m = myDes.encrypt(text, key)
                self.outputText.setText(m)
            else:
                m = myDes.decrypt(text, key)
                if m == -1:
                    self.showDecryptError()
                else:
                    self.outputText.setText(m)

    #   '''    ==============================   公   钥   密   码   加   解   密   ==============================    '''
    # 生成RSA密钥P，Q
    def genRSAKey(self):
        p = str(generateLargePrime())
        q = str(generateLargePrime())

        self.inputKey.setText(p)
        self.inputKey2.setText(q)

    # RSA加解密
    def rsaCipher(self):
        text, p, q, s = self.getInformation2()
        if text == "":
            self.showNoTextError()
        else:
            try:
                p = int(p)
                q = int(q)
                if s == 2:
                    c = int(text)
            except ValueError:
                self.showError()
            else:
                if isPrime(p) and isPrime(q):
                    if s == 1:
                        flag = tools.longToBytes(text)
                        m = myRsa.encrypt(flag, p, q)
                        self.outputText.setText(str(m))
                    else:
                        m = myRsa.decrypt(c, p, q)
                        m = tools.bytesToLong(m)
                        self.outputText.setText(m)
                else:
                    self.showError()


class DhWindow(QDialog, Ui_Dialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.setWindowIcon(QIcon('1207136.icon'))
        self.initUI()

    def initUI(self):
        self.gen_PG_buttom.clicked.connect(self.gen_P_G)
        self.gen_A_buttom.clicked.connect(self.gen_A)
        self.gen_B_button.clicked.connect(self.gen_B)
        self.snedGAButton.clicked.connect(self.sendGAToB)
        self.sendGBButton.clicked.connect(self.sendGBToA)
        self.calAKButton.clicked.connect(self.calAkey)
        self.calBKButton.clicked.connect(self.calBkey)
        self.pushButton.clicked.connect(self.clearText)

    def showNoPG(self):
        QMessageBox.warning(self, "警告", "请生成P，G")

    def showNoA(self):
        QMessageBox.warning(self, "警告", "请生成a")

    def showNoB(self):
        QMessageBox.warning(self, "警告", "请生成b")

    def showNoGB(self):
        QMessageBox.warning(self, "警告", "请获得G^b(mod p)")

    def showNoGA(self):
        QMessageBox.warning(self, "警告", "请获得G^a(mod p)")

    def gen_P_G(self):
        p = generateLargePrime()
        g = tools.gen_RandNum()
        self.largeP_text.setPlainText(str(p))
        self.randG_text.setPlainText(str(g))

    def gen_A(self):
        a = tools.gen_RandNum()
        self.randA.setPlainText(str(a))

    def gen_B(self):
        b = tools.gen_RandNum()
        self.randB.setPlainText(str(b))

    def sendGAToB(self):
        p = self.largeP_text.toPlainText()
        g = self.randG_text.toPlainText()
        a = self.randA.toPlainText()
        if p == '' or g == '':
            self.showNoPG()
        elif a == '':
            self.showNoA()
        else:
            p = int(p)
            g = int(g)
            a = int(a)
            stb = pow(g, a, p)
            self.GATextEdit.setPlainText(str(stb))

    def sendGBToA(self):
        p = self.largeP_text.toPlainText()
        g = self.randG_text.toPlainText()
        b = self.randB.toPlainText()
        if p == '' or g == '':
            self.showNoPG()
        elif b == '':
            self.showNoB()
        else:
            p = int(p)
            g = int(g)
            b = int(b)
            sta = pow(g, b, p)
            self.GBTextEdit.setPlainText(str(sta))

    def calAkey(self):
        p = self.largeP_text.toPlainText()
        a = self.randA.toPlainText()
        gb = self.GBTextEdit.toPlainText()
        if p == '':
            self.showNoPG()
        elif a == '':
            self.showNoA()
        elif gb == '':
            self.showNoGB()
        else:
            p = int(p)
            a = int(a)
            gb = int(gb)
            key = pow(gb, a, p)
            self.aKeyTextEdit.setPlainText(str(key))

    def calBkey(self):
        p = self.largeP_text.toPlainText()
        b = self.randB.toPlainText()
        ga = self.GATextEdit.toPlainText()
        if p == '':
            self.showNoPG()
        elif b == '':
            self.showNoB()
        elif ga == '':
            self.showNoGA()
        else:
            p = int(p)
            b = int(b)
            ga = int(ga)
            key = pow(ga, b, p)
            self.bKeyTextEdit.setPlainText(str(key))

    def clearText(self):
        self.largeP_text.setPlainText("")
        self.randG_text.setPlainText("")
        self.randA.setPlainText("")
        self.randB.setPlainText("")
        self.GATextEdit.setPlainText("")
        self.GBTextEdit.setPlainText("")
        self.aKeyTextEdit.setPlainText("")
        self.bKeyTextEdit.setPlainText("")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MainWindow()
    myWin.show()
    childWin = DhWindow()
    dhb = myWin.dhModeButton
    dhb.clicked.connect(childWin.show)
    sys.exit(app.exec_())
