

#去除文件名中的_,将_换为空格键

import os.path
import pathlib
from os import path, listdir
from pathlib import Path
from glob import glob
import string


# sPath='C:/Users/aaron/Documents/MyZoteroFiles_IRF'
sPath='I:/MyZoteroFiles_DHF'
lstFilelist=listdir(sPath)

print(lstFilelist)

# for eachfilename in lstFilelist:
    # print(eachfilename)

path1=Path(sPath).iterdir()

# 取得文件夹中的文件名

count=0
filewholepath=''

for eachfile in path1:
    # print(eachfile.name)
    filename=eachfile.stem

    # if len(filename)<9:
    #     print(filename)
    # else:
    #     print(filename)
    # 取得需要的前11位，看是否
    if count<300:
        if len(filename)>12:
            needfilename=filename[0:13]
            # print(filename)
            if(filename[9]=='_') or (filename[11]=='_'):
                print('correct: ' + filename)
                # 判断
                # 文件改名
                newfilenamelist=str.split(filename,"_",1) #函数里的1表示只分割1次
                newfilename=newfilenamelist[0] + " " +  newfilenamelist[1] + eachfile.suffix
                print(newfilename)
                os.rename(sPath + '/' + filename+eachfile.suffix,sPath + '/' + newfilename)
                count=count+1


