""" MylfVentus (c) 2020 """
import os
import fnmatch
from tkinter import *
from tkinter import filedialog, ttk

def input_folder():
    directory = filedialog.askdirectory()
    if not directory:
        return 0
    return directory

def iterfindfiles( path, fnexp):
    for root, dirs, files in os.walk(path):
        for filename in fnmatch.filter(files, fnexp):
            yield os.path.join(root, filename)

def rename( path, newextension):
    (filepath, tempfilename) = os.path.split(path)
    (filename, extension) = os.path.splitext(tempfilename)
    filepn=filepath+os.sep+filename
    os.rename(path,filepn+newextension)

def gethead( path):
    with open(path,"rb") as f:
        binstr = (f.read())[:40]
        return binstr

def change( path):
    with open(path,"rb") as f:
        binstr = (f.read())[2:]
    with open(path,"rb+") as f:
        f.write(binstr)

if __name__ == '__main__':
    root = Tk()
    root.title(" ")
    root.overrideredirect(True)
    root.geometry('0x0')
    path=input_folder()
    for filename in iterfindfiles(path, "*.ndf"):
        head = gethead(filename)
        if ((str(head)).find(("mp4"))!=-1):
            print ("找到文件：     "+filename+"     \033[0;32m[视频]\033[0m")
            change(filename)
            rename(filename,".mp4")
        elif((str(head)).find(("PNG"))!=-1):
            print ("找到文件：     "+filename+"     \033[0;32m[图片]\033[0m")
            rename(filename,".png")
        else:
            print ("找到文件：     "+filename+"     \033[0;31m[未知类型]\033[0m")