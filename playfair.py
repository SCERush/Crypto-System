# -*- coding: UTF-8 -*-
# @File: playfair.py
# @Author: SCERush
# @Contact: 1037920609@qq.com
# @Datetime: 20/7/2 19:14
# @Software: PyCharm
"""
文件说明：playfair密码
"""

import re


def getKeywordList(keyword):
    """
    获取密钥矩阵
    :param keyword:
    :return:
    """
    keyword = keyword.upper().replace('J', 'I')
    normalList = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    toCombine = keyword + normalList
    combineList = ''
    for i in toCombine:
        if i in combineList:
            pass
        else:
            combineList = combineList + i
    return combineList


def removePunctuation(text):
    """
    将文本中非英文字母去掉，并将字母转为大写
    :param text:
    :return:
    """
    filter = '[^A-Z]'
    return re.sub(filter, '', text.upper())


def encryptPart(keywordList, a, b):
    """
    加密主要算法：
    首先获取得到的两个字母在矩阵中的行列值
    然后对两个坐标分别进行判断：
    1.位于同一行，返回两个字母在矩阵中右边的字母
    2.位于同一列，返回两个字母在矩阵中下边的字母
    3.位于对角，返回相应对角字母
    :param keywordList:
    :param a:
    :param b:
    :return:
    """
    arow, acol = int(keywordList.index(a) / 5), keywordList.index(a) % 5
    brow, bcol = int(keywordList.index(b) / 5), keywordList.index(b) % 5
    if arow == brow:
        return keywordList[arow * 5 + (acol + 1) % 5] + keywordList[brow * 5 + (bcol + 1) % 5]
    elif acol == bcol:
        return keywordList[((arow + 1) % 5) * 5 + acol] + keywordList[((brow + 1) % 5) * 5 + bcol]
    else:
        return keywordList[arow * 5 + bcol] + keywordList[brow * 5 + acol]


def decryptPart(keywordList, a, b):
    """
    加密算法的逆运算
    """
    arow, acol = int(keywordList.index(a) / 5), keywordList.index(a) % 5
    brow, bcol = int(keywordList.index(b) / 5), keywordList.index(b) % 5
    if arow == brow:
        return keywordList[arow * 5 + (acol - 1) % 5] + keywordList[brow * 5 + (bcol - 1) % 5]
    elif acol == bcol:
        return keywordList[((arow - 1) % 5) * 5 + acol] + keywordList[((brow - 1) % 5) * 5 + bcol]
    else:
        return keywordList[arow * 5 + bcol] + keywordList[brow * 5 + acol]


def encrypt(plaintext, key):
    """
    对获取的明文进行基本的处理
    转为大写
    除去非字母
    如果遇到两个相同的字母，在中间加'Q'
    文本长度不足2的倍数需要加'X'补齐
    然后以两两字母进行加密
    :param plaintext:
    :param key:
    :return:
    """
    plaintext = removePunctuation(plaintext).replace('J', 'I')
    plain = ""
    plain += plaintext[0]
    for i in range(1, len(plaintext)):
        if plain[len(plain) - 1] == plaintext[i]:
            plain += 'Q'
        plain += plaintext[i]
    keywordList = getKeywordList(key)
    if len(plain) % 2 == 1:
        plain += 'X'
    ret = ''
    for c in range(0, len(plain), 2):
        ret += encryptPart(keywordList, plain[c], plain[c + 1])
    return ret


def decrypt(ciphertext, key):
    """
    同加密
    """
    cipher = removePunctuation(ciphertext).replace('J', 'I')
    keywordList = getKeywordList(key)
    if len(cipher) % 2 == 1:
        cipher += 'X'
    ret = ''
    for c in range(0, len(cipher), 2):
        ret += decryptPart(keywordList, cipher[c], cipher[c + 1])
    return ret


if __name__ == '__main__':
    key = "cipher"
    key = getKeywordList(key)
    p = "PlayfairCipher"
    d = encrypt(p, key)
    print(d)
    m = decrypt(d, key)
    print(m)
