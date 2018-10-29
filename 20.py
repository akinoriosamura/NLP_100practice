# coding: utf-8

import gzip
import json

fname = 'jawiki-country.json.gz'

with gzip.open(fname, "rt", "utf-8") as f:
    for line in f:
        djson = json.loads(line)
        if djson["title"] == "イギリス":
            print(djson["text"])
            break
