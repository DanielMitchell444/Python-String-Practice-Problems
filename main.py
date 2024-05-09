##Inside this file, you will be doing a variety of coding problems
##associated with strings. If you have any questions, please ask
## me and i will be happy to answer it

"""
PRACTICE PROBLEM 1:
Given a string, return the string made of its first two chars, 
so the String "Hello" yields "He". If the string is shorter than length 2, 
return whatever there is, so "X" yields "X", 
and the empty string "" yields the empty string "".


first_two('Hello') → 'He'
first_two('abcdefg') → 'ab'
first_two('ab') → 'ab'

Please type your answer inside the function below
"""

def first_two(str):
  print("hello") 
  

"""
PRACTICE PROBLEM 2:
Given two strings, a and b, return the result of putting them together in the order abba, e.g. "Hi" and "Bye" returns "HiByeByeHi".


make_abba('Hi', 'Bye') → 'HiByeByeHi'
make_abba('Yo', 'Alice') → 'YoAliceAliceYo'
make_abba('What', 'Up') → 'WhatUpUpWhat'
"""

def make_abba(a,b):
  print("hello")


"""
PRACTICE PROBLEM 3:

Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".


hello_name('Bob') → 'Hello Bob!'
hello_name('Alice') → 'Hello Alice!'
hello_name('X') → 'Hello X!'
"""


"""
Practice Problem 4:
we have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling. We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.


monkey_trouble(True, True) → True
monkey_trouble(False, False) → True
monkey_trouble(True, False) → False
"""

"""
PRACTICE PROBLEM 5:

Given a string, return a version without the first and last char, so "Hello" yields "ell". The string length will be at least 2.


without_end('Hello') → 'ell'
without_end('java') → 'av'
without_end('coding') → 'odin'
"""

"""
Practice Problem 6:
The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.


sleep_in(False, False) → True
sleep_in(True, False) → False
sleep_in(False, True) → True
"""

##After you complete this, you will take a 5 minute break and
##then we will be moving onto more string methods.