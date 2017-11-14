
def check_lapindrome(string):
    # getting string length and initialising spliting indeces
    length = len(string)
    mid = length // 2
    delim = mid

    # checking if string is having odd length or not
    if length % 2 != 0: delim += 1

    # spliting strings
    first = string[:mid]
    second = string[delim:]

    # sorting strings and joining
    first = "".join(sorted(list(first)))
    second = "".join(sorted(list(second)))

    # returns true if string is lapindrome else false
    return first == second
