
def check_palindrome(string):
    # getting string length and initialising spliting indeces
    length = len(string)
    mid = length // 2
    delim = mid

    # checking if string is having odd length or not
    if length % 2 != 0: delim += 1

    # spliting strings
    first = string[:mid]
    second = string[delim:]

    # getting last value of second string
    last = len(second) - 1

    # traversing first from L -> R and second from R -> L
    for x in range(len(first)):
        # return false on any non relevant character
        if first[x] != second[last]: return False
        # decrease the iterator for second by 1
        last -=1
    return True
