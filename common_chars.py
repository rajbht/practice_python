from icecream import ic 
from collections import Counter  


def commonChar(words):
    res = []
    for i in words[0]:
        if all([i in w for w in words]):
            for s in range(len(words)):
                words[s] = words[s].replace(i, "",1)
            res.append(i)                
    return res

# ic(commonChar(["cool","cook","lock"]))
# ic(commonChar(["bella","label","roller"]))


def commonChar2(words):
    dict1 = words[0]
    for i in range(1, len(words)):
        ic(words[i])
        ic(Counter(dict1))
        ic(Counter(words[i]))
        dict1 = Counter(dict1) & Counter(words[i])
    return list(dict1.elements())

ic(commonChar2(["cool","cook","lock"]))
ic(commonChar2(["bella","label","roller"]))