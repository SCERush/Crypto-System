# -*- coding: UTF-8 -*-
# @File: affine.py
# @Author: SCERush
# @Contact: 1037920609@qq.com
# @Datetime: 20/7/2 15:41
# @Software: PyCharm
"""
文件说明：仿射密码
"""


def gcd(a, b):
    """
    求a，b的最大公因数，判断a，b是否合法
    :param a:
    :param b:
    :return:
    """
    if a < b:
        a, b = b, a
    while b != 0:
        temp = a % b
        a = b
        b = temp
    return a


def egcd(a, b):
    """
    扩展欧几里得算法，用于之后求逆元
    :param a:
    :param b:
    :return:
    """
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y


def modinv(a, m):
    """
    求逆元
    :param a:
    :param m:
    :return:
    """
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def encrypt(plaintext, a, b):
    """
    加密函数：E(x) = (ax + b)(mod m) m为编码系统中的字母数，一般为26
    :param plaintext:
    :param a:
    :param b:
    :return:
    """
    cipher = ""
    for i in plaintext:
        if not i.isalpha():
            cipher += i
        else:
            n = "A" if i.isupper() else "a"
            cipher += chr((a * (ord(i) - ord(n)) + b) % 26 + ord(n))
    return cipher


def decrypt(ciphertext, a, b):
    """
    解密函数：D(x) = a^-1 * (x - b)(mod m) a^-1:a在m上的乘法逆元
    :param ciphertext:
    :param a:
    :param b:
    :return:
    """
    a1 = modinv(a, 26)
    plain = ""
    for i in ciphertext:
        if not i.isalpha():
            plain += i
        else:
            n = "A" if i.isupper() else "a"
            plain += chr((a1 * (ord(i) - ord(n) - b)) % 26 + ord(n))
    return plain


if __name__ == '__main__':
    p = "Affine Cipher 123"
    a = 5
    b = 8
    c = encrypt(p, a, b)
    print(c)
    m = decrypt(c, a, b)
    print(m)
