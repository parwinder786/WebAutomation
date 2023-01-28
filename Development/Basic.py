# name = input('what is your name') # to ask run time input from user
# print(name)
import time

# DATA tYPES

# float will need more memory to store than integer

# print(type(2-4))
# print(type(2/4))
#
# print(5/4)
# print(5//4) # round the value

# % modulas remainder of divison

# print(round(3.1))
#
# print(abs(-10))

# google math functions, keywords

# Operator predence
# print(20 - 3 * 4)
# print((20 - 3) * 4)
#
# print(bin(5))
# print(int('0b101', 2))

#
# iq = 100 # whole line is statement
# user_age = iq / 5   #(id/5 is expression which produces the value)
# user_age = iq / 5 entire line of code is statement which perform action

# augmented assignment operator

some_value = 5
# some_value = some_value + 7
# some_value += 7
# print(some_value)
#
# #string
# long_string = '''
# WOW
# ---
# ***
# &&&
# '''
# print(long_string)
#
#
# print(type(str(100)))
#
# weather= "\t it\'s \"kind of\" sunny \n hope it good" #t add tab n new line
# #weather= "it\'s \"kind of\" sunny"
# print(weather)


# name = 'john'
# age = 55
#
# print(f'hi {name}. you are {age} years old')
# print('hi {}. you are {} years old'.format('john', '55'))
# print('hi {}. you are {} years old'.format(name, age))
# print('hi {0}. you are {1} years old'.format(name, age))


# selfish = '01234567'
# print(selfish[1:8:2])
# print(selfish[1:])
# print(selfish[:5]) #01234
# print(selfish[::1]) #01234567
# print(selfish[::-1])

# strings are immutable, can not change the value
# only way is to assign the value
# selfish[1] = 4 # not possible
# selfish = '8'
#
# print(selfish)
#
# ab = "hi, how are you"
# print(ab.upper())
# print(ab.capitalize())
#
# print(ab.find('are'))
#
# print(ab.replace('hi', 'hola'))

# ---------------------list----------------------
#
# cart = ['notebook','sunglass','toys','grapes']
#
# #new_cart = cart
# new_cart = cart[:]
# new_cart[0] = 'new_value'
#
# print(new_cart)
# print(cart)

# matrix to define multidimeonsal list or array inside other array
# #useful in pictures navigation for pixel,
# matrix = [
#     [1,5,1],
#     [0,1,0],
#     [1,0,1]
# ]
#
# print(matrix[0][1])
# print(len(matrix))
#
# cart = ['notebook','sunglass','toys','grapes']
# new_cart = cart.append('110')
# print(new_cart)
# print(cart)

# to make it impact into new list
# cart.append('100')
# new_cart = cart

# insert
#
# cart.insert(4, 100)
# print(cart)
#
#
# cart.extend([1777, 11145, 4444])
# print(cart)
#
# ab = cart.pop()
# print(ab)
# print(cart)


# basket = [0, 1,5, 99, 8, 9, 8,44]
# print(basket.index(5))
#
# print(9 in basket)
#
# print(basket.count(8))
#
# basket.sort()
#
# # print(sorted(basket))
# # print(basket)
# basket.reverse()
# print(basket[::-1])
# print(basket)
#
# print(list(range(1,100)))

#
# sen = '7'
# new_sen = sen.join(['hi', 'my', 'a'])
# print(new_sen)
#
# new_se = ' '.join(['hi', 'my', 'a'])
# print(new_se)
#
# a,b,c, *other = [1,2,3,4,5,6,7,8,9]
# print(a)
# print(b)
# print(c)
# print(other)
#
#
# dict = {'a':[1,4,5], 'b':2, 'x':True}
#
# print(dict['a'][1])

# print(dict.items())
# ab = [{'a':[1,4,5], 'b':2, 'x':True},{'v':[1,4,5], 'b':2, 't':True}]
#
# print(ab[0]['a'])
#
# print(dict.get('age', 55))
#
# user = dict(name='joho')
# print(user)

