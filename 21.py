# coding: utf-8

import gzip
import json

fname = 'jawiki-country.json.gz'

def extract_UK():
    with gzip.open(fname, "rt", "utf-8") as f:
        for line in f:
            djson = json.loads(line)
            if djson["title"] == "イギリス":
                return djson["text"]
    raise ValueError("there is no UK")
    
UKtexts = extract_UK()
Blist = UKtexts.split("\n")
Clist = [l for l in Blist if "Category" in l]
print("\n".join(Clist))
