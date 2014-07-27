Python 2.7.2 (default, Jun 12 2011, 14:24:46) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> open("yeni dosyam","w")
<open file 'yeni dosyam', mode 'w' at 0x0000000002FF4420>
>>> import os
>>> os.rmdir("yeni dosyam")

Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    os.rmdir("yeni dosyam")
WindowsError: [Error 267] Dizin adý geçersiz: 'yeni dosyam'
>>> os.rmdir("/yeni dosyam/")

Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    os.rmdir("/yeni dosyam/")
WindowsError: [Error 2] Sistem belirtilen dosyayý bulamýyor: '/yeni dosyam/'
>>> open("yeni dosyamm.txt","w")
<open file 'yeni dosyamm.txt', mode 'w' at 0x0000000002FF4540>
>>> dosya=open("belgem.odt","w")
>>> dosya.write("guýdo van rossum")
>>> dosya.close()
>>> import os
>>> os.listdir(os.getcwd)

Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    os.listdir(os.getcwd)
TypeError: coercing to Unicode: need string or buffer, builtin_function_or_method found
>>> ost.getcwd()

Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    ost.getcwd()
NameError: name 'ost' is not defined
>>> os.getcwd()
'C:\\Python27'
>>> os.listdir(os.curdir)
['asal.py', 'belgem.odt', 'DLLs', 'Doc', 'getcwd.py', 'include', 'Lib', 'libs', 'LICENSE.txt', 'listdir.py', 'name.py', 'NEWS.txt', 'python.exe', 'pythonw.exe', 'README.txt', 'tcl', 'Tools', 'yeni dosyam', 'yeni dosyamm.txt']
>>> os.open("/belgem.odt/")

Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    os.open("/belgem.odt/")
TypeError: function takes at least 2 arguments (1 given)
>>> os.chdir("/belgem")

Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    os.chdir("/belgem")
WindowsError: [Error 2] Sistem belirtilen dosyayý bulamýyor: '/belgem'
>>> os.chdir("/belgem/")

Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    os.chdir("/belgem/")
WindowsError: [Error 2] Sistem belirtilen dosyayý bulamýyor: '/belgem/'
>>> os.chdir("/belgem.odt/")

Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    os.chdir("/belgem.odt/")
WindowsError: [Error 2] Sistem belirtilen dosyayý bulamýyor: '/belgem.odt/'
>>> os.listdir(os.curdir)
['asal.py', 'belgem.odt', 'DLLs', 'Doc', 'getcwd.py', 'include', 'Lib', 'libs', 'LICENSE.txt', 'listdir.py', 'name.py', 'NEWS.txt', 'python.exe', 'pythonw.exe', 'README.txt', 'tcl', 'Tools', 'yeni dosyam', 'yeni dosyamm.txt']
>>> a = os.listdir(os.curdir)
>>> for s, d in enumerate(a, 1):
	print s, d
	
