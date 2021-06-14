# -*- coding: UTF-8 -*-
# @File: myDes.py
# @Author: SCERush
# @Contact: 1037920609@qq.com
# @Datetime: 20/7/4 15:55
# @Software: PyCharm
"""
文件说明：DES
"""

import re
import tools
import binascii
from desMatrix import *


def strToHex(str_text):
    """
    将str型数据转换成16进制字符串
    :param str_text: str
    :return: hex
    """
    return binascii.hexlify(str_text.encode()).decode()


def hexToBin(hex_text):
    """
    将hex型数据转换成2进制的字符串
    :param hex_text: hex
    :return: bin
    """
    bin_text = ''
    for i in hex_text:
        text_ord = int(i, 16)
        bin_text += decToBinStr(text_ord)
    # 将text与key补全，使长度其为64整数倍
    hex_len = len(hex_text) % 16
    if hex_len != 0:
        bin_text += '0' * (16 - hex_len) * 4
    return bin_text


def decToBinStr(d, lens=4):
    """
    将10进制转为2进制字符串
    :param d: dec num "1"
    :param lens:
    :return: bin num "0001"
    """
    bin_text = ''
    for i in range(lens):
        bin_text = str(d >> i & 1) + bin_text
    return bin_text


def binToHex(bin_text):
    """
    将2进制字符串转为hex型字符串
    :param bin_text: bin
    :return: hex
    """
    bin_num = bin_text.encode()
    res = hex(int(bin_num, 2))
    return str(res)[2:]


# 明文密文置换部分
def ipChange(bin_str):
    """
    IP盒处理
    :param bin_str: 64bit
    :return: 64bit
    """
    res = ""
    for i in IP:
        res += bin_str[i - 1]
    return res


def fpChange(bin_str):
    """
    末置换
    :param bin_str: 64bit
    :return: 64bit
    """
    res = ""
    for i in FP:
        res += bin_str[i - 1]
    return res


def eChange(bin_str):
    """
    E-Box置换
    :param bin_str: 32bit
    :return: 48bit
    """
    res = ""
    for i in E_Box:
        res += bin_str[i - 1]
    return res


def str_xor(text, key):
    """
    异或
    :param text: 48bit
    :param key: 48bit
    :return: 48bit
    """
    res = ""
    for i in range(0, len(text)):
        xor_num = int(text[i], 10) ^ int(key[i], 10)
        if xor_num == 1:
            res += '1'
        if xor_num == 0:
            res += '0'
    return res


def sChange(bin_str):
    """
    S-Box置换
    :param bin_str: 48bit
    :return: 32bit
    """
    res = ""
    c = 0
    for i in range(0, len(bin_str), 6):
        run_str = bin_str[i:i + 6]
        row = int(run_str[0] + run_str[5], 2)
        col = int(run_str[1:5], 2)
        num = bin(S_Box[c][row * 16 + col])[2:]
        for j in range(0, 4-len(num)):
            num = '0' + num
        res += num
        c += 1
    return res


def pChange(bin_str):
    """
    P-Box置换
    :param bin_str: 64bit
    :return: 64bit
    """
    res = ""
    for i in P_Box:
        res += bin_str[i - 1]
    return res


# 密钥处理部分
def pc1_Change(key):
    """
    密钥PC-1置换
    :param key: 64bit
    :return: 56bit
    """
    res = ""
    for i in PC_1:
        res += key[i - 1]
    return res


def leftShift(sub_key, num):
    """
    循环左移
    :param sub_key: 28bit
    :param num: turn
    :return: 28bit
    """
    res = sub_key[num:len(sub_key)]
    res = res + sub_key[0:num]
    return res


def pc2_Change(key):
    """
    密钥PC-2置换
    :param key: 56bit
    :return: 48bit
    """
    res = ""
    for i in PC_2:
        res += key[i - 1]
    return res


