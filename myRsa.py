# -*- coding: UTF-8 -*-
# @File: myRsa.py
# @Author: SCERush
# @Contact: 1037920609@qq.com
# @Datetime: 20/7/2 21:12
# @Software: PyCharm
"""
文件说明：RSA公钥密码
"""


import tools


def egcd(a, b):
    """ 扩展欧几里得算法 """
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y


def modinv(a, m):
    """ 求乘法逆元 """
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def encrypt(m, p, q):
    """ 加密函数 """
    e = 65537
    n = p * q
    return pow(m, e, n)


def decrypt(c, p, q):
    """ 解密函数 """
    n = p * q
    e = 65537
    phi = (p - 1) * (q - 1)
    d = modinv(e, phi)  # 求私钥d
    return pow(c, d, n)


if __name__ == '__main__':
    p = 9018588066434206377240277162476739271386240173088676526295315163990968347022922841299128274551482926490908399237153883494964743436193853978459947060210411
    q = 7547005673877738257835729760037765213340036696350766324229143613179932145122130685778504062410137043635958208805698698169847293520149572605026492751740223
    m = 'flag{this_is_flag}'
    m = tools.longToBytes(m)
    c = encrypt(m, p, q)
    print(c)
    d = decrypt(c, p, q)
    print(d)
    print(tools.bytesToLong(d))
