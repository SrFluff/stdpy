import os

def cls():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def log(msg):
    if os.path.exists("log.txt"):
        f = open("log.txt","a")
        f.write("[AUTO]:" + msg + "\n")
        f.close()
    else:
        f = open("log.txt","w")
        f.close()
        f = open("log.txt","a")
        f.write("[AUTO]:" + msg + "\n")
        f.close()