# tuple

# My_tuple = (1,3,4,5)
#
# x,y,x, *other = (1,3,4,5)
#
# print(My_tuple.count(5))
# print(My_tuple.index(5))
# new_tuple = My_tuple


# ======set


# my_set = {1,4,65,7,1,8}
#
# your_set = {777,666,33,22,1,4,65,7,1,8}
#
# print(list(my_set))
#
# print(my_set)
#
# my_set.add(88)
#
# print(my_set)
#
# #print(my_set[0])
# print(1 in my_set)
# my_list = [1,2,3,4,5,1]
# print(set(my_list))

# my_set = {1,4,65,1,8}
#
# your_set = {777,666,33,22,1,4,65,7,1,8}
#
# print(my_set.union(your_set))
# # print(my_set.difference(your_set))
# #
# #
# # my_set.discard(8)
# # print(my_set)
# #
# # my_set.difference_update(your_set)
# # print(my_set)
#
# #
# # my_set.intersection(your_set)
# # print(my_set)
#
# is_old = True
#
# #is _old = 'hello' # bool('hello')     '' or 0 are falsy values
#
# if is_old:
#     print('Value is True')
# else:
#     print('Value is false')
#
# #dothisiftrue if checksconditionhere else dothisifconditionfalse
#
# is_friend = True
# is_user = True
#
# can_message = "message allowed" if is_friend else "not allowed to message"
#
# print(can_message)
#
# print(is_friend and is_user)
#
# print(10 == 10.1)
#
# #--------------For loop---------------
#
# for variable in 'iterable':
#     print(variable)
#
# for item in (1,2,):
#     for x in ['a','b']:
#         print(item, x)


# user_dict = {
#     'name' : 'arry',
#     'age' : 500,
#     'can-do': False
# }
#
# for i in user_dict.values():
#     print(i)
#
# for i in user_dict.items():
#     key, value = i;
#     print(key, value)
#
# # for i in 10:
# #     print(i)
#
# print(range(100))
# #
# # for no in range(0, 100):
# #     print(no)
#
# for no in range(10, 0, -1):
#     print('email sent')
#
# for _ in range(2):
#     print(list(range(10)))
#
#
# for i,char in enumerate('Hello'):
#     (print(i, char))
#
# for i,char in enumerate(list(range(100))):
#     if char == 50:
#         print('index of 50 is ' + str(i))
# i = 0;
# while i<10:
#     print(i)
#     i = i + 1
#     break
# else:
#      print('done with all the work')
#
# while True:
#     response = input('say something: ')
#     if (response =='bye'):
#      break
#
# my_list = [1,2,3]
#
# for  i in my_list:
#     pass # it will remove the errors
# continue
# print(i)

# ------------functions ------------------------------

# def say_hello(name = 'ram', emoji = '+++'): # to call the function, parameters , whwn we defined the function
#     print(f'Hello,, {name} {emoji}')
#
# #arguments when we call or invoke the function, will be passed during the call of function when we provide the actual value to function
# say_hello('parwinder', 'smile')
#
#
# say_hello( emoji ='smile', name ='parwinder',)
#
# say_hello()

# def sum( num1, num2):
#     #print('Hii')
#     #num1 +  num2
#     return num1 + num2
#
#
# total = sum(4,6)
# print(total)
# print(sum(4,5))
#
# print(sum(20,total))

# define the function inside the funtion

# def sum( num1, num2):
#     def another_func(num1, num2):
#         return num1 + num2
#     return another_func
#
# total = sum(10,20)
#
# print(total(10, 20))
#
# 'hello'.capitalize()

# def test(a):
#     '''
#     info: docstring
#     '''
#
#     print(a)
# help(test)
# print(test.__doc__)

# a = 'hellooooooerer'

# if ((n := len(a)) > 10):
#     print(f"too long {len(a)}")

# while((n := len(a)) >1):
#     print(n)
#     a = a[:-1]

