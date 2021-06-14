# -*- coding: UTF-8 -*-
# @File: doubleTransposition.py
# @Author: SCERush
# @Contact: 1037920609@qq.com
# @Datetime: 20/7/5 20:02
# @Software: PyCharm
"""
文件说明：Double-Transposition密码
因为Double-Transposition就是两次Column Permutation，所以直接调用函数即可
"""

import columnPermutation


def encrypt(plaintext, key1, key2):
    cipher1 = columnPermutation.encrypt(plaintext, key1)
    cipher2 = columnPermutation.encrypt(cipher1, key2)
    return cipher2


def decrypt(ciphertext, key1, key2):
    plain1 = columnPermutation.decrypt(ciphertext, key2)
    plain2 = columnPermutation.decrypt(plain1, key1)
    return plain2


if __name__ == '__main__':
    m = "This is the plain text"
    k1 = "key"
    k2 = "dog"
    c = encrypt(m, k1, k2)
    print(c)
    d = decrypt(c, k1, k2)
    print(d)
