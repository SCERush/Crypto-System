# -*- coding: UTF-8 -*-
# @File: tools.py
# @Author: SCERush
# @Contact: 1037920609@qq.com
# @Datetime: 20/7/2 19:20
# @Software: PyCharm
"""
文件说明：
"""

import re
import random
import binascii
from RabinMiller import generateLargePrime


def removePunctuation(text):
    """ 除去非字母字符 """
    filter = '[^a-zA-Z]'
    return re.sub(filter, '', text)


def checkKey(text):
    """ 检查密钥是否为英文 """
    for i in range(len(text)):
        if not text[i].isalpha():
            return False
    return True


def checkText(text):
    """ 检查文本是否为英文 """
    text = text.replace(' ', '')
    for i in range(len(text)):
        if not text[i].isalpha():
            return False
    return True


def strToList(text):
    """ 将Permutation的密钥转换为list形式 """
    try:
        listKey = list(map(int, text.split()))
    except ValueError:
        return -1
    else:
        for i in range(1, len(listKey)):
            if i in listKey:
                pass
            else:
                return -1
        return listKey


def gcd(a, b):
    """ 求最大公因数 """
    if a < b:
        a, b = b, a
    while b != 0:
        temp = a % b
        a = b
        b = temp
    return a


def longToBytes(text):
    """ 将数据转换为int类型 """
    return int(binascii.hexlify(text.encode()), 16)


def bytesToLong(num):
    """ 将int型转换为str类型 """
    return binascii.a2b_hex(str(hex(num)[2::1])).decode()


def gen_RandNum(size=512):
    """ 512位随机整数 a,b """
    return random.randrange(2 ** (size - 1), 2 ** size)


if __name__ == '__main__':
    m = 'flag{this_is_flag}'

    m = "中文 字符"
    # str
    print(binascii.hexlify(m.encode()).decode())

    # int
    c = longToBytes(m)
    print(c)

    # int -> hex
    print(hex(c))
    print(hex(c)[2::1])
    print(bytesToLong(c))
