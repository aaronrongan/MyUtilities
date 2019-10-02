

#去除文件名中的_,将_换为空格键

import os.path
import pathlib
from os import path, listdir
from pathlib import Path
from glob import glob
import string

sPath='C:/Users/aaron/Documents/MyZoteroFiles_IRF'

lstFilelist=listdir(sPath)

print(lstFilelist)

# for eachfilename in lstFilelist:
    # print(eachfilename)

path1=Path(sPath).iterdir()

# 取得文件夹中的文件名
for eachfile in path1:
    # print(eachfile.name)
    filename=eachfile.stem
    # if len(filename)<9:
    #     print(filename)
    # else:
    #     print(filename)
    # 取得需要的前11位，看是否
    if len(filename)>9:
        needfilename=filename[0:12]
        print(needfilename)
        if(filename[12]==)

    #判断
    # 文件改名
