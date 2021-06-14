# -*- coding: UTF-8 -*-
# @File: permutation.py
# @Author: SCERush
# @Contact: 1037920609@qq.com
# @Datetime: 20/7/3 14:43
# @Software: PyCharm
"""
文件说明：permutation密码
"""

import tools


def inverseKey(key):
    """
    通过key获取解密时所需要的key的逆解
    :param key:
    :return:
    """
    inverse = []
    for i in range(min(key), max(key) + 1):
        inverse.append(key.index(i) + 1)
    return inverse


def encrypt(plaintext, key):
    """
    便于在之后对文本的遍历，首先将文本补齐，使其长度为密钥长度的整数倍
    然后开始分组遍历，通过对range参数的设置，使每次加密都对密钥长度的明密文进行加解密
    然后对组内明密文进行加解密
    :param plaintext:
    :param key:
    :return:
    """
    plaintext = tools.removePunctuation(plaintext).upper()
    cipher = ''
    for i in range(0, len(plaintext) % len(key) * -1 % len(key)):
        plaintext += "X"
    for i in range(0, len(plaintext), len(key)):  # 步长设置为密钥长度
        for j in [a - 1 for a in key]:
            cipher += plaintext[i + j]
        cipher += " "
    return cipher[:-1]


def decrypt(ciphertext, key):
    """ 得到逆密钥，然后和加密一样 """
    return encrypt(ciphertext, inverseKey(key))


if __name__ == '__main__':
    f = "this is the plain text"
    key = [3, 4, 1, 5, 2]
    key2 = inverseKey(key)
    print(key2)
    c = encrypt(f, key)
    print(c)
    m = decrypt(c, key)
    print(m)
