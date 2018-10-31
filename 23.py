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
        (={2,}) # =を二回以上
        \s* # 空白
        (.*?) # 文字列。非貪欲なので以降の正規表現条件に合えば解除
        \s* # 空白
        \1 # グループの後方参照
        .*
        $ # 行末
        ''', flags=(re.MULTILINE + re.VERBOSE))

# 抽出
results = pattern.findall(UKtexts)

# 表示
# print(results)
for l in results:
    # count section num
    seclen = len(l[0])
    print(seclen, l[1])

