#even or odd
"""n1,n2,n3 = map(int,input().split())
if(n1%2 == 0):
    print("n1 is even")
else:
    print("n1 is odd")
if(n2%2 == 0):
    print("n2 is even")
else:
    print("n2 is odd")
if(n3%2 == 0):
    print("n3 is even")
else:
    print("n3 is odd")"""

# find which is even or odd from list numbers
"""list = [1,2,3,4,5]
for index in range(0,5,1):
    if list[index]%2==0:
        print(list[index],"is even")
    else:
        print(list[index],"is odd")"""

"""#print even numbers between 20-40
n=list(map(int,input().split())
for i in range(20,41,2):
    print(i,"is even")
else:
    print(i,"is odd")"""

#2nd method
"""for i in range(20,41,2):
    if(i%2==0):
        print(i,"is even")
else:
    print(i,"is odd")"""

"""for num in range(20,41):
    if num%2 == 0:
        print(num)"""

#print 1-100 numbers
"""n=list(map(int,input().split())
for i in range(1,101):
    print(i, end = " ")"""

#find the sum of n natural numbers
"""n = int(input())
total = 0
for i in range(1,n+1):
    total = total+i
print(total)"""

##while loop##
#Print numbers from 1 to 100 using while loop
"""num = 1
while num <= 100:
    print(num, end=" ")  
    num += 1  
print("\nDone printing 1 to 100.")"""
      
#print even number betwwen 10-40
"""num = 10
while num <= 40:
    print(num)
    num += 2"""
    
#print odd bunber between 1-50
"""num = 1
while num <= 50:
    if num % 2 != 0:
        print(num)
    num += 1 """ 

#find which even or odd from list of number
"""numbers = [12, 7, 9, 24, 18, 5]  
i = 0
while i < len(numbers):
    num = numbers[i]
    if num % 2 == 0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")
    i += 1""" 

# Sum of even numbers up to n using while loop
"""n = int(input("Enter a number: "))
i = 2
sum_even = 0
while i <= n:
    sum_even = sum_even + i
    i = i + 2
print("Sum of even numbers up to", n, "is:", sum_even)"""



    
