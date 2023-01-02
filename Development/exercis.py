#to print the your age

# birth_year = input('when was you born?')
# age = 2022 - int(birth_year)
# print('you age is = '+ str(age))

#
# username = input('what is your name')
# password = input('what is your password')
#
# password_len = len(password)
#
# hidden_pwd = '*' * password_len
#
#
# #print(f'{username}, your password {password} is {password_len} letters only')
#
# print(f'{username}, your password {hidden_pwd} is {password_len} letters only')


# my_list = [1,2,3,4,5,6,7,8,9,10]
#
# sum = 0
# for i in my_list:
#     sum = sum  + i
# print(sum)
#
# from datetime import datetime,timezone
#
# current = datetime.now(timezone.utc)
# print(current)
# Date_str = str(current.year-2000)+ str(current.month) +str(current.day)
# #print(Date_str)
#
# sum = 0
# for digit in Date_str:
#       sum += int(digit)
#       #print(sum)
# lastdigit_sum = int(repr(sum)[-1]) #fist digit of password
# print(lastdigit_sum)
# lastdigit_year = int(repr(current.year )[-1]) #last digit of year
# print(lastdigit_year)
#
# rev_date = str(lastdigit_sum) + str(lastdigit_year) + (str(current.day)[-1]) + (str(current.day)[-2])
# print(str(current.day)[-1]) # 4
# print(str(current.day)[-2]) # 2

#print(rev_date)

picture = [
      [0,0,0,1,0,0,0],
      [0,0,1,1,1,0,0],
      [0,1,1,1,1,1,0],
      [1,1,1,1,1,1,1],
      [0,0,0,1,0,0,0],
      [0,0,0,1,0,0,0],
]
#
# # if 0-> print '' and if 1-> print *
#
# print(picture)
# def show_tree():
#   for row in picture:
#       for pixel in row:
#         if(pixel == 1):
#             print('*', end='') # not gonna print the new line
#         else:
#             print(' ', end='')
#       print('') #this will take the o/p to next line after the 1st iteration
#
# show_tree()
# fill = '*'  #create validation variable in advance, it validation changes then it will be changed here
# empty = ' '
#
# for row in picture:
#       for pixel in row:
#             if(pixel == 1):
#                   print(fill, end='') # not gonna print the new line
#             else:
#                   print(empty, end='')
#       print('') #this will take the o/p to next line after the 1st iteration

#-----------check duplicate value in list -------------------
#
# some_list = ['a','a','b','c','d','b','m','n','n']
# # you can not use the set
#
# Set = print(set(some_list))
#
# duplicates = []
#
# for value in some_list:
#       if some_list.count(value) > 1:
#             if value not in duplicates:
#               duplicates.append(value)
# print(duplicates)
#
# def is_even(num):
#       if num % 2 ==0:
#             return True
#       elif num % 2 != 0:
#             return False
#
# print(is_even(50))

# def super_func(*args, **kwargs):
#       print(args)
#       print(kwargs)
#
#       total = 0
#       for items in kwargs.values():
#             total = total+items
#       return sum(args) + total
#
# print(super_func(5,4,5, num1=5, num2=10))

# def highest_even(li):
#       even = [] # new list to get the even number
#       for i in li:
#             if i % 2 == 0:
#                   even.append(i)
#       return max(even)
#
# print(highest_even([10,2,3,4,8,11]))
#
# print(max(3,4,5,6,8))
# ab = 10/2
# print(ab)

# class Cat:
#       def __init__(self, name, age):
#             self.name = name
#             self.age = age
#
#
# obj1 = Cat('a', 38)
# obj2 = Cat('b', 48)
# obj3 = Cat('c', 58)
#
# print(obj1.age)
#
#
# def max_age():
#  cats_age = [obj1.age,obj2.age,obj3.age]
#  x = max(cats_age)
#  return x
#
# print(max_age())

#
# class SuperList(list): #if you define list here, Class superlist has parent list
#       def __len__(self):
#             return 100
#
#
# super_list1 = SuperList()
# print(len(super_list1))
# super_list1.append(5) #y defining list in parent class, we can append it now
# print(super_list1[0])
#
# print(issubclass(SuperList, list)) # superlist is subclass of class list
# print(issubclass(list, object)) #evferything in python is object, list is subclass of object

#-------------------Exercise------------------


from functools import reduce

# #1 Capitalize all of the pet names and print the list
# my_pets = ['sisi', 'bibi', 'titi', 'carla']
#
# new_list = []
# for item in my_pets:
#         item = item.upper()
#         new_list.append(item)
# print(new_list)
#
#
# #2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
# my_strings = ['a', 'b', 'c', 'd', 'e']
# my_numbers = [5,4,3,2,1]
#
# my_numbers.sort()
# print(my_numbers)
#
# print(list(zip(my_strings , my_numbers)))
#
# #3 Filter the scores that pass over 50%
# scores = [73, 20, 65, 19, 76, 100, 88,10]
#
#
#
# def over50(iterable):
#     return iterable > 50
#
# print()
#
# print(list(filter(over50, scores)))
#
#
#
# #4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total
#
# from functools import reduce
#
# def accumlator(acc, item):
#     print(acc ,item)  # 0 from argument 1 from my_list 0 1
#     return acc + item
#
# print((reduce(accumlator,my_numbers + scores, 0)))


# lamda expression to square our list

# my_list = [5,4,3]
#
# new_list = []
# for item in my_list:
#       print(item)
#       new_list.append(item*item)
# print(new_list)
#
#
# lam_list = list(map(lambda  num: num**2, my_list))
# print(lam_list)
#
# #num = num*num or num**2 are same thing
#
#
# #list sorting on based on second value in tuple -1, 2 ,3
#
# a = [(0,2), (4,3),(9,9),(10,-1)]
# # a.sort()
# # print(a)  #it will sort based on the first item in the tuple
#
# #but we want to sort by 2nd item in tuple
#
# a.sort(key=lambda x:x[1])   #lambda is define key to get the second item
#
# print(a)
#
#
#
# #----to find the duplicate with list comprehension
#
# some_list = ['a','b','f','g','b','n','m','g']
#
# duplicate = [x for x in some_list if some_list.count(x) >1]
# duplicate1 = set([x for x in some_list if some_list.count(x) >1])
# duplicate2 = list(set([x for x in some_list if some_list.count(x) >1]))
# print(duplicate)
# print(duplicate1)
# print(duplicate2)

#----decorator execrcise

# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
# user1 = {
#     'name': 'Sorna',
#     'valid': True #changing this will either run or not run the message_friends function.
# }
#
# def authenticated(fn):
#   def wrapper(*args, **kwargs):
#       if args[0]['vaild']:
#             return fn(*args, **kwargs)
#   return wrapper
#
# @authenticated
# def message_friends(user):
#     print('message has been sent')
#
# message_friends(user1)


def do_stuff(num):
    return num + 5
