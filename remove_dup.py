from icecream import ic 

def removeDuplicates(nums):
 
    l = set(nums)  
    expectedNums = list(nums)

    k = len(expectedNums)
    stop = len(l)
    for i in range(k,stop):
        expectedNums.append("_")        

    return k, expectedNums



def rmdups(nums):
    nums[:] = sorted(set(nums))
    return len(nums), nums

ic(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))

ic(rmdups([0,0,1,1,1,2,2,3,3,4]))