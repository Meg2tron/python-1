import os

files = []

# making list of test files
for path, subdirs, Files in os.walk("code"):
    for F in Files:
        if "test" in F:
            files.append(os.path.join(path ,F))

# running test files
for file in files:
    print("Testing : {}".format(file))
    os.system("python {}".format(file))
