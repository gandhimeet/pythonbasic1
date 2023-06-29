'''
Write a Python program to list all files in a directory.
'''
#importing list dir from os 
from os import listdir
#importing isfile and join from os.path
from os.path import isfile,join
#fileslist consist of file in the directory
fileslist = [f for f in listdir('D:\pythonbasic1') if isfile(join('D:\pythonbasic1',f))]
#displying the fileslist consist of all files in the directory.
print(fileslist)