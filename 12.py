# coding: utf-8

fname = 'hightemp.txt'
path1 = "cols1.txt"
path2 = "cols2.txt"
with open(fname) as f, \
        open(path1, mode="w") as cols1_f, \
        open(path2, mode="w") as cols2_f:
            # print(f)
            for line in f:
                # print(line)
                text = line.split("\t")
                cols1_f.write(text[0] + "\n")
                cols2_f.write(text[1] + "\n")
print(text[0])
print(text[1])
