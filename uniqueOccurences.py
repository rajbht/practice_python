from collections import Counter
from icecream import ic 

def uniqueOccurrences(arr):

    c_dict = Counter(arr)

    x = list(c_dict.values())

    for i in x:
        if x.count(i) > 1:
            return False  
        else:
            return True




ic(uniqueOccurrences([1,2,2,1,1,3]))