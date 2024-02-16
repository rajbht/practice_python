from icecream import ic

# using slice
# Time Complexity: O(n), where n is the length of the string
# Auxiliary Space: O(1)
def isPalindrome(string):
    rev = string[::-1]
    if ic(string == rev):  
        return True
    else:
        return False

# using list iteration 
def isPalindrome1(string):
    s = list(string)
    rev = ''
    for i in range(len(s)-1,-1,-1):
        rev += s[i]
    if rev == string:
        return True
    else:
        return False
        

# using reverse function
# Time complexity: O(n)
# Auxiliary Space: O(n)
def isPalindrome2(string):
    rev = ''.join(reversed(string))
    
    if rev == string:
        return True
    else:
        return False
        

# using recusion

def isPalindrome3(string):
    s = string.lower()
    l = len(s)

    if l < 2:
        return True
    elif s[0] == s[l-1]:
        return isPalindrome3(s[1:l-1])
    else: 
        return False
    

# ic(isPalindrome3("palindrome"))
# ic(isPalindrome3("ab"))
# ic(isPalindrome3("abcdcba"))
# ic(isPalindrome3("abcdefghihgfedcba"))

def isPalindromeNum(x):
    string = str(x)
    rev = string[::-1]
    if ic(string == rev):  
        return True
    else:
        return False
    
def isPalindromeNum1(x):   
    x = str(x)
    return x == x[::-1]
    

def isPalindromeNum2(x):

    if x < 0 or (x > 0 and x%10 == 0):   # if x is negative, return False. 
        print(x)
        return False                     #  if x is positive and last digit is 0, that also cannot form a palindrome, return False.
	
    temp = x
    rev_num = 0	
    while temp > 0:
        digit = temp % 10
        rev_num = rev_num * 10 + digit
        temp //= 10 # manipulating temp
	
    return x == rev_num # only match with x NOT temp


ic(isPalindromeNum2(1001))
ic(isPalindromeNum2(-121))
ic(isPalindromeNum2(10))
