# Mastan Abdulkhaligli
# Lambda (anonymous function) exercises 6-10(Including)


"""6. Write a Python program to square and cube every number in a given list of integers using Lambda"""

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

square_list = list(map(lambda x: x**2,my_list))
cube_list = list(map(lambda x: x**3,my_list))

print(square_list,"\n",cube_list)


"""7. Write a Python program to find if a given string starts with a given character using Lambda."""
def func(x):# Given String
    return lambda y: x[0]==y


print(func("Mastan")("M"))

"""8. Write a Python program to extract year, month, date and time using Lambda."""

import datetime
now = datetime.datetime.now()

year  = lambda x: x.year
print(year(now))

month = lambda x: x.month
print(month(now))

# And so on

"""9. Write a Python program to check whether a given string is number or not using Lambda."""

g = lambda x: True if x.isnumeric() else False
print(g("25"))

# Lets try filter function and apply it to array of string

str_list = ["15","Mastan", "Cs", "55","1996", "is","my"]

cs  = list(filter(lambda x : True if x.isnumeric() else False,str_list))
print(cs)

cs  = list(map(lambda x : True if x.isnumeric() else False,str_list))
print(cs)

"""10. Write a Python program to find intersection of two given arrays using Lambda"""

array_nums1 = [1, 2, 3, 5, 7, 8, 9, 10]
array_nums2 = [1, 2, 4, 8, 9]

intersection = list(filter(lambda x: x in array_nums1,array_nums2))
print(intersection)
