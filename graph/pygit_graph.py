# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from subprocess import PIPE, Popen
import os

def cmdline(command):
    """
    コマンドを実行する。shell=Trueの場合シェル経由で実行する。
    :param command: str
    :return: Popen
    """
    return Popen(
        args=command,
        stdout=PIPE,
        stderr=PIPE,
        shell=True
    )


os.chdir('../')

# 標準出力
print '標準出力:' + cmdline('ls').stdout.readline()

lines = cmdline('git status').stdout.readlines()

for line in lines:
    print line