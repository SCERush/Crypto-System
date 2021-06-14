# -*- coding: UTF-8 -*-
# @File: columnPermutation.py
# @Author: SCERush
# @Contact: 1037920609@qq.com
# @Datetime: 20/7/5 19:56
# @Software: PyCharm
"""
文件说明：Column Permutation密码
"""

import re


def removePunctuation(text, filter='[^A-Z]'):
    return re.sub(filter, '', text.upper())


def sortind(key):
    """ 通过key获取加密顺序 """
    t1 = [(key[i], i) for i in range(len(key))]
    t2 = [(k[1], i) for i, k in enumerate(sorted(t1))]
    return [q[1] for q in sorted(t2)]


def unsortind(key):
    """ 通过key获取解密顺序 """
    t1 = [(key[i], i) for i in range(len(key))]
    return [q[1] for q in sorted(t1)]


def encrypt(plaintext, key):
    """ 加密函数 """
    plain = removePunctuation(plaintext)
    cipher = ''
    ind = sortind(key)
    for i in range(len(key)):
        cipher += plain[ind.index(i)::len(key)]
    return cipher


def decrypt(ciphertext, key):
    """ 解密函数 """
    cipher = removePunctuation(ciphertext)
    plain = ['_'] * len(cipher)
    l, m = len(cipher), len(key)
    ind = unsortind(key)
    upto = 0
    for i in range(len(key)):
        collen = int(l / m)
        if ind[i] < l % m:
            collen += 1
        plain[ind[i]::m] = cipher[upto:upto + collen]
        upto += collen
    return ''.join(plain)


if __name__ == '__main__':
    m = "This is the plain text"
    k = "key"
    kl = sortind(k)
    print(kl)
    uk = unsortind(k)
    print(uk)
    c = encrypt(m, k)
    print(c)
    d = decrypt(c, k)
    print(d)
