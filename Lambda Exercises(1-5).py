# Mastan Abdulkhaligli
# Lambda (anonymous function) exercises 1-5(Including)

"""1. Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, 
also create a lambda function that multiplies argument x with argument y and print the result"""

first = lambda x: x+15
second  = lambda x,y: x*y

print(second(5,3))

"""2. Write a Python program to create a function that takes one argument, 
and that argument will be multiplied with an unknown given number """

def cal(n):
    return lambda x: x*n

print(cal(15)(5))

"""3. Write a Python program to sort a list of tuples using Lambda.
Original list of tuples:"""

my_list = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

my_list.sort(key = lambda x: x[1])
print(my_list)

"""4. Write a Python program to sort a list of dictionaries using Lambda"""
my_dict = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, 
            {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, 
            {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]


my_dict_sorted = sorted(my_dict,key = lambda x: x['color'])
print(my_dict_sorted)

"""5. Write a Python program to filter a list of integers using Lambda"""

int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = list(filter(lambda x: x%2==0,int_list))
odd_numbers = list(filter(lambda x: x%2!=0,int_list))

print(even_numbers,"\n",odd_numbers)
