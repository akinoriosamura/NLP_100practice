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
    
UKtexts = extract_UK()

# 正規表現
pattern1 = re.compile(r"Category:([^\|]*?)\]\]", flags=(re.MULTILINE))
pattern2 = re.compile(r"Category:(.*)\|", flags=(re.MULTILINE))

# Category list 抽出
results1 = pattern1.findall(UKtexts)
results2 = pattern2.findall(UKtexts)
# print(results1, results2)
results = results1 + results2
# 表示 
for line in results:
    print(line)
