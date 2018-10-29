# coding: utf-8

fname = 'hightemp.txt'
with open(fname) as f:
    texts = f.read()
    tabtexts = texts.replace("\t", " ")
print(tabtexts)
