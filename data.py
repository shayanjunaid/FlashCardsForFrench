from pandas import *

try:
    data = read_csv("words_to_learn.csv")
except FileNotFoundError:
    data = read_csv("French_words.csv")
finally:
    words = data.to_dict()
    used_words = []
