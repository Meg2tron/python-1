import os
code = 0
for path, subdirs, files in os.walk("code"):
    for name in files:
        if "test" in name:
            os.chdir(path)
            s = os.system("python test.py")
            os.chdir("../../")
            if s != 0:
                code = 1
os._exit(code)
