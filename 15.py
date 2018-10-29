# coding: utf-8

fname = 'hightemp.txt'

with open(fname) as f:
    texts = f.readlines()
    print("please input number less than ", len(texts))
    N = int(input())
    if N > len(texts):
        print("please input number less than ", len(texts))
        N = int(input())
    for text in texts[-N:]:
        print(text.rstrip())

        

