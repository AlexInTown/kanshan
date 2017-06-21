import math


def norm2(a):
    res = 0.0
    for k,v in a.items():
        res += v * v
    return math.sqrt(res)


def cosine(a, b):
    """
    Calculate cosine similarity of dict a and dict b.
    :param a:
    :param b:
    :return:
    """
    na = norm2(a)
    nb = norm2(b)
    if na == 0 or nb == 0:
        return 0.0
    c = 0.0
    for k,v in a.items():
        if k in b:
            c += v * b[k]
    return c / na / nb


