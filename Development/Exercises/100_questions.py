#import Fibonacci #to import the module from same folder
#import Development.exercis  # to import exercis outside the folder


#Question 1
#Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).The numbers obtained should be printed in a comma-separated
# sequence on a single line.

# number = range(2000,3201)
# lis = []
# for item in number:
#     if(item%7 == 0 and item%5 != 0):
#         lis.append(item)
# print(lis)2

#Question 2
#Write a program which can compute the factorial of a given numbers.The results should be printed in a
# comma-separated sequence on a single line.Suppose the following input is supplied to the program: 8
# Then, the output should be:40320

# n = int(input("enter the num "))
#
# fact = 1
# i = 1
#
# while i <= n:
#     #3
#     fact = fact * i #3
#     i = i + 1
# print(fact)

#Question 3
#With a given integral number n, write a program to generate a dictionary that contains (i, i x i) such
# that is an integral number between 1 and n (both included). and then the program should print the
# dictionary.Suppose the following input is supplied to the program: 8
#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

# dict = {}
# num = int(input("Enter the dictionary value"))
#
# for item in range (num):
#     dict[item] = item*item
# print(dict)


#Question 4

#Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple
#which contains every number.Suppose the following input is supplied to the program:
# input 34,67,55,33,12,98
#output
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')
#
# inp = input('enter the number').split(',')
# print(inp)


#Question 5
# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

# class IO():
#     def get_string(self):
#        self.s = input("enter the string")
#
#     def print_string(self):
#         print(self.s.upper())
#
# get = IO()
# get.get_string()
# get.print_string()

#Question 6

# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 _ C _ D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.
# For example Let us assume the following comma separated input sequence is given to the program:
# from math import sqrt
# def square_root(num):
#     c = 50
#     h = 30
#     q = sqrt((2*c*num/h))
#     return round(q)

#print(square_root(180))

# for i in [100,150,180]:
#     print(square_root(i))

# D = input("enter the values ").split(',')   # splits in comma position and set up in list
#D = [str(round(square_root(int(i)))) for i in D]  # using comprehension method. It works in order of the previous code
#print(",".join(D))
# for i in D:
#         D = [str(round(square_root(int(i))))]
#         #print(ab)
#         print(",".join(D))


#Question 7
#_Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
# The element value in the i-th row and j-th column of the array should be i _ j.*
# Note: i=0,1.., X-1; j=0,1,¡­Y-1. Suppose the following inputs are given to the program: 3,5
# Then, the output of the program should be:
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]

# x,y = map(int,input("please enter here -->").split(','))
# lst = []
# #print(x, y)
# for i in range(x):  # 0 1
#     tmp = []
#     for j in range(y): # 0 range(4) 0 1
#         tmp.append(i*j) #0 0 1
#     lst.append(tmp)
#
# print(lst)

#Question 8
#Write a program that accepts a comma separated sequence of words as input and prints the words
# in a comma-separated sequence after sorting them alphabetically.
#Suppose the following input is supplied to the program:
#
# inp = input("enter the values").split(",")
# inp.sort()
# print(inp)


# Question 9
#Write a program that accepts sequence of lines as input and prints the lines after making all
# characters in the sentence capitalized.
#Suppose the following input is supplied to the program:
#Hello world
#Practice makes perfect
#Then, the output should be:
# HELLO WORLD
# PRACTICE MAKES PERFECT



# solution 1
# inp = input("enter the values")
# #inp.upper()
# print(inp.upper())



#---solution 2
# lst = []
# while True:
#     x = input("enter the value here")
#     if len(x)==0:
#         break
#     lst.append(x.upper())
#
# for line in lst:
#     print(line)

#Question 10
#Write a program that accepts a sequence of whitespace separated words as input and prints the words
# after removing all duplicate words and sorting them alphanumerically.
# Suppose the following input is supplied to the program:
# hello world and practice makes perfect and hello world again
# Then, the output should be:
# again and hello makes perfect practice world

# x = input("enter the value here").split()
#
# print(x)
#
# for i in x:
#     if x.count(i) >1:
#         x.remove(i)
#
# x.sort()
# print(" ".join(x))

#2nd solution
# x = sorted(list(set(input("enter here : ").split())))
# print(x)


#Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and
# then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
# 0100,0011,1010,1001
# Then the output should be:
# 1010
