#!/usr/bin/env python
# -*- coding: utf-8 -*-
import commands
import os
import stat
import sys

if os.path.isdir(sys.argv[0]):
    os.chdir(sys.argv[0])
elif os.path.isfile(sys.argv[0]):
    os.chdir(os.path.dirname(sys.argv[0]))

home = os.environ["HOME"]  # 获取家目录地址

xmind_file = os.path.join(os.getcwd(), "xmind")

xmind_icon = os.path.join(os.getcwd(), "resources", "icon.png")

text = """[Desktop Entry]
Exec={xmind_file}
Name=Xmind
StartupNotify=true
Type=Application
Icon={xmind_icon}
Categories=Application;Office""".format(xmind_file=xmind_file, xmind_icon=xmind_icon)


# print os.path.exists(os.path.join(home,"Desktop"))
# print os.path.exists(os.path.join(home,u"桌面"))
if os.path.exists(os.path.join(home, u"桌面")):
    desktop_dir = os.path.join(home, u"桌面")
else:
    desktop_dir = os.path.join(home, "Desktop")

desktop_file = os.path.join(desktop_dir, "xmind.desktop")

with open(desktop_file, "w") as f:
    f.write(text)

os.chmod(desktop_file, stat.S_IRWXU)
