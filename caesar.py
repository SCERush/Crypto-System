# -*- coding: UTF-8 -*-
# @File: caesar.py
# @Author: SCERush
# @Contact: 1037920609@qq.com
# @Datetime: 20/7/1 15:20
# @Software: PyCharm
"""
文件说明：凯撒密码
"""


def encrypt(plaintext, key):
    """
    加密函数，主要原理是将明文中每个字母的序号加上key值即可得到密文
    :param plaintext:
    :param key: 0 ~ 25
    :return: cipher
    """
    re_str = ""
    for i in plaintext:
        if not i.isalpha():
            re_str += i  # 判断是否为字母，若不是则不需要操作
        else:
            a = "A" if i.isupper() else "a"  # 根据当前字母是否大小写，确定其ASCII码范围值
            re_str += chr((ord(i) - ord(a) + key) % 26 + ord(a))
    return re_str


def decrypt(ciphertext, key):
    """
    解密函数，用26来减去key得到偏移量，再次进行加密函数即可得出明文
    :param ciphertext:
    :param key: 0 ~ 25
    :return: cipher
    """
    return encrypt(ciphertext, 26 - key)


if __name__ == '__main__':
    p = "flag{This_is_plaintext_123}"
    c = encrypt(p, 13)
    print(c)
    m = decrypt(c, 13)
    print(m)
