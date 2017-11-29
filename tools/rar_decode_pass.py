#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: rar_decode_pass.py
@time: 2017/7/18 下午2:15
"""

import os
import sys
import zipfile

from unrar import rarfile


def decrypt_rar_zip_file(file_name):
    # 根据文件扩展名，使用不同的库
    if file_name.endswith('.zip'):
        fp = zipfile.ZipFile(file_name)
    elif file_name.endswith('.rar'):
        fp = rarfile.RarFile(file_name)
    else:
        fp = None
    # 解压缩的目标文件夹
    des_path = file_name[:-4]
    if not os.path.exists(des_path):
        os.mkdir(des_path)
    # 先尝试不用密码解压缩，如果成功则表示压缩文件没有密码

    try:

        fp.extractall(des_path)
        fp.close()
        print('No password')
        return

    # 使用密码字典进行暴力破解
    except:
        try:
            # fp_pwd = open('pwddict.txt')
            fp_pwd = open('/Users/zhanghe/code/hack_project/data/password_same_char_6')
        except:
            print('No dict file pwddict.txt in current directory.')
            return
        for pwd in fp_pwd:
            pwd = pwd.rstrip()
            try:
                if file_name.endswith('.zip'):
                    for file in fp.namelist():
                        # 对zip文件需要重新编码再解码，避免中文乱码
                        fp.extract(file, path=des_path, pwd=pwd.encode())
                        os.rename(des_path + '\\' + file, des_path + '\\' + file.encode('cp437').decode('gbk'))
                    print('Success! ====>' + pwd)
                    fp.close()
                    break
                elif file_name.endswith('.rar'):
                    fp.extractall(path=des_path, pwd=pwd)
                    print('Success! ====>' + pwd)
                    fp.close()
                    break
            except:
                pass
        fp_pwd.close()


if __name__ == '__main__':
    filename = sys.argv[1]
    if os.path.isfile(filename) and filename.endswith(('.zip', '.rar')):
        decrypt_rar_zip_file(filename)
    else:
        print('Must be Rar or Zip file')


"""
https://github.com/matiasb/python-unrar

非windows环境

http://www.rarsoft.com/download.htm


Mac 环境
wget -c https://www.rarlab.com/rar/rarosx-5.5.0.tar.gz
tar -xvf rarosx-5.5.0.tar.gz
cd rar
sudo install -c -o $USER rar /usr/local/bin
sudo install -c -o $USER unrar /usr/local/bin


$ wget -c https://www.rarlab.com/rar/unrarsrc-5.5.8.tar.gz
$ tar -xvf unrarsrc-5.5.8.tar.gz
$ cd unrar
$ make lib
$ make install-lib
"""