# x = 10
#
# # def some_func():
# #     total = 100
# # print(x)
#
#
# def parent():
#     x = 2
#     def con():
#         return sum
#     return con()
#
# print(parent())
# print(x)
#
#
# a = 10
#
# def confusion(b):
#     print(b)
#     a = 90
#
# confusion(66)

# total = 0
#
#
# def count():
#     global total
#     total += 1
#     return total
#
#
# count()
# print(count())

#========================OOP Class========================================
# class BigObject:
#     pass
#
# obj1 = BigObject()
#
# print(type(obj1))


# class PlayerCharacters:
#     membership = True #class object attribute, its static. it will true for all the objects
#     def __init__(self, name, age): # init is constructor, will be automatically called upon instastiate, self linked to class
#         #if (self.membership):
#         #if (PlayerCharacters.membership): same as above because self links to the class
#         if (age >18): #add check in constructor
#             self.name = name #self linked to called object
#             self.age = age # attributes,dynamic one
#
#     def run(self):
#         print('run')
#         #return 'done' #without it will return none
#
#     @classmethod
#     def add_things(cls, num1, num2):
#         return num1 + num2
#
#     #@classmethod
#     # def add_things(cls, num1, num2):
#     #     return cls('teddy', num1 + num2) # it will insitate the obkj
#     @staticmethod
#     def add_number(num1, num2):
#         return num1 + num2
#
# player1 = PlayerCharacters('pindu', 44)
# player2 = PlayerCharacters('pitt', 88)
# player2.surtu = 'haha'
#
# print(player1.name)
# print(player1.age)
# print(player1.run())
# print(player2.surtu)
#
# print(player1.membership)
#
# print(PlayerCharacters.add_things(2,3))
#
# print(PlayerCharacters.add_things(4,9))


#
# class character:
#     def __init__(self, name, age): #__init__ is called dunder method (double underscore, its bulit in)
#         self._name = name #underscore means private, there is no private variable in python, underscore means should not modified
#         self._age = age
#
#     def run(self):
#         #return self
#         print('run')
#
#     def speak(self):
#         print(f'my name is {self._name}, and i am {self._age} years old')
#
# player = character('pindu', 44)
#
# print(player.speak())
#
# player.name = '!!!!!'
# player.speak = 'booo'
#
# print(player.speak)


# class User():
#
#     def sign_in(self):
#         print('logged in')
#
#     def __init__(self, email):
#         self.email = email
#         print('what is your email, constructor in parent class')
#
#     def attack(self):
#         print('do nothing')
#
#
# class Wizard(User):
#     def __init__(self, name, power, email): # to call the parent class constrcutor method
#         User.__init__(self, email)  # to call the parent class constrcutor method
#         super().__init__(email) # other way to call the constructor mehod
#         self.name = name
#         self.power = power
#
#     def attack(self):
#         print(f'attaacking with the power of {self.power}')
#
#
# class Archer(User):
#     def __init__(self, name, arrows):
#         User.attack(self) # to call the parent class with sub class other wise only sub class method will be executed
#         self.name = name
#         self.arrows = arrows
#
#     def attack(self):
#         print(f'attaacking with the arrows, arrows left {self.arrows}')
#
#
# #to check if something is instance in python
#
#
#
# wizard1 = Wizard('pindu', 50, 'abc@mail.cm')
#
# print(wizard1.email)
#
# print(dir(wizard1))
# archer1 = Archer('Robin', 30)
#
# print(wizard1.attack())
# print(archer1.attack())

# def player_attack(char):
#     char.attack()

# for item in [wizard1, archer1]:
#     item.attack()

#print(isinstance(wizard1, Wizard))





# archer1 = Archer('Robin', 100)
#
# wizard1.attack()
# archer1.attack()
#
# print(wizard1.sign_in())
# print(archer1.sign_in())

