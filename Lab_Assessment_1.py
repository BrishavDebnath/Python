# -*- coding: utf-8 -*-
"""Untitled11.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wM62JtPvZKj1LMi1rKWPTJvY5Jeyi-aS
"""

#Write a python function that takes a positive integer and returns the sum of the cube of all the positive integers smaller than the specified number.

def sum_of_cubes(n):
  sum=0
  for i in range(1,n):
    sum=sum+i**3
  return (sum)
num=int(input("Enter a positive integer:"))
print("The sum of cubes of all numbers smaller than specified number is:",sum_of_cubes(num))

#Write a function to print fibonacci series till n numbers.
def fibonacci(n):
  a=0
  b=1
  c=0
  print(a)
  print(b)
  for i in range(1,n):
    c=a+b
    a=b
    b=c
    print(c)
num=int(input("Enter a number:"))
print(fibonacci(num))

#Write a lambda function to find min max from a list.
def max_min(num):
  largest=0
  for i in num:
    if i>largest:
      largest=i
  min=1000000
  for i in num:
    if i<min:
      min=i
  return largest,min
list1=[12,11,23,43,45,66,87]
min_max=max_min(list1)
print(min_max)

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/drive/MyDrive/Colab Notebooks

!ls

!python main_c.py