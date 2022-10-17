import os
from Cython.Build.BuildExecutable import build
file = input(' Put file:  ')

ex = file.split('.')[0]
build(file)

os.system('strip -s '+ex)
os.system('termux-elf-cleaner '+ex)
os.system(f'rm -rf {ex}.c {ex}.o && mv {ex} /sdcard')
print(' File stored in /sdcard/'+ex)
