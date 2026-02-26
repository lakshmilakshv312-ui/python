"""#string operations¶
1.string Concatenation(using +)
2.string Repetation(using * )"""

"""#String Concatenation
s1 = 'code'
s2 = 'gnan'
print(s1+s2)"""

"""#String Concatenation
s1 = 'code'
s2 = 'gnan'
print(s1+" " + s2)
print(s1 * + " " + 5)"""

"""#string functions
case convesrtion function
a. upper()
b. lower()
c. swapcase()
d. title()
e. capitalize()"""

"""s1 = 'likitha'
print(s1.upper())"""

"""s1 = 'likitha'
print(s1.lower())"""

"""s1 = 'likitha'
print(s1.swapcase())"""

"""s1 = 'likitha'
print(s1.title())"""

"""s1 = 'likitha'
print(s1.capitalize())"""

"""s1 = 'likitha'
print(s1.isupper())"""

"""s1 = 'likitha'
print(s1.islower())"""

"""s1 = 'likitha'
print(s1.isdigit())"""

"""s1 = 'likitha'
print(s1.isalpha())"""

"""s1 = 'likitha'
print(s1.isalpha())"""

"""#string functions
s= "The sky is blue and ocean is blue"
res = s.split()
print(res)
print(s.split(sep = 'Blue'))
print(s.split(sep = 'blue'))"""

"""#string functions
#find(sub_str) : it returns the first occurence sub string index if it present in string otherwise
#-1
s= "The sky is blue and ocean is blue"
print(s.find('is'))
print(s.find('z'))"""

"""#string functions
# strip() : it removes the leading and lagging white space
# -1
s= "                 The sky is blue and ocean is blue                 "
print(s.strip())
print(s.lstrip())
print(s.rstrip())"""

"""#string functions
# strip() : it removes the leading and lagging white space
# -1
s= "                 The sky is blue and ocean is blue                 "
print(s.strip('@'))
print(s.lstrip())
print(s.rstrip())"""

"""#string functions
# 'sep'.join(iterable): its joins the all elements in the iterable with separator
lst = ['The', 'sky', 'is', 'blue', 'and', 'ocean', 'is', 'blue']
print("".join(lst))
print(' '.join(lst))
print('@'.join(lst))"""
