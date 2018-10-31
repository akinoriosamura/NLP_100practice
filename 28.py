# coding: utf-8

import gzip
import json
import re
import urllib.request

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

# get dictionary
tempdict = {}
for l in results:
    # delte markup.
    delkey = re.sub(r"\'{2,5}", "", l[0])
    delvalue = re.sub(r"\'{2,5}", "", l[1])

    # delte link markup.
    delkey = re.sub(r"\[\[|\]\]", "", delkey)
    delvalue = re.sub(r"\[\[|\]\]", "", delvalue)
    tempdict[delkey] = delvalue

# get the url file name
keyfield = tempdict["国旗画像"][1:]
url = "https://www.mediawiki.org/w/api.php?" \
        + "action=query&" \
        + "titles=File:" + urllib.parse.quote(keyfield) + "&" \
        + "prop=imageinfo&" \
        + "format=json&" \
        + "iiprop=url"
request = urllib.request.Request(url,
        headers={"User-Agent" : "NLP"}
        )
res = urllib.request.urlopen(request)
print(res)
body = json.loads(res.read().decode("utf-8"))

# extract image url
imageurl = body["query"]["pages"]["-1"]["imageinfo"][0]["url"]
print(imageurl)
