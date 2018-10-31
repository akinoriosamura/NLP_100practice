# coding: utf-8

import gzip
import json
import re

fname = 'jawiki-country.json.gz'

def extract_UK():
    with gzip.open(fname, "rt", "utf-8") as f:
        for line in f:
            djson = json.loads(line)
            if djson["title"] == "イギリス":
                return djson["text"]
    raise ValueError("there is no UK")
    
# extract wiki texts
UKtexts = extract_UK()
# print(UKtexts)

# 正規表現
pattern = re.compile(r'''
        ^ # 行頭
        \|
        (.+?) # =を二回以上
        \s # 空白
        =
        (.*)
        $ # 行末
        ''', flags=(re.MULTILINE + re.VERBOSE))

# 抽出
results = pattern.findall(UKtexts)
tempdict = {}
# 表示
# print(results)
for l in results:
    # delte markup.
    delkey = re.sub(r"\'{2,5}", "", l[0])
    delvalue = re.sub(r"\'{2,5}", "", l[1])

    # delte link markup.
    delkey = re.sub(r"\[\[|\]\]", "", delkey)
    delvalue = re.sub(r"\[\[|\]\]", "", delvalue)
    tempdict[delkey] = delvalue

print(tempdict)