#
# class Toy():
#     def __init__(self, color,age):
#         self.color = color
#         self.age = age
#     def __str__(self):
#         return f'{self.color}'
#     def __len__(self):
#         return 5
#
# action_figure = Toy('red', 0)
# print(str(action_figure))
# print(len(action_figure))
#
# print(action_figure.__str__())
#
# print(action_figure)

#------------------MRO-------------------------#
#
# class A:
#     num = 10
#
# class B(A):
#     pass
#
# class C(A):
#     num = 1
#
# class D(B, C):
#     pass
#
# #---pute functions
#
# print(D.mro())  # print the order of class methods execution
# print(D.num)


# def mmultiply_by2(li):
#       new_list = []
#       for item in li:
#             new_list.append(item*2)
#       return new_list
#
# mmultiply_by2([1,2,3])

#----pure functions

# my_list = [1,2,3]
# your_list = [12,33,44]
# # def mmultiply_by2(item):
# #       return item*2
# #
# # def check_odd(item):
# #     return item%2 != 0
#
#
# # print(list(map(mmultiply_by2 , my_list)))
# #
# # print(list(filter(check_odd , my_list)))
# #
# # print(list(zip(my_list , your_list)))
# #
# # print(my_list)
#
from functools import reduce
#
# def accumlator(acc, item):
#     print(acc ,item)  # 0 from argument 1 from my_list 0 1
#     return acc + item
#
# print((reduce(accumlator,my_list, 0)))  #0 is intial accumulator value


#---lambda functions

# lambda parameter: function(parameter) #action or function we want to take on parameter
#
#
# my_list = [1,2,3]
#
#
# # def mmultiply_by2(item):
# #       return item*2
#
# # print(list(map(mmultiply_by2 , my_list)))
#
#
# print(list(map(lambda item: item*2, my_list)))
#
#
# print(list(filter(lambda item: item%2 != 0, my_list)))
#
#
# print(reduce(lambda acc, item: acc + item, my_list))


#----list comprehensions

# my_list = []

# my_list_comprehension = [char for char in'hello'] # first char is variable, second is iterable
#
# print(my_list_comprehension)
#
# my_list_comprehension1 = [num*2 for num in range(0,100)]
#
# my_list_comprehension2 = [num*2 for num in range(0,100) if num%2 ==0]
#
# print(my_list_comprehension1)
# print(my_list_comprehension2)    #
#     # for char in 'hello':
#     #     my_list.append(char)
#     # print(my_list)
#
# # print the even number
#
# #---set comprehension
#
# my_list_comprehension = {char for char in'hello'} # first char is variable, second is iterable
#
# print(my_list_comprehension)
#
# my_list_comprehension1 = {num*2 for num in range(0,100)}
#
# my_list_comprehension2 = {num*2 for num in range(0,100) if num%2 ==0}

# simeple_dict = {
#     'a':1,
#     'b':2
# }
# my_dict = {key:value**2 for key,value in simeple_dict.items()} #power of 2 to the dictionary items
#
# print(my_dict)
#
#
# new_dic = {num:num*2 for num in [1,2,3] }
# print(new_dic)

# def hello(func):
#     func()
#
# def greet():
#     print('still here')
#
#
# # greet = hello
# #
# # del hello
# # hello()
# a = hello(greet)
# print(a)


#Hiher order of function HOC

#----------------------------------Decoratotrs--------------------------------
#
# def my_decorator(func):
#     def wrap_func():
#         print('**********')
#         func()
#         print('^^^^^^^^^^')
#     return wrap_func
#
# @my_decorator  #super boost it, it will use the above methods
# def hello():
#     print('hello')
# hello()
# # #how it works
# # hello2 = my_decorator(hello)
# # hello2
# print('----------------------------------')
# def my_decorator(func):
#     def wrap_func(x):
#         print('**********')
#         func(x)
#         print('^^^^^^^^^^')
#     return wrap_func
#
# @my_decorator  #super boost it, it will use the above methods
# def hello(greeting):
#     print(greeting)
# hello('hiiiiiii')
#
# print('----------------------------------')
# def my_decorator(func):
#     def wrap_func(*args, **kwargs):
#         print('**********')
#         func(*args, **kwargs)
#         print('^^^^^^^^^^')
#     return wrap_func
#
# @my_decorator  #super boost it, it will use the above methods
# def hello(greeting, emoji=':('):
#     print(greeting, emoji)
# hello('hiiiiiii')


