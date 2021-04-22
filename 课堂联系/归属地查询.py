import os.path
spath = " D:/download/repository.7z"
p,f = os.path.split(spath);
print ( " diris: " + p)
print ( " fileis: " + f.split(".")[0])
drv,left = os.path.splitdrive(spath);
print ( " driveris: " + drv)
print ( " leftis: " + left)
f,ext = os.path.splitext(spath);
print ( " fis: " + f)
print ( " extis: " + ext)
