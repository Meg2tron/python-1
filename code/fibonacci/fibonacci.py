
def get_series(limit):
    fibs = [0, 1, 1]
    for f in range(2, limit):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs
