# -*- coding: UTF-8 -*-
# @File: autokey.py
# @Author: SCERush
# @Contact: 1037920609@qq.com
# @Datetime: 20/7/6 13:57
# @Software: PyCharm
"""
文件说明：
"""

import re


def removePunctuation(text, filter='[^A-Z]'):
    return re.sub(filter, '', text.upper())


def encryptPlain(text, keyword):
    """
    对于Autokey Plaintext，本质上和vigenere相同，相当于将明文附加在key后面作为密钥来进行vigenere加密
    但明文中的空格、非字母字符会影响加密，所以在Autokey的加解密中将除去所有非字母字符，并将全部字母大写
    :param text:
    :param keyword:
    :return:
    """
    text = removePunctuation(text)
    res = ""
    key = keyword.upper()
    for (i, c) in enumerate(text):
        if i < len(key):  # 明文前i项，使用key进行vigenere加密
            offset = ord(key[i]) - 65
        else:  # 从明文的i+1项，使用明文作为密钥进行vigenere加密
            offset = ord(text[i - len(key)]) - 65
        res += chr((ord(c) - 65 + offset) % 26 + 65)
    return res


def decryptPlain(text, keyword):
    """ 因为Autokey本质上是vigenere加密，所以在解密上唯一不同的点就是“-offset” """
    text = removePunctuation(text)
    res = ""
    key = keyword.upper()
    for (i, c) in enumerate(text):
        if i < len(key):
            offset = ord(key[i]) - 65
        else:
            offset = ord(res[i - len(key)]) - 65
        res += chr((ord(c) - 65 - offset) % 26 + 65)  # 不同点
    return res


def encryptCipher(text, keyword):
    """
    Autokey Cipher的加解密与Autokey Plain的解加密相对应
    但在求offset上不同，此处使用的与plain相反
    :param text:
    :param keyword:
    :return:
    """
    text = removePunctuation(text)
    res = ""
    key = keyword.upper()
    for (i, c) in enumerate(text):
        if i < len(key):
            offset = ord(key[i]) - 65
        else:
            offset = ord(res[i - len(key)]) - 65
        res += chr((ord(c) - 65 + offset) % 26 + 65)
    return res


def decryptCipher(text, keyword):
    text = removePunctuation(text)
    res = ""
    key = keyword.upper()
    for (i, c) in enumerate(text):
        if i < len(key):
            offset = ord(key[i]) - 65
        else:
            offset = ord(text[i - len(key)]) - 65
        res += chr((ord(c) - 65 - offset) % 26 + 65)
    return res


if __name__ == '__main__':
    m = "This is autokey cipher"
    k = "key"
    c = encryptPlain(m, k)
    print(c)
    d = decryptPlain(c, k)
    print(d)

    cc = encryptCipher(m, k)
    print(cc)
    dd = decryptCipher(cc, k)
    print(dd)
