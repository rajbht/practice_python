x = [1,3,5,6,7,8,4,10,12]
y = []
for i in range(len(x)):
    # y.append(x[i],x[i+1])
    # print(y)
    print(x[i])

# for i, element in enumerate(x):
    # print(i, element)


# REVERSE a list

sliced = x[::-1]
print(sliced)


# x.reverse()
# print(x)

y = []

# for i in range(len(x)-1,-1,-1):
#     print(x[i])
#     y.append(x[i])
    
# y.sort(reverse=True)
# print(y)

# SETS -> search / add / remove is faster,  NOT for frequency or order of the items
# cannot contain dup, not ordered or indexed.
x = set()
array = [1,2,3,4,5,6,7,8]
x = set(x for x in array)
print(x)


# s = {} dont use for empty set, you will end up creating dict
# if creating an empty set use contructor x = set() NOT s = {}, as this creates dict

s = {4, 32, 3,3}
print(s)
print(4 in s)

# dict (hashmap or hashtable) -> key/value pair

x = {'name':'mario', 'age' : 4}

for key, value in x.items():
    print(key, value)


# comprehension -> one line intialized of list, tuples.
    
x = [x + 5 for x in range(10)]
print(x)


# x = [[0 for x in range(100) for x in range(5)]]
# print(x)

x = [i for i in range(100) if i % 5 == 0]
print("comprehension")
print(x)

x = tuple(i for i in range(100) if i % 5 == 0)
print(x)

# Functions

def func(x, y):
    return x * y

func(5,6)


# Unpacking
# args / kwargs
# * for list and tuples
# ** for dict

def  func (x, y):
    print(x,y)

pairs = [(1,2), (3,4)]

for pair in pairs:
    func(*pair)

func(**{'x': 2, 'y': 5})


x = [1,34,3244,23423]
print(*x) #unpack
print(x)


def func(*args, **kwargs):
    print(args, kwargs)

func(1,2,3,4,5,one=4,two=1)


# global keyword is not good to use anywhere

# raise & handle exception

# raise Exception('bad')
# raise FileExistsError('')
# x = 7 / 0 -> raises division by zero exception and halts

try:
    x = 7 / 0
except Exception as e:
    print(e)
finally:
    print('finally')




# lambda - one line anonymous function
    
x = lambda x, y: x + y

print(x(2, 15))
    
# map and filter

x = [1,3,4,5,6,6,7,7,8,8,23]

# using lambda
mp = map(lambda i: i*2, x)
print(list(mp))

mp2 = filter(lambda i: i % 2 == 0, x)
print(list(mp2))

# using function
def func(i):
    i = i * 3
    return i % 2 == 0

mp2 = filter(func, x)
print(list(mp2))


# f strings in >python 3.6
y = 8
x = f'hello {6 + 8} {y}'
print(x)
print(f'hello {y}')

# f-string allows you to easily format objects into strings.
# For example, .format once upon a time was common,
name = "jeff"
age = 22
print("{} is {} years old".format(name, age))
# Then came f-strings, where instead of using .format, you can just precede the string with a simple f then, embed the object directly,
print(f"{name} is {age} years old")

