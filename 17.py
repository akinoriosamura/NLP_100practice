# coding: utf-8

import pandas as pd

fname = 'hightemp.txt'
data = pd.read_table(fname, header=None)
udata = data[0].unique()

for text in udata:
    print(text)
