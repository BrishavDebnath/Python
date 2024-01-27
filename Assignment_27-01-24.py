#Write a python program to display the multiplication table.(Use input function and for loop)
num=int(input("Enter a number:\n"))
print("Multiplication table of ",num)
for i in range(1,11):
  print(str(num)+"X"+str(i)+":"+str(num*i))
  int(num)
  int(i)

#Write a program to check whether a given number is a armstrong number or not.
num1=input("Enter a number:\n")
n=len(num1)
r=0
sum=0
num1=int(num1)
number=num1
while (number != 0):
  r=number%10
  sum=sum+r**n
  number=number//10
if num1==sum:
  print(num1,"is an Armstrong number.")
else:
  print(num1,"is not an Armstrong number.")



#Write a Program to find Armstrong number in an interval.
num2=int(input("Enter the first number of the interval:\n"))
num3=int(input("Enter the last number of the interval:\n"))
print("Armstrong Numbers in the given Interval are:\n")
for i in range(num2,num3+1):
  sum1=0
  r1=0
  i=str(i)
  n1=len(i)
  i=int(i)
  temp=i
  while(temp>0):
    r1=temp%10
    sum1=sum1+r1**n1
    temp//=10
  if sum1 == i:
    print(i," is a Armstrong Number.")


