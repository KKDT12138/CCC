import os

def run(**args):
    printf("[*] in dirlister mod")
    files = os.listdir(".")
    return str(files)