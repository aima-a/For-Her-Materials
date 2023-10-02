'''Append new string in the middle of a given string Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1. '''
s1 = 'Aulto'
s2 = 'Kelly'
result = 'AuKellylt'
'''str1 = input('Enter first string: ') # Inputs'''
'''str2 = input('Enter second string: ')'''


def mid_3_inserter(str1, str2):  # Define function
    mid_index = len(str1) // 2
    new_string = str1[0:mid_index] + s2 + str1[mid_index:]
    print(new_string)


mid_3_inserter(s1, s2)
