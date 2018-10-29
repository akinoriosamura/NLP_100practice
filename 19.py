# coding: utf-8

import pandas as pd

fname = 'hightemp.txt'
data = pd.read_table(fname, header=None)
udata = data[0].unique()
ucounts = {}
clist = []
for utext in udata:
    ucounts[utext] = data[0].value_counts()[utext]

for text in data[0]:
    clist.append(ucounts[text])
# print(clist)

data["counts"] = clist
# print(data)
sdata = data.sort_values("counts", ascending=False)
sdata = sdata.drop("counts", axis=1)
print(sdata)
