# -*- coding: utf-8 -*-

# -- Sheet --

# Problem 1: Lists, Sets and Coercion
#1.a Create a list of integers no fewer than 10 items from 0 to 9.

one_a = [5, 6, 7, 2, 3, 6, 9, 2, 1, 7, 7, 7, 1]
print(one_a)
one_b = one_a[4] + 3
print(one_b)
one_c = [float(x) for x in one_a]
print(one_c)
one_d = set(one_a)
print(one_d)

# 1.e Using a method, append int 10 to the set
one_e = one_d.add(10)
print(one_e)
    # I'm a little confused why this returns 'None'
# 1.f Using a method, pop an item from the set
one_f = one_d.pop()
print(one_d)
# 1.g Using a length counting function, count the number of items in the set
one_g = len(one_d)
print(one_g)
# 1.h Check if the number of items in the set is the same as the number of items in the list
one_h = len(one_d) == len(one_a)
print(one_h)

