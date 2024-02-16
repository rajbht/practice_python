from icecream import ic 

def longCommonPrefix(strs):
    
    if len(strs) == 0:
        return ""
    
    prefix = strs[0]

    for string in strs[1:]:
        while string.find(prefix) != 0:
            ic(string.find(prefix))
            prefix = prefix[:-1]
            ic(prefix[:-1])
            if not prefix:
                return ""
    return prefix

def longCommonPrefix1(strs):

    if len(strs) == 0:
        return ""
    
    prefix = strs[0]
    res = ""
    for i in range(len(prefix)):
        for word in strs[1:]:
            ic(word[i], prefix[i])  
            if i == len(word) or word[i] != prefix[i]:
                ic(word[i], prefix[i])                
                return prefix[0:i]
    
    return res


ic(longCommonPrefix1(["flower","flow","flight"]))
ic(longCommonPrefix1(["dog","racecar","car"]))