#---create decorator
#
# from time import *
# def performance(fn):
#     def wrapper(*args, **kawrgs):
#         t1 = time()
#         result = fn(*args, **kawrgs) #measure the performance of function
#         t2 = time()
#         print(f'took {t2-t1} s')
#         return result
#     return wrapper
#
# @performance  #custom decotrator
# def long_time():
#     for i in range(100000000):
#         i*5
#
# long_time()



#-----------------------------Error Handling----------------------

#print('123)  #syntax error
#print(1+'hello')  #type error int and str
#
# def hell()  # it will show you the syntax error because : is not placed
#     print('ahha')
#
#
# li = [3,5,6]
# li[5]  #it will show list index out range
#
# di ={'a':1}
# di['m'] #key error because key is not present


# while True:
#     try:
#         age = int(input('what is your age '))
#         10/age
#         raise ValueError('custom')
#     except ValueError:
#         print('please enter a number')
#     except ZeroDivisionError:
#         print('please enter a number higher than 0')
#     else:
#         print('Thank You')
#         break

# def sum(num1, num2):
#     try:
#         return num1/num2
#     except(TypeError, ZeroDivisionError) as err:
#         print(err)
#
# print(sum(1,0))

#--------------------Generators---------------------
#range is generator

# range(100) #range creates items 1 by 1 in memory
# list(range(100)) #list creates togther 100 items in memory
#
# #custom generator
#
# def generator_function(num):
#     for i in range(num):
#         yield i
#
# g = generator_function(10)
# next(g)
# print(next(g))
# print(next(g))

#----Under the hood of generators (for loop)

# def special_for(iterable):
#     iterator = iter(iterable)
#     while True:
#         try:
#             print(iterator)
#             print(next(iterator)*2)
#         except StopIteration:
#             break
#
# special_for([1,2,3])


# class MyGen():
#     current = 0
#     def __int__(self, first, last):
#         self.first = first
#         self.last = last
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if MyGen.current < self.last:
#             num = MyGen.current
#             MyGen.current +=1
#             return num
#         raise StopIteration
#
#
# gen = MyGen(0, 100)
# for i in gen:
#     print(i)


#print(__name__)
#-------------------in built modules-----------------------

# import random
# print(dir(random)) # it will show the methods for this module
# print(random.randint(1, 10 ))
# print(random.choice([1,2,4,5,7,1]))
# lis = [3,4,11,66,22]
# random.shuffle(lis) #it will shuffle the list
# print(lis)
#help(random)

# import sys
# print(sys)
# sys.argv
#
# import pyjokes
# jk = pyjokes.get_joke('en', 'neutral')
# print(jk)
#=======collection module=============
# from collections import Counter,defaultdict, OrderedDict
# li = [1,2,3,4,5,6,3,2,22,11,44,55,3]
# sentence = "hello hi are you"
# print(Counter(li))  # it will return dictionary how many time item is repeated inside the list
# print(Counter(sentence)) #will return the number of character used in string
#
# dic = defaultdict(lambda: 'does not exit', {'a':1, 'b':2}) #you will be able to add if it does not exit
# print(dic['c'])
#
# d = OrderedDict() #set up the values in dictionary in order way, regular dictionay not have order
# d['a'] = 1
# d['b'] = 2
#
# d2 = OrderedDict()
# d2['a'] = 1
# d2['b'] = 2
# print(d2 == d)
# import datetime
# print(datetime.date.today())
#
# from array import array
# # for less memory we can use array than list
# arr = array('i', [1,2,3])
# print(arr[1])

