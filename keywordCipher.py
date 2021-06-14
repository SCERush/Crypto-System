# -*- coding: UTF-8 -*-
# @File: keywordCipher.py
# @Author: SCERush
# @Contact: 1037920609@qq.com
# @Datetime: 20/7/1 18:56
# @Software: PyCharm
"""
文件说明：keyword密码
"""


def getKeywordList(keyword):
    """
    主要用于生成密码表
    :param keyword:
    :return:
    """
    normalList = ''
    keyword = keyword.lower()
    for i in range(26):
        normalList = normalList + chr(ord('a') + i)
    toCombine = keyword + normalList
    combineList = ''
    for i in toCombine:
        if i in combineList:
            pass
        else:
            combineList = combineList + i
    if len(combineList) == 26:
        return combineList
    else:
        return ''


def replaceChar(keywordList, inputChar):
    """
    对于大写字母，就先转换为小写然后继续调用改函数
    转换至小写字母后，得到该字母在字母表上的位置然后使用keywordList替换即可
    :param keywordList:
    :param inputChar: 当前加密字母
    :return: 加密后的字母
    """
    if inputChar.isupper():
        return replaceChar(keywordList, inputChar.lower()).upper()
    else:
        return keywordList[ord(inputChar) - 97]


def dereplaceChar(keywordList, inputChar):
    """
    解密函数就是加密函数的逆过程
    :param keywordList:
    :param inputChar:
    :return:
    """
    if inputChar.isupper():
        return dereplaceChar(keywordList, inputChar.lower()).upper()
    else:
        return chr(keywordList.find(inputChar) + 97)


def encrypt(toReplace, keyword):
    """
    keyword 字符替换法 替换函数
    """
    afterReplace = ''
    keywordList = getKeywordList(keyword)
    for i in toReplace:
        if i.isalpha():
            afterReplace = afterReplace + replaceChar(keywordList, i)
        else:
            afterReplace = afterReplace + i
    return afterReplace


def decrypt(toReplace, keyword):
    """
    keyword 字符替换法  反替换函数
    """
    afterReplace = ''
    keywordList = getKeywordList(keyword)
    for i in toReplace:
        if i.isalpha():
            afterReplace = afterReplace + dereplaceChar(keywordList, i)
        else:
            afterReplace = afterReplace + i
    return afterReplace


if __name__ == '__main__':
    print(encrypt('QCTF{cCgeLdnrIBCX9G1g13KFfeLNsnMRdOwf}', 'lovekfc'))
    print(decrypt('PVSF{vVckHejqBOVX9C1c13GFfkHJrjIQeMwf}', 'lovekfc'))
