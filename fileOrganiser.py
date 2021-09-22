import os
import shutil
path = 'C:/Users/sarav/Desktop/python/c-99/test1'
list_of_files = os.listdir(path)
print(list_of_files)
for file in list_of_files:
    name, ext = os.path.splitext(file)
    print(name+'--'+ext)
    ext = ext[1:]
    print(ext)
    if ext == '':
        continue
    if os.path.exists(path+'/'+ext):
        shutil.move(path+'/'+file,path+'/'+ext+'/'+file)
    else:
        os.makedirs(path+'/'+ext)
        shutil.move(path+'/'+file,path+'/'+ext+'/'+file)