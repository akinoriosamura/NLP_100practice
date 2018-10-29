# coding: utf-8

fname = 'hightemp.txt'

with open(fname) as f:
    texts = f.readlines()
    print("please input number less than ", len(texts))
    N = int(input())
    if N > len(texts):
        print("please input number less than ", len(texts))
        N = int(input())
    for i in range(0, len(texts), N):
        # print(texts[i:N+i])
        ctexts = [text.rstrip() for text in texts[i:N+i]]
        ntexts = "\n".join(ctexts)
        print(ntexts)
        newf = "file" + str(i) + ".txt"
        with open(newf, mode="w") as nf:
            nf.write(ntexts)