#--------debugging-----

#linting
#num + 4

#ide/editors
#pycharm - auto formatting, detect erros
#read errors  e.g syntax error, or trying to add str to int
#name error (no variable defined)
#print is good way to debug your code

# import pdb #importing it for debug
# def add(num1, num2):
#     pdb.set_trace()
#     t = 4*4
#     return num1 + num2
# print(add(4,5))

#---------------I/O File working -----------------

# file = open('test.txt')
# print(file.read())
# file.seek(0)
# print(file.read())
# file.seek(0)
# print(file.read())
# with open you can only open the file once, to fix this see(0) is used to set the cursor to 0

#print(file.readline()) # it will read first line
# print(file.readlines()) # it will return the list with all line
# file.close()

#---standard way to read the files

#write to the file
#write mode will override the file

# with open('test.txt', mode='a') as my_file: #mode r is read, if not it automatically assumes read
#     text = my_file.write('\nhey its\'me') #cusors reset and overwite, use append to avoid overwrite as mode
#     print(text)


#------file path-------------
# try:
#     with open('C:\\Users\\jpree\\OneDrive\\Pictures\\Desktop\\ETC\\pythonDeskyoplearning\\psd.txt', mode='r') as my_file:
#         text = my_file.read()
#         #text = my_file.write('\nhey its\'me') #cusors reset and overwite, use append to avoid overwrite as mode
#         print(text)
# except FileNotFoundError as err:
#     print("File does not exit")
#     raise err
# except IOError as err:
#     print('I/O erros')
#     raise err

# from translate import Translator
#
# translator = Translator(to_lang="ja")
#
# try:
#     with open('./test.txt', mode='r') as my_file:
#         text = my_file.read()
#         print(text)
#         translation = translator.translate(text)
#         #print(translation)
#         with open('./test2.txt', mode='w') as my_file2:
#             my_file2.write(translation)
#
# except FileNotFoundError as e:
#     print('check your file path')

#------------------- regular expression  ----------------
import re

# st = "i love my country search this"
# a = re.search('my', st)
# print(a.span())
# print(a.group())
# print(a.end())
#
# #pattern = re.compile('my') #pattern to check
# pattern = re.compile(r"([a-zA-Z]).([a])")
# b = pattern.search(st)
# bb = pattern.findall(st)
# print(bb)
# c = pattern.fullmatch(st) # it has to be exact string
# print(c)
# d = pattern.match(st)
# print(d)
# print(b.group(1))

# email validation for correct format
#(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)
# patt = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
# string = 'b@b.com'
# a = patt.search(string)
# print(a)

# password = re.compile(r"[A-Za-z0-9$%#@]{8,}\d")
# passw = 'hfdh%$9l'
# check = password.fullmatch(passw)
# print(check)

#----------------testing----------------

import unittest
import pytest

# import exercis
#
# class TestMain(unittest.TestCase):
#     def test_do_stuff(self):
#         num = 10
#         result = exercis.do_stuff(num)
#         self.assertEquals(result,15)
#
# unittest.main()
#-----------------Image processing---------------

# from PIL import Image, ImageFilter
#
# img = Image.open('D:\Drive D\Study\Python\WebAutomation\Development\image.png')
#
# #img = Image.open('./Development/image.png')
#
# print(img)
# print(img.format)
# print(img.size)
# print(dir(img))

#filter_img = img.filter(ImageFilter.BLUR) # it will apply the Blur filter
# filter_img = img.filter(ImageFilter.SMOOTH) # it apply the smooth filter
# filter_img = img.convert('L')  # it will convert into grey picture

# rotate = filter_img.rotate(90) # it will rotate the file by 90 degree
# rotate.save("modified.png", "png")

# resize = filter_img.resize((500, 500)) # resize will re size the picture
# resize.save("modified.png", "png")
#
# # instead of resize be we can use thhumbnail
# img2 = Image.open('D:\Drive D\Study\Python\WebAutomation\Development\modified.png')
# print(img2.size)

