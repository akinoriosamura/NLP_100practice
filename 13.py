# coding: utf-8

fname = 'cols.txt'
path1 = "cols1.txt"
path2 = "cols2.txt"
col = ""

with open(path1) as cols1_f, \
        open(path2) as cols2_f, \
        open(fname, mode="w") as f:
            col1 = cols1_f.readlines()
            col2 = cols2_f.readlines()
            for (c1, c2) in zip(col1, col2):
                nc1 = c1.replace("\n", "\t")
                c = nc1 + c2
                col += c
print(col)
