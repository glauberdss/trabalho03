#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import os.path
import commands
import subprocess
import signal
import sys


def start():
    # Listar entradas y meterlas en "files"
    files = os.listdir('.')
    for j in range(len(files)):
	# Si es un directorio
	if (os.path.isdir(files[j])) and (not files[j].startswith('.')):
		nomepasta = "python "+files[j]+"/server.py &"
		os.popen(nomepasta)


def killp():

    p = subprocess.Popen(['ps', '-ax'], stdout=subprocess.PIPE)
    out, err = p.communicate()

    for line in out.splitlines():
        if 'python grupo' in line:
            pid = int(line.split(None, 1)[0])
            os.kill(pid, signal.SIGKILL)


if (sys.argv[1] == "kill"):
    killp()
elif(sys.argv[1] == "start"):
    start()
else: #restart
    killp()
    start()