# box = (100, 100, 400, 400)  # crop the picture on dimesions
# region = filter_img.crop(box)
# region.save("modified.png", "png")

#filter_img.save("modified.png", "png") #jpg support filters
#filter_img.show() # it will show the image

# img.thumbnail((400, 400))  # to generate the thumbnail
# img.save("modified.png", "png")
# print(img.size) # thumbnail will decide the size adjusted size for image
#--------------------PDF -----------------------

# import pypdf
#
# with open('D:\Drive D\Study\Python\WebAutomation\Development\SuperVisaDeclaration_updated_Parwinder Singh.pdf', 'rb') as file:
#     #print(file)
#     reader = pypdf.PdfReader(file)
#     print(len(reader.pages)) # to get total number of pages
#     print(reader.pages[0]) # to get the page number content
#
#     page  = reader.pages[0]
#     page.rotate(90)
#     writer = pypdf.PdfWriter() #this will write the object in memory
#     writer.add_page(page) # add the pages
#     with open('new.pdf', 'wb') as new_file:
#         writer.write(new_file)
#
#
#     #print(reader.numPages)

#-------------------Email--------------------------------

# import smtplib  #allow to create smtp server, which used in send email
# #smtp (simple mail transfer protocol) server used in email sending
# from email.message import EmailMessage
# from string import Template  #substitue variable inside text
#
# from pathlib import Path # similar to os.path
#
# html = Template(Path('index.html').read_text()) #wrap in template object
#
# print(html)
#
# email  = EmailMessage()
#
# email['from'] = 'armanndhillon@gmail.com'
# email['to'] = 'parwinderdhaliwal1990@gmail.com'
# email['subject'] = 'you won million dollar'
# #email.set_content('I am python mater!')
# email.set_content(html.substitute({'name' : 'parwinder'}), 'html')
#
# with smtplib.SMTP(host='smtp.gmail.com', port='587') as smtp:
#     smtp.ehlo()
#     smtp.starttls() # encryption mechanisim
#     smtp.login('armanndhillon@gmail.com','751449Ps!pb03u2300')
#     smtp.send_message(email)
#     print('all is good, email is sent')

#   code to fix the email password issue
# server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
# serverEmail = "EMAILADDRESS"
# serverPw = "QWERTY"
# server.login(serverEmail, serverPw)
# subject = "Rejection"
# body = "Hi! You've been unfortunately declined access to our system."
# message = f'Subject: {subject}\n\n{body}'
# server.sendmail("EMAILADDRESS", doctorEmail['email'], message)
# server.quit()

#-----------------------password checker for HACK-------------------
#
# import requests
# import hashlib
# import sys
#
# #url = 'https://api.pwnedpasswords.com/range/' + 'password123'
#
# #send the hash pwd, companies use this
#
# #url = 'https://api.pwnedpasswords.com/range/' + 'cbfdac6008f9cab4083784cbd1874f76618d2a97'
#
# #give the 5 char of your pwd hash
#
# # url = 'https://api.pwnedpasswords.com/range/' + 'cbfda'
# # res = requests.get(url)
# # print(res)
#
# def request_api_data(query_char):
#     url = 'https://api.pwnedpasswords.com/range/' + query_char
#     res = requests.get(url)
#     if res.status_code != 200:
#         raise RuntimeError(f'Error fecthing: {res.status_code}, check the api and try again')
#     return res
#
# def read_res(response):
#     print(response.text)
#
# def get_password_leaks_count(hashes, hash_to_check):
#     hashes = (line.split(':') for line in hashes.text.splitlines())
#     for h, count in hashes:
#         #print(h, count)
#         if h == hash_to_check:
#             return count # return number of leaks of password
#     return 0 # if password does not found return 0
#     #print(hashes)
# def pwned_api_check(password):
#
#     sha1password = hashlib.sha1(password.encode('utf')).hexdigest().upper()
#     first5_char, tail = sha1password[:5], sha1password[5:]
#     print(first5_char, tail)
#     response = request_api_data(first5_char)
#     #return read_res(response)
#     return get_password_leaks_count(response, tail)
#
# #pwned_api_check('123')
#
# def main(args):
#     for password in args:
#         count = pwned_api_check(password)
#         if count:
#             print(f'{password} was found {count} times...you should probably change the password')
#         else:
#             print(f'{password} was not found. Carry ON!')
#     return 'done!'
#
# if __name__ == '__main__':
#     sys.exit(main(sys.argv[1:]))

