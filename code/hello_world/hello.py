
def say_hello(name = ""):
    if name != "":
        return "Hello, {}!".format(name)
    else:
        return "Hello, World!"
