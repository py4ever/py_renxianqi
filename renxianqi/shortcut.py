#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/10/10 8:30 下午
# @Author : LeiXueWei
# @CSDN/Juejin/Wechat: 雷学委
# @XueWeiTag: CodingDemo
# @File : shortcut.py
# @Project : renxianqi(aka qingdian)


import os

from renxianqi.pip_trigger import install_win32


def create_shortcut(bin_path: str, name: str, desc: str):
    try:
        do_create(bin_path, desc, name)
        return True
    except ImportError as err:
        print("error detail %s" % str(err))
        if "No module named 'win32con'" in str(err):
            install_win32()
            do_create(bin_path, desc, name)
        else:
            print("Well, do nothing as 'winshell' lib may not available on current os")
    return False


def do_create(bin_path, desc, name):
    import winshell
    shortcut = os.path.join(winshell.desktop(), name + ".lnk")
    winshell.CreateShortcut(
        Path=shortcut,
        Target=bin_path,
        Icon=(bin_path, 0),
        Description=desc
    )


if __name__ == "__main__":
    create_shortcut("/Library/Frameworks/Python.framework/Versions/3.8/bin/rxq.exe", "RenXianQi", "清点小程序")
