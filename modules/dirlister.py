import os

def run(**args):
    print("[*] in dirlister mod")
    files = os.listdir(".")
    return str(files)
