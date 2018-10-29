# coding: utf-8

import pandas as pd

fname = 'hightemp.txt'
data = pd.read_table(fname, header=None)
data[2] = data[2].sort_values(ascending=False)
print(data)
