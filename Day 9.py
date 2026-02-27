#Sum of list elements
"""def sum_list(lst):
    total = 0
    for num in range(len(numbers)):
        total = total + lst[num]
    return total
#list input
numbers = [10, 20, 30, 40, 50]
#function call
result = sum_list(numbers)
print("Sum of list elements:", result)"""

#sub of two numbers 
"""def sub(x,y):
    return x - y
b1 = int(input())
b2 = int(input())
print(sub(b1,b2))
print(sub(b2,b1))"""

#sum of two numbers 
"""def add(x,y):
    return x + y
b1 = int(input())
b2 = int(input())
print(add(b1,b2))"""

#Simple Calculator Program
"""num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
#Choose operation
print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice = input("Enter choice (1/2/3/4): ")
#Perform calculation
if choice == '1':
    result = num1 + num2
    print("Result =", result)
elif choice == '2':
    result = num1 - num2
    print("Result =", result)
elif choice == '3':
    result = num1 * num2
    print("Result =", result)
elif choice == '4':
    if num2 != 0:
        result = num1 / num2
        print("Result =", result)
    else:
        print("Error! Division by zero is not allowed.")
else:
    print("Invalid choice")"""

# 1. Positional arguments
# sub of two numbers 
"""def sub(x,y):
    return x - y
b1 = int(input())
b2 = int(input())
print(sub(b1,b2))
print(sub(b2,b1))"""

# keyword arguments
# sum of two numbers 
"""def add(x,y):
    return x + y
b1 = int(input())
b2 = int(input())
print(add(x = b1,y = b2))
print(add(y = b2,x = b1))"""

#sum of three numbers
"""def sum(x,y,z):
    return x+y+z
b1 = int(input())
b2 = int(input())
b3 = int(input())
print(sum(x = b1, y = b2, z = b3))
print(sum(x = b3, y = b2, z = b1))"""

#sum of four numbers
"""def sum(x,y,z,s):
    return x+y+z+s
b1 = int(input())
b2 = int(input())
b3 = int(input())
b4 = int(input())
print(sum(x = b1, y = b2, z = b3, s = b4))
print(sum(x = b4, y = b3, z = b2, s = b1))"""

#positional arguments with default arguments
#sum of four numbers
"""def sum(w,x,y = 0, z = 0):
    return w+x+y+z
b1 = int(input())
b2 = int(input())
b3 = int(input())
b4 = int(input())
print(sum(b1,b2))
print(sum(b1,b2,b3))
print(sum(b1,b2,b3,b4))"""

#sum of four numbers
"""def add(w,x,y = 0, z = 0):
    return w+x+y+z
b1 = int(input())
b2 = int(input())
b3 = int(input())
b4 = int(input())
print(add(b1, x = b2))"""
#print(add(b1, y = b2))#TypeError: add() missing 1 required positional argument: 'x'
#print(add(y = b2,b1))# posistional arguments follows keyword arguments

#variable length positional arguments
#sum of four numbers
"""def add(x, *args):
    print(type(args))
    print(args)
    s = 0
    for num in args:
        s += num
    return s
print(add(10,20,30,40,50))"""

"""def add(x,y = 0,*args):#y = 20
    print(type(args))
    print(args)
    s = 0
    for num in args:
        s += num
    return s
print(add(10,20,30,40,50))
print(add(10,20,30,40,50,60,1,2,3,4,56))# we can represent whenever you wnat by using variable"""

#variable length keyword arguments
"""def add(x, y=0, *args, **kwargs):
    print(x,y)
    print(type(args), args)
    print(type(kwargs), kwargs)
print(add(10,20,30,40,50,1,2,3,4,5,6, a=10, b=0, c=30))"""

"""def add(x, y=0, *args, **kwargs):
    print(x,y)
    print(type(args), args)
    print(type(kwargs), kwargs)
print(add(10,20,30,40,50,1,2,3,4,5,6, a=10, b=0, c=30))
print(add(10))
print(add(10,-20))#,30,40,50,1,2,3,4,5,6, a=10, b=20, c=30))
print(add(10,20,30,40,50,))
#output
10 20
<class 'tuple'> (30, 40, 50, 1, 2, 3, 4, 5, 6)
<class 'dict'> {'a': 10, 'b': 0, 'c': 30}
None
10 0
<class 'tuple'> ()
<class 'dict'> {}
None
10 -20
<class 'tuple'> ()
<class 'dict'> {}
None
10 20
<class 'tuple'> (30, 40, 50)
<class 'dict'> {}
None"""

#lists
"""l = [1,2,5,6,7,10]
print(l[-1:-5:-1])
print(l[-1:-100:-1])
print(l[5:-6:-1])
print(l[1:-2:1])
print(l[3:-5:-1])
print(l[-2])
print(l[3:-5])
#Output
[10, 7, 6, 5]
[10, 7, 6, 5, 2, 1]
[10, 7, 6, 5, 2]
[2, 5, 6]
[6, 5]
7
[]"""

"""print([1,2,3]+[3])"""
"""print([1,2,3]+[4,5])"""

"""# Function definition with arguments
def calculator(num1, num2, operator):
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Invalid operator"
    return result
# Taking input from user
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")
# Function call with arguments
output = calculator(a, b, op)
# Display result
print("Result =", output)"""





