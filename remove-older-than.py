import os,time

path = "/home/ftpuser/home/ftpuser/FI9853EP_00626E680A2C/record"
now  = time.time()
dni  = 30



for filename in os.listdir(path):
    filestamp= os.stat(os.path.join(path,filename)).st_mtime
    filecompare=now - dni * 86400
    if filestamp < filecompare:
        print(filename)
        file_with_path=path+'/'+filename
        print(file_with_path)
        if os.path.isfile(file_with_path)==True:
            print(file_with_path)
            os.remove(file_with_path)
        else:
            print("This is a directory =>" + file_with_path)
