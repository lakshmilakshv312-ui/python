#find the length of number
"""number = 12345
length = len(str(number))
print(f"The length of the number is: {length}")"""
#dont know the number of iterations that case uses while loop
"""n = 156
count = 0
while n>0:
    n //=10
    count +=1
    print(count)"""

#sum of digit in a number
"""number = 12345
sum_of_digits = sum(map(int, str(number)))
print(f"The sum of digits for {number} is: {sum_of_digits}")"""
#while loop
"""n = 156
s = 0
while n>0:
    rem = n % 10
    n//= 10
    s=s+ rem
print(s)"""

#reverse of a number
"""num = 1234
rev = 0
while num != 0:
    rem = num % 10
    rev = rev * 10 + rem
    num //= 10
print(rev)"""

#check weather the number is palindrom or not
"""num = 1221
temp = num
rev = 0
while temp > 0:
    rem = temp % 10
    rev = (rev * 10) + rem
    temp = temp // 10
if num == rev:
  print('Palindrome')
else:
  print("Not Palindrome")"""

#check weather the number is amstrong or not
"""number = int(input("Enter a number: "))
sum = 0
temp = number
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
    if number == sum:
        print(sum,"is an Armstrong number")
    else:
        print(sum,"is not an Armstrong number")"""

#perfect number
#for loop
"""n = 28
Sum = 0
for i in range(1, n):
    if(n % i == 0):
        Sum = Sum + i
if (Sum == n):
    print("Number is a Perfect Number.")
else:
    print("Number is not a Perfect Number.")"""







