# Existing add() function which adds two numbers

def add_Two(n1,n2):
    return n1+n2

# creating a custom decorator

def my_decorator(func):
    def decor_fun(*args):
        print("<-----Starting addition of three numbers----->")
        res=func(*args)
        print("<-----Finished the addtition of numbers------>")
        return res
    return decor_fun

# Using the custom decorator with the function to add 3 numbers

@my_decorator
def add_Three(x,y,z):
    res1=add_Two(x,y)
    total_sum=add_Two(res1,z)
    print(f"The sum of {x},{y} and {z} is = {total_sum}")
    return total_sum

# calling the function to add three numbers
a,b,c=map(int,input("Enter 3 numbers : ").split())
add_Three(a,b,c)
