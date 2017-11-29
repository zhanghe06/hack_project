#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: generate.py
@time: 2017/7/18 上午12:29
"""


_numbers = ''.join(map(str, range(10)))                     # 数字
_lower_letter_cases = 'abcdefghijklmnopqrstuvwxyz'          # 小写字母
_upper_letter_cases = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'          # 大写字母
_special_character = '~`!@#$%^&*()_+-={}|[]\\:";\'<>?,./'   # 特殊字符


print(len(_numbers))
print(len(_lower_letter_cases))
print(len(_upper_letter_cases))
print(len(_special_character))

allow_lengths = [4, 6, 8]


def _g_same_char(digit=6, *args):
    init_chars = ''.join(args)
    print init_chars
    init_chars_list = list(init_chars)
    while init_chars_list:
        yield str(init_chars_list.pop())*digit


def _g_4(*args):
    """
    生成组合字符
    :param args:
    :return:
    """
    init_chars = ''.join(args)
    print init_chars
    for i in init_chars:
        for j in init_chars:
            for m in init_chars:
                for n in init_chars:
                    yield '%s%s%s%s' % (i, j, m, n)


def _g_6(*args):
    """
    生成组合字符
    :param args:
    :return:
    """
    init_chars = ''.join(args)
    print init_chars
    for i in init_chars:
        for j in init_chars:
            for m in init_chars:
                for n in init_chars:
                    for p in init_chars:
                        for q in init_chars:
                            yield '%s%s%s%s%s%s' % (i, j, m, n, p, q)


def _g_8(*args):
    """
    生成组合字符
    :param args:
    :return:
    """
    init_chars = ''.join(args)
    print init_chars
    for i in init_chars:
        for j in init_chars:
            for m in init_chars:
                for n in init_chars:
                    for p in init_chars:
                        for q in init_chars:
                            for x in init_chars:
                                for y in init_chars:
                                    yield '%s%s%s%s%s%s%s%s' % (i, j, m, n, p, q, x, y)


def run_captcha(digit=4):
    """
    创建验证码字典
    验证码特点:
        大小写不敏感
        常见 4-6 位
    In [1]: 36**4
    Out[1]: 1679616
    ➜  hack_project wc -l data/captcha_4
     1679616 data/captcha_4
    ➜  hack_project du -h data/captcha_4
    8.0M	data/captcha_4
    :param digit:
    :return:
    """
    if digit not in allow_lengths:
        raise Exception(u'nonsupport')
    # 数字 + 小写字母
    if digit == 8:
        g = _g_8(_numbers, _lower_letter_cases)
    elif digit == 6:
        g = _g_6(_numbers, _lower_letter_cases)
    else:
        g = _g_4(_numbers, _lower_letter_cases)

    data_path = '../data/captcha_%s' % digit
    with open(data_path, 'w') as f:
        for i in g:
            f.write('%s\n' % i)


def run_password_same_char(digit=6):
    """
    相同字符密码
    :param digit:
    :return:
    """
    if digit not in allow_lengths:
        raise Exception(u'nonsupport')
    g = _g_same_char(digit, _numbers, _lower_letter_cases, _upper_letter_cases, _special_character)

    data_path = '../data/password_same_char_%s' % digit
    with open(data_path, 'w') as f:
        for i in g:
            f.write('%s\n' % i)


def run_password_simple(digit=6):
    """
    创建密码字典 - 简单
    密码特点:
        大小写敏感
        最少 6-8 位
    In [1]: (10+26+26)**6
    Out[1]: 56800235584
    ➜  hack_project wc -l data/captcha_4
     1679616 data/captcha_4
    ➜  hack_project du -h data/captcha_4
    8.0M	data/captcha_4
    :param digit:
    :return:
    """
    if digit not in allow_lengths:
        raise Exception(u'nonsupport')
    g = _g_6(_numbers, _lower_letter_cases, _upper_letter_cases)

    data_path = '../data/password_simple_%s' % digit
    with open(data_path, 'w') as f:
        for i in g:
            f.write('%s\n' % i)


def run_password_complex(digit=6):
    """
    创建密码字典 - 复杂
    密码特点:
        大小写敏感
        最少 6-8 位
    In [1]: (10+26+26+32)**6
    Out[1]: 689869781056
    ➜  hack_project wc -l data/captcha_4
     1679616 data/captcha_4
    ➜  hack_project du -h data/captcha_4
    8.0M	data/captcha_4
    :param digit:
    :return:
    """
    if digit not in allow_lengths:
        raise Exception(u'nonsupport')
    g = _g_6(_numbers, _lower_letter_cases, _upper_letter_cases, _special_character)

    data_path = '../data/password_complex_%s' % digit
    with open(data_path, 'w') as f:
        for i in g:
            f.write('%s\n' % i)


if __name__ == '__main__':
    # run_captcha()
    # run_password_same_char(6)
    # run_password_same_char(8)
    run_password_simple(6)
    # run_password_complex()
