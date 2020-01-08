#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'MiracleWong'

# 20 Python Snippets You Should Learn Today
# 地址：https://medium.com/better-programming/20-python-snippets-you-should-learn-today-8328e26ff124

import sys
import time
import random
from collections import Counter
from iteration_utilities import deepflatten

# 1. Reversing a String
# Reversing a string using slicing
my_string = "ABCDE"
reversed_string = my_string[::-1]

print(reversed_string)

# 2. Using rhe Title Case (First Letter Caps)
my_string = "my name is chaitanya baweja"

# using the title() function of string class
new_string = my_string.title()

print(new_string)

# 3. Finding Unique Elements in a String
my_string = "aavvvvccccdddddee"

temp_set = set(my_string)
new_string = ''.join(temp_set)

print(new_string)

# 4. Printing a String or a List n Times
n = 3  # number of repetitions

my_string = "abcd"
my_list = [1, 2, 3]
my_list1 = [0]
print(my_string * n)
# abcdabcdabcd

print(my_list * n)
# [1,2,3,1,2,3,1,2,3]
print(my_list1 * n)

# 5. List Comprehension
original_list = [1, 2, 3, 4]

new_list = [2 * x for x in original_list]

print(new_list)
# [2,4,6,8]

# 6. Swap Values Between Two Variables
a = 1
b = 2
a, b = b, a
print(a)
print(b)

string_1 = "My name is Chaitanya Baweja"
string_2 = "sample/ string 2"

# 7. Split a String Into a List of Substrings
# default separator ' '
print(string_1.split())
# ['My', 'name', 'is', 'Chaitanya', 'Baweja']

# defining separator as '/'
print(string_2.split('/'))
# ['sample', ' string 2']

list_of_strings = ['My', 'name', 'is', 'Miracle', 'Wong']

print(' '.join(list_of_strings))

# 回文
my_string = "abcba"

if my_string == my_string[::-1]:
    print("palindrome")
else:
    print("not palindrome")

my_list = ['a', 'a', 'b', 'b', 'b', 'c', 'd', 'd', 'd', 'd', 'd']
count = Counter(my_list)  # defining a counter object

print(count)
print(count['b'])
print(count.most_common(1))

str_1, str_2, str_3 = "acbde", "abced", "abcda"
cnt_1, cnt_2, cnt_3 = Counter(str_1), Counter(str_2), Counter(str_3)

if cnt_1 == cnt_2:
    print('1 and 2 anagram')
if cnt_1 == cnt_3:
    print('1 and 3 anagram')

a, b = 1, 0

try:
    print(a / b)
    # exception raised when b is 0
except ZeroDivisionError:
    print("division by zero")
else:
    print("no exceptions raised")
finally:
    print("Run this always")

# 13. Using Enumerate to Get Index/Value Pairs
my_list = ['a', 'b', 'c', 'd', 'e']

for index, value in enumerate(my_list):
    print('{0}: {1}'.format(index, value))

num = 21

print(sys.getsizeof(num))

dict_1 = {'apple': 9, 'banana': 6}
dict_2 = {'banana': 4, 'orange': 8}

combined_dict = {**dict_1, **dict_2}

print(combined_dict)

start_time = time.time()
# Code to check follows
a, b = 1, 2
c = a + b
# Code to check ends
end_time = time.time()
time_taken_in_micro = (end_time - start_time) * (10**6)

print(" Time taken in micro_seconds: {0} ms".format(time_taken_in_micro))


# if you only have one depth nested_list, use this
def flatten(l):
    return [item for sublist in l for item in sublist]


l = [[1, 2, 3], [3]]
print(flatten(l))
# [1, 2, 3, 3]

# if you don't know how deep the list is nested
l = [[1, 2, 3], [4, [5], [6, 7]], [8, [9, [10]]]]

print(list(deepflatten(l, depth=3)))

# 18. Sampling From a List
my_list = ['a', 'b', 'c', 'd', 'e']
num_samples = 2

samples = random.sample(my_list, num_samples)
print(samples)

# 19. Digitize
num = 123456

list_of_digits = list(map(int, str(num)))

print(list_of_digits)

# [1, 2, 3, 4, 5, 6]


# 20. Check for Uniqueness
def unique(l):
    if len(l) == len(set(l)):
        print("All elements are unique")
    else:
        print("List has duplicates")


unique([1, 2, 3, 4])
# All elements are unique

unique([1, 1, 2, 3])
# List has duplicates