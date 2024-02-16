from icecream import ic
# # using dict
# # O(n) time | O(n) space
def twoNumberSum(array, targetSum):   
    nums = {}
    for i, num in enumerate(array):
        match = targetSum - num
        print(nums)
        if match in nums:
            return [match, num]
        else:
            nums[num] = i  
            print(nums)          
    return []

# # using for loop
# # O(n^2) time | O(1) space
# def twoNumSum(array, targetSum):
#     for i in range(len(array) - 1):
#         firstNum = array[i]
#         for j in range(i+1, len(array)):
#             secNum = array[j]
#             if firstNum + secNum == targetSum:
#                 return [firstNum, secNum]
#     return []

ic(twoNumberSum([3,4,-4,8,1,-1,6,5,9,7], 14))

# ic(twoNumSum([3,5,-4,8,11,1,-1,6,5,9,7], 17)) 


def twoSumIndex(nums, target):
    x = {}
    for i, num in enumerate(nums):
        match = target - num
        if match in x:
            # print(i)
            return [x[match], i]
        else: 
            x[num] = i
            print(x)

    return []
           

ic(twoSumIndex([3,3],6))
ic(twoSumIndex([2,7,5,6],9))
