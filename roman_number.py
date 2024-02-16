from icecream import ic
def romanToInt(s):

    if (len(s) < 1 or len(s) > 15):
        return None

    r_dict = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000
    }

    print(r_dict)
    
    result = 0
    prev = 0
    for s in s[::-1]:
        # print(r_dict[s])
    
        if r_dict[s] >= prev:  
            result += r_dict[s]    
        else:
            result -= r_dict[s]
        prev = r_dict[s]
    return result


ic(romanToInt("LVIII"))
ic(romanToInt("III"))
ic(romanToInt("MCMXCIV"))


def romanToInt2(s):
    translations = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    number = 0
    s = s.replace("IV", "IIII").replace("IX", "VIIII")
    s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
    s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
    for char in s:
        number += translations[char]
    return number


# ic(romanToInt2("LVIII"))
# ic(romanToInt2("III"))
# ic(romanToInt2("MCMXCIV"))