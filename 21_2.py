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
pattern = re.compile(r'''
        ^ # 行頭
        ( # キャプチャ対象のグループ開始
        .* # 任意の文字0文字以上
        \[\[Category:
        .*
        \]\]
        .*
        )
        $
        ''', flags=(re.MULTILINE | re.VERBOSE))

# 抽出
results =  pattern.findall(UKtexts)

# 表示 
for line in results:
    print(line)
