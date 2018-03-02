from cx_Freeze import setup, Executable
import os
import sys
des = input("С консолью или без(+ или -): ")
if des=='-':
    base='Win32GUI'
else:
    base = None

os.environ['TCL_LIBRARY'] = r'C:\Program Files\Python36\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Program Files\Python36\tcl\tk8.6'
setup(
    name = input("Название .exe: "),
    version = input("Версия: "),
    description = input("Описание: "),
    author = input("Автор: "),
    executables = [Executable(input("Файл(перетащи сюда) "), base=base)]
)
