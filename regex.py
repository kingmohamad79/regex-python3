import re


with open(file=r'C:\Users\User\Desktop\regex in python\text.txt', mode='r+') as read :
    z = read.read()
    x = re.sub(pattern='\s*d[a-z]{3}r\s*',repl=' king ',string=z)
    read.write(x)