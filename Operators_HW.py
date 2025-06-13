# Arithmetic Operators -> Used to perform some mathmetical computations 

str="Insta"
str1="gram"
print(str+str1)   # Concatination

print(str*3)      # InstaInstaInsta

# Performing Arithmetic operations on list
# NOTE -> We cannot perform (-,/,//) Operations on list,it will throw -> (TypeError: unsupported operand type(s) for %: 'list' and 'list')

l1=[2,40,6,9,57]
l2=[3,65,8,10,50]
print(l1+l2)      # [2, 40, 6, 9, 57, 3, 65, 8, 10, 50] # Adds list2 at end of list1

print(l1*2)       # [2, 40, 6, 9, 57, 2, 40, 6, 9, 57]

print(l2*3)       # [3, 65, 8, 10, 50, 3, 65, 8, 10, 50, 3, 65, 8, 10, 50]

# Performing Arithmetic Operations on Tuple

t1=(1,4,7,8,10)
t2=(10,6,5,2,3)
t3=([3,65,8,10,50])

print(t1+t2)       # (1, 4, 7, 8, 10, 10, 6, 5, 2, 3)
print(t1*2)        # (1, 4, 7, 8, 10, 1, 4, 7, 8, 10)
print(t2*4)        # (10, 6, 5, 2, 3, 10, 6, 5, 2, 3, 10, 6, 5, 2, 3, 10, 6, 5, 2, 3)

# performing Arithmetic Operations on set

s1={20,5,6,79,30}
s2={10,6,5,2,3}       # 10,56,40,20,5

print(s1+s2)         # Throws error -> TypeError: unsupported operand type(s) for +: 'set' and 'set'
print(s1-s2)         # {79, 6, 30}
print(s2-s1)         # {56, 40, 10}

# Dictionary

dict1={101:"Manasi",102:"Shraddha",103:"Sanjana"}
dict2={110:"Arya",112:"Tejas",113:"Anushka"}

# print(type(dict1),dict1)
# print(dict1+dict2)         # Throws Error -> TypeError: unsupported operand type(s) for +: 'dict' and 'dict'


# Using Arithmetic operators with different datatypes
# print(l1+t1)           # TypeError: can only concatenate list (not "tuple") to list
# print(l2+s1)

# Using Special Operators

print(t1 in s1)
print(t2 in s2)

print(t1 is s1)
print(t2 is s2)

print(10 in t2)      # True 
print(l2[2] in t3)   # True

print(l2 is t3)      # False

    

