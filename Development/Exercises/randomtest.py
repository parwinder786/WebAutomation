#from Development.Extra.otherpackage.method import hello
import Development.Extra.otherpackage.method

#print(hello())

#other way of importing it

from Development import *
#import * will import everything
print(Development.Extra.otherpackage.method.hello())

print(__name__)

# def number(num):
#     print(num)
#     #yield
#     #print('ahhah')
#
# number(33)