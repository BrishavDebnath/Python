#1 Write a program to iterate two s strings.
str1=input("Enter first String:")
str2=input("Enter second string:")
l1=len(str1)
l2=len(str2)
for i in range(0,l1):
  print(str1[i])
print("\n")
for i in range(0,l2):
  print(str2[i])



#2 Write a Program to print the tables starting from 2 to 11
for i in range(2,12):
 print("Multiplication table of ",i)
 for j in range(1,11):
  print(str(i)+"X"+str(j)+"="+str(i*j))
 print("\n")


#3 Write a program to move through a list
n=int(input("Enter number of items in your list:\n"))
my_list=[]
for i in range(0,n):
  my_list.append(input("Enter list"+"["+str(i)+"]"+":"))
print("Your list is:\n ")
for i in range(0,n):
  print("List"+"["+str(i)+"]"+":"+my_list[i])
