import os 
import copy
print("\033[47;31m\ngive me a txt to convert to html ? \n")
a=input().strip()
b=a
aaa=a.find(".")
if aaa>-1:
    b=copy.copy(a[:aaa])
heads="<html><head><title>$1</title><style>\nbody \n{\n  color: #ff0000;\n}\n</style>\n</head><body><h1>".replace("$1",copy.copy(b))
titles="</h1><h5>"
ends="</h5></body></html>"
b=b+".html"
f1=open(a,"r")
ff=f1.read()
f1.close()
ff=ff.replace("<","«")
ff=ff.replace(">","»")

aaa=ff.find("\n")
tit=ff
if aaa>-1:
    
    tit=ff[:aaa]
    ff=ff[aaa:]
else:
    ff=""

ff=ff.replace("\r\n","<br>")
ff=ff.replace("\n","<br>")
heads=heads+tit+titles
ends=ff+ends
heads=heads+ends
f1=open(b,"w")
f1.write(heads)
f1.close()

