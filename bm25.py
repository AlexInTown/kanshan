import math

def bm25(q, d, df, k1=2, k2=1.):
    score = 0.0
    K = k1 * (1 - b + b*len(d)/avgdl)
    for w in q:
        s = d[w] * (k1+1) / (d[w] + k1 *(1-b))
        s *= 1.0 / math.log(df[w] + 1) * d[w]
        score += s
    pass