#----------------Twitter---------

#
# import tweepy
# auth = tweepy.OAuth1UserHandler('pEgJoBA0XAxxYKHKDT4MRcrCW', 'nnSaF3vOkc45FmufiGCZQ6lV8Il3a8kde0urJd797ZdisX3mhE')
# auth.set_access_token('1052009251491770369-E9JuVtjqRKhQWnOCjOwe66mZamrcW3', 'IWYAvHjf1siydFKF5DOr1IIQXWCWoBr9bWM8TIU0l4wDw')
#
# api = tweepy.API(auth)
#
# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)
#
# api.me()  # it will display the info your self
# def limit_handle(cursor):
#     try:
#         while True:
#             yield cursor.next()
#     except tweepy.RateLimitError:
#         time.sleep(1000)
#
# #twitter has limited the access to server to avoid the crashing
#
# for follower in tweepy.cursor(api.get_followers): # to print the follwers name
#     print(follower.name)
#     if follower.name == 'aps@ghh': #if name is this then follow that user
#         follower.follow()
#
# search_st = 'python'
# numberOfTweets = 2
# for tweet in tweepy.cursor(api.search_tweets, search_st):
#     try:
#         tweet.favorite()
#         print('i liked that tweet')
#     except tweepy.TweepyException as e:
#         print(e.reason)
#     except StopIteration:
#         break


#-----------------SMS----------------

# # to send the text messages to your self
# # Download the helper library from https://www.twilio.com/docs/python/install
# import os
# from twilio.rest import Client
#
# # Set environment variables for your credentials
# # Read more at http://twil.io/secure
# account_sid = "AC888a8238521502f2dfb5dc5d506aed21"
# auth_token = "d9e19db189a1c94ee131b5cddf51d2cb"
# client = Client(account_sid, auth_token)
#
# message = client.messages.create(
#   body="Hello Kand Singh, How are you buddy",
#   from_="+14846624066",
#   to="+14319999021"
#   #to="+12049633976"
# )
#
# print(message.sid)

#--------------------Scrapping--------------------

import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/newest')
res2 = requests.get('https://news.ycombinator.com/newest?p=2')  # for page 2
#print(res)
soup = BeautifulSoup(res.text, 'html.parser') #parses the data
#print(soup) # it will print the html (page) source info

#print(soup.body) # it will print the body of page
#print(soup.body.contents)
#print(soup.find_all('div')) #find out all the div displayed on page
#print(soup.find_all('a'))  # find out the a tags
#print(soup.title) # it will print the title of page
# print(soup.a) # it will print first a tag
# print(soup.find('a')) # it will print the first a tag like last command
#print(soup.find(href="https://elkue.com/nyc-slice/"))
#print(soup.select('a'))

#links = soup.select('.storylink') # it will return the class links

votes = soup.select('.score')
# print(votes[1])
# print(votes[1].get('id'))
# print(votes[1].attrs)

links = soup.select('subline')
print(links)

subtext = soup.select('.subtext')
print(subtext)

def sort_stories_by_vote(hnlist):
    return sorted(hnlist, key= lambda k:k['votes'], reverse=True)

def create_custom_hn(links, subext):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(votes[0].getText().replace(' ponits', ''))
            if points>99:
                hn.append({'title': title, 'link': href, 'votes' : points})
    return sort_stories_by_vote(hn)

pprint.pprint(create_custom_hn(links, subtext))















