import math
from collections import defaultdict


def get_df():
    char_df = defaultdict(int)
    word_df = defaultdict(int)
    with open('data/question_train_set.txt') as f:
        for line in f:
            strs = line.rstrip(' \r\n').split()
            chars = set(strs[1].split(','))
            chars.update(strs[3].split(','))
            words = set(strs[2].split(','))
            words.update(strs[4].split(','))
            for c in chars:
                char_df[c] += 1
            for w in words:
                word_df[w] += 1
    return char_df, word_df


def get_tf_idf(bow, df):
    res = defaultdict(float)
    for w in bow:
        res[w] += 1.0 / math.log(df[w] + 1)
    return res









