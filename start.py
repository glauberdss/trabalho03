#coding: utf8

import os
import commands

for i in range(1,13):
    if i< 10 :
       grupo = "grupo0"+str(i)
    else:
       grupo = "grupo"+str(i)
    print grupo
