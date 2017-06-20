import numpy as np


def get_char_embeddings():
    c2v = dict()
    with open("data/char_embedding.txt") as f:
        first = f.readline()
        cnum, d = first.rstrip(" \r\n").split()
        print("- Reading {} char embeddings of dim {}".format(cnum, d))
        for line in f:
            strs = line.rstrip(" \r\n").split()
            k = strs[0]
            v = [float(x) for x in strs[1:]]
            c2v[k] = np.asarray(v)
        print("- Done.")
    return c2v


def get_word_embeddings():
    w2v = dict()
    with open("data/word_embedding.txt") as f:
        first = f.readline()
        cnum, d = first.rstrip(" \r\n").split()
        print("- Reading {} word embeddings of dim {}".format(cnum, d))
        for line in f:
            strs = line.rstrip(" \r\n").split()
            k = strs[0]
            v = [float(x) for x in strs[1:]]
            w2v[k] = np.asarray(v)
        print("- Done.")
    return w2v
    

if __name__ == "__main__":
    c2v = get_char_embeddings()
    w2v = get_word_embeddings()
    pass
