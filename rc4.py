# -*- coding: UTF-8 -*-
# @File: rc4.py
# @Author: SCERush
# @Contact: 1037920609@qq.com
# @Datetime: 20/7/4 13:15
# @Software: PyCharm
"""
文件说明：RC4密码
"""

import hashlib
import base64


def KSA(key):
    """
    密钥初始流程KSA
    :param key: 
    :return: 
    """
    key = hashlib.md5(key.encode('UTF-8')).hexdigest()
    S = []
    K = []
    for i in range(256):
        S.append(i)
        K.append(key[i % len(key)])
    j = 0
    for i in range(256):
        j = (j + S[i] + ord(K[i])) % 256
        S[i], S[j] = S[j], S[i]
    return S


def PRGA(text, key):
    """
    加解密算法
    :param text: 
    :param key: 
    :return: 
    """
    S = KSA(key)
    outText = ""
    i = j = 0
    for a in text:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        t = (S[i] + S[j]) % 256

        c = chr(ord(a) ^ S[t])
        outText += c
    return outText


def encodeBase64(text):
    """ text to base64 """
    text1 = text.encode('UTF-8')
    text2 = base64.b64encode(text1)
    text3 = text2.decode()
    return text3


def decodeBase64(text):
    """ base64 to text """
    text1 = text.encode()
    text2 = base64.b64decode(text1)
    text3 = text2.decode('UTF-8')
    return text3


def encrypt(plaintext, key):
    """
    加密最终输出为base64串
    :param plaintext: 
    :param key: 
    :return: 
    """
    plain = encodeBase64(plaintext)
    cipher = PRGA(plain, key)
    return encodeBase64(cipher)


def decrypt(ciphertext, key):
    """
    因为之前输出是base64串，所以需要对其检验
    :param ciphertext:
    :param key:
    :return:
    """
    try:
        cipher = decodeBase64(ciphertext)
    except Exception:
        return -1
    else:
        plain = PRGA(cipher, key)
        return decodeBase64(plain)


if __name__ == '__main__':
    p = "RC4流密码加解密"
    key = "流：stream"
    c = encrypt(p, key)
    print(c)
    d = decrypt(c, key)
    print(d)
