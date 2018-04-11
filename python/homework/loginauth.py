#/usr/bin/env python
# -*- coding: utf-8 -*

"this is a login auth module"


import os
import sys


WORKDIR = os.path.split(os.path.realpath(__file__))[0]
PASSFILEPATH = os.path.join(WORKDIR, 'user.password')
LOCKFILEPATH = os.path.join(WORKDIR, 'user.lock')


def main():
    NUM = 0
    username = input('请输入您的用户名：')
    userpasslist = open(PASSFILEPATH,'r').readlines()
    userpasslist = [line.replace('\n','') for line in userpasslist]
    userlist = [line.split(':')[0].replace('\n','') for line in userpasslist]

    if os.path.isfile(LOCKFILEPATH):
        locklist = open(LOCKFILEPATH,'r').readlines()
        locklist = [line.replace('\n', '') for line in locklist]
        if username in locklist:
            sys.exit("您的账号处于被锁状态，不能登陆")

    if not username in userlist:
        sys.exit('此用户不存，请检查用户表！')

    for i in range(3):
        password = input('请输入您的密码：')
        userpass = "%s:%s" % (username, password)
        if userpass in userpasslist:
            print('欢迎%s登陆' %username)
            return
        else:
            print('您输入的密码有误，请重新输入')

        NUM += 1

    if NUM == 3:
        print("您输入的密码错误累积3次，账号被锁定")
        with open(LOCKFILEPATH, 'a') as f:
            f.write(username + '\n')


if __name__ == '__main__':
    main()