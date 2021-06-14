# -*- coding: UTF-8 -*-
# @File: multiliteral.py
# @Author: SCERush
# @Contact: 1037920609@qq.com
# @Datetime: 20/7/5 17:30
# @Software: PyCharm
"""
文件说明：multiliteral密码
"""

import re

# 字母表
keywordList = "ABCDEFGHIKLMNOPQRSTUVWXYZ"


def removePunctuation(text):
    filter = '[^A-Z]'
    return re.sub(filter, '', text.upper())


def encrypt(plaintext, key):
    """
    主要算法，获取加密字母在二维字母表中的行列值，其密文为与之对应的key中位置的相应字母
    :param plaintext:
    :param key:
    :return:
    """
    plain = removePunctuation(plaintext).replace('J', 'I')
    key = key.upper()
    cipher = ''
    for i in range(len(plain)):
        row = int(keywordList.index(plain[i]) / 5)
        cipher += key[row]
        col = keywordList.index(plain[i]) % 5
        cipher += key[col]
    return cipher


def decrypt(ciphertext, key):
    """
    主要算法：对密文两两遍历，找到相应字母在key中的位置，分别对应明文在字母表中的行列
    :param ciphertext:
    :param key:
    :return:
    """
    cipher = removePunctuation(ciphertext).replace('J', 'I')
    key = key.upper()
    plain = ''
    for i in range(0, len(cipher), 2):
        row = key.index(cipher[i])
        col = key.index(cipher[i + 1])
        num = row * 5 + col
        plain += keywordList[num]
    return plain


if __name__ == '__main__':
    m = "Multilieral"
    key = "codes"
    c = encrypt(m, key)
    print(c)
    d = decrypt(c, key)
    print(d)
