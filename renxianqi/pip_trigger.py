#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/10/17 11:49 下午
# @Author : LeiXueWei
# @CSDN/Juejin/Wechat: 雷学委
# @XueWeiTag: CodingDemo
# @File : pip_trigger.py
# @Project : renxianqi(aka qingdian)

from renxianqi.setting import NAME


def install_win32():
    from pip._internal import main
    main(['install', 'pypiwin32'])


def upgrade():
    from pip._internal import main
    main(['install', '--user', '--upgrade', NAME])


if __name__ == '__main__':
    upgrade()
