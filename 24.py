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
        \[\[File|ファイル
        :
        (.+?)
        \|
        ''', flags=(re.VERBOSE))

# 抽出
results = pattern.findall(UKtexts)

# 表示
# print(results)
for l in results:
    print(l)

