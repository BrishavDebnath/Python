#1. Write a program to append the numbers in a list and after that print whether the numbers are even or odd.
list_1=[i for i in range(1,21)]
print(list_1)
for i in range(0,20):
  if list_1[i]%2==0:
    print("list_1["+str(i)+"]"+"is even and is :",list_1[i])
  else:
    print("list_1["+str(i)+"]"+"is odd and is :",list_1[i])



#2. Extract letters from a string. The string is "Welcome to the world of python" and put them in a list.
str_2="Welcome to the World of Python!"
list_3=[i for i in str_2]
print(list_3)


#3. Write a program to create a tuple and add 10 values to it and print all those values using a for loop.
tuple_1 = (22, 33, 44, "Brishav", "Ninety", 67, 12, "Hello", 66, "World")
for i in range(0, 10):
  print(tuple_1[i])
