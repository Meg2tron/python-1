class Stack:
    def __init__(self):
        self.__stack = []
        pass

    def push(self, value):
        self.__stack.append(value)
        pass

    def pop(self):
        return self.__stack.pop()

    def get_stack(self):
        return self.__stack

    def get_top(self):
        return self.__stack[-1]

    pass
