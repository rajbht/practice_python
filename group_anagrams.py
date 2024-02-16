from collections import defaultdict
from icecream import ic 

def groupAnagrams(strs):

    # x = defaultdict(list) if you using defaultDict , no need to check if/else
    x = {}
    for s in strs:
        # sort the chars in s
        sorted_s = "".join(sorted(s))
        ic(sorted_s)
        ic(x)
        if sorted_s not in x:         
            x[sorted_s] = [s]
            ic(x)
        else:
            print(s)
            x[sorted_s].append(s)
            ic(x)
    
    return x.values()


# ic(groupAnagrams([""]))
# ic(groupAnagrams(["a"]))
ic(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))