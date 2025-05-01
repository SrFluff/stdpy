logA = []
def log(msg="Logged with no message"):
    global logA
    logA.append("[AUTO]:"+msg)
def clog():
    global logA
    logA = []
def fetch():
    return "\n".join(logA)
