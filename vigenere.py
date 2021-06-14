# -*- coding: UTF-8 -*-
# @File: vigenere.py
# @Author: SCERush
# @Contact: 1037920609@qq.com
# @Datetime: 20/7/1 17:04
# @Software: PyCharm
"""
文件说明：vigenere密码
"""


def encrypt(plaintext, key):
    """
    vigenere密码就相当于Caesar密码，不同的是vigenere的密钥key是可变的几个值，然后使用这几个值进行加解密
    :param plaintext:
    :param key:
    :return:
    """
    cipher = ''
    count = 0  # 设置一个计数器，当遇到非字母的时候加一，便于之后确定key
    key = key.lower()
    for i in range(len(plaintext)):
        if not plaintext[i].isalpha():
            cipher += plaintext[i]
            count += 1
        else:
            a = "A" if plaintext[i].isupper() else "a"
            offset = ord(key[(i - count) % len(key)]) - ord('a')  # offset:相当于Caesar中的key
            cipher += chr((ord(plaintext[i]) - ord(a) + offset) % 26 + ord(a))
    return cipher


def decrypt(ciphertext, key):
    """
    解密算法原理同Caesar
    """
    plain = ''
    count = 0
    key = key.lower()
    for i in range(len(ciphertext)):
        if not ciphertext[i].isalpha():
            plain += ciphertext[i]
            count += 1
        else:
            a = "A" if ciphertext[i].isupper() else "a"
            offset = ord(key[(i - count) % len(key)]) - ord('a')
            plain += chr((ord(ciphertext[i]) - ord(a) - offset) % 26 + ord(a))
    return plain


if __name__ == '__main__':
    p = "flag{This_is_plaintext_123}"
    k = "key"
    c = encrypt(p, k)
    print(c)
    m = decrypt(c, k)
    print(m)