def function_f(bin_str, key):
    """
    将E-Box,xor,S-Box,P-Box的运算封装在一起
    :param bin_str: 32bit
    :param key: 48bit
    :return: 32bit
    """
    first_str = eChange(bin_str)  # E-Box 32bit->48bit
    second_str = str_xor(first_str, key)  # xor
    third_str = sChange(second_str)  # S-Box 48bit->32bit
    final_str = pChange(third_str)  # P-Box 32bit
    return final_str


def gen_key(key):
    """
    生成子密钥
    :param key: 64bit
    :return: 48bit * 16
    """
    key_list = []
    first_change = pc1_Change(key)  # 56bit
    key_C0 = first_change[0:28]  # 28bit
    key_D0 = first_change[28:]
    for i in LS:
        key_Ci = leftShift(key_C0, i)
        key_Di = leftShift(key_D0, i)
        second_change = pc2_Change(key_Ci + key_Di)  # 48bit
        key_list.append(second_change)
    return key_list


def encryptPart(bin_plain, bin_key):
    """
    加密主要算法
    :param bin_plain: 64bit
    :param bin_key: 64bit
    :return: 64bit
    """
    ip_str = ipChange(bin_plain)  # ip初始置换
    key_list = gen_key(bin_key)  # 生成子密钥
    plain_left = ip_str[0:32]
    plain_right = ip_str[32:]

    # 进行前15次轮换
    for i in range(0, 15):
        tmp_right = plain_right
        f_res = function_f(tmp_right, key_list[i])
        plain_right = str_xor(f_res, plain_left)
        plain_left = tmp_right
    # 第16次轮换
    f_res = function_f(plain_right, key_list[15])
    fin_left = str_xor(plain_left, f_res)
    fin_right = plain_right
    fin_str = fpChange(fin_left + fin_right)  # 末置换
    return fin_str


def decryptPart(bin_cipher, bin_key):
    """
    解密函数主体部分，同加密算法，注意密钥是反序的
    :param bin_cipher: 64bit
    :param bin_key: 64bit
    :return: 64bit
    """
    ip_str = ipChange(bin_cipher)
    key_list = gen_key(bin_key)
    cipher_left = ip_str[0:32]
    cipher_right = ip_str[32:]

    for i in range(0, 15):
        j = 15 - i  # 从第16个子密钥开始轮换
        tmp_right = cipher_right
        f_res = function_f(cipher_right, key_list[j])
        cipher_right = str_xor(cipher_left, f_res)
        cipher_left = tmp_right

    f_res = function_f(cipher_right, key_list[0])
    fin_left = str_xor(cipher_left, f_res)
    fin_right = cipher_right
    fin_str = fpChange(fin_left + fin_right)
    return fin_str


def encrypt(plaintext, key):
    """
    加密函数入口，主要作用是将明文和密钥转为64倍数位的2进制bit流
    :param plaintext:
    :param key:
    :return: 16进制密文
    """
    bin_plain = hexToBin(strToHex(plaintext))  # 获得明文的64倍数位bit流
    bin_key = hexToBin(strToHex(key))  # 获得密钥的64倍数位bit流
    tmp = re.findall(r'.{64}', bin_plain)  # 将明文bit流分为64一组
    bin_cipher = ""
    for i in tmp:
        bin_cipher += encryptPart(i, bin_key[0:64])  # 对每组bit流进行加密
    return binToHex(bin_cipher)  # 返回16进制密文


def decrypt(ciphertext, key):
    """
    基本上同加密算法，不同的是首先需要对输入进行检查
    :param ciphertext:
    :param key:
    :return:
    """
    try:
        bin_cipher = hexToBin(ciphertext)
    except Exception:
        return -1
    else:
        bin_key = hexToBin(strToHex(key))
        tmp = re.findall(r'.{64}', bin_cipher)
        bin_plain = ""
        for i in tmp:
            bin_plain += decryptPart(i, bin_key[0:64])
        return tools.bytesToLong(int(bin_plain.encode(), 2))


if __name__ == '__main__':
    m = "123456789 asd 加解密"
    k = "123Des密码"
    c = encrypt(m, k)
    print(c)
    d = decrypt(c, k)
    print(d)
