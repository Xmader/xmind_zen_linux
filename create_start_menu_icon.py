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

xmind_file = os.path.join(os.getcwd(), "xmind")

xmind_icon = os.path.join(os.getcwd(), "resources", "icon.png")

text = """[Desktop Entry]
Exec={xmind_file}
Name=Xmind
StartupNotify=true
Type=Application
Icon={xmind_icon}
Terminal=false
Categories=Office;
""".format(xmind_file=xmind_file, xmind_icon=xmind_icon)

desktop_file = os.path.join("/usr/share/applications", "xmind.desktop")

with open(desktop_file, "w") as f:
    f.write(text)

os.chmod(desktop_file, stat.S_IRWXU)
