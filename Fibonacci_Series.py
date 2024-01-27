#Write a program to generate Fibonacci series.
num=int(input("Enter a Number:\n"))
sum=0
a=0
b=1
print("Fibonacci Series:")
print(a)
for i in range(1,num+1):
  print(b)
  sum=a+b
  a=b
  b=sum
