#Basic Arithmetic Operations

a=float(input("Enter the first variable:\n"))
b=float(input("Enter the second variable:\n"))
c=a+b
d=a-b
e=a*b
f=a/b
g=a%b
h=a//b
i=a**b
print("The addition is:",c)
print("The subtraction is:",d)
print("The multiplication is :",e)
print("The division is:",f)
print("The remainder after dividing the first variable from the second is:",g)
print("The quotient after dividing the first variable from the second is:",h)
print("The first variable raised to the power of second is:",i)


#Logical and Boolean Operations
#1
a=10
if not a:
  print("Boolean value of a is true")
if not (a%3==0 or a%5==0):
  print("10 is divisible by either 3 or 5")
else:
  print("10 is divisible by either 3 or 5")


#2
a=10
if  a:
  print("Boolean value of a is true")
if  (a%3==0 or a%5==0):
  print("10 is divisible by either 3 or 5")
else:
  print("10 is divisible by either 3 or 5")



#3
def order(x):
  print("Method called for value:",x)
  return True if x>0 else False
a=order
b=order
c=order
if a(-1)or b(5) or c(10):
  print("Atleast one of them is positive")

#4
temp=30
print(temp>5 and temp<10)
print(temp>40 or temp<=30)
print( not temp==30)
print(type(temp))

#5
temp=30
print(temp>5 and temp<10)
print(temp>40 or temp<=30)
print( not temp==30)
print(type(temp))  #finding type of a data type


#6
temp=float(input("Enter the temperature: "))
if temp >= 40 and temp <=50:
  print("it is too hot today!")
  print("take enough fluids.")
elif temp>=30:
  print("It is awesome today!")
elif temp <=20:
  print("It's cool")
elif temp >30 and temp <40:
  print("It is hot today!")
else:
  print("Enjoy whatever it is!")



#7
temp=float(input("Enter the temperature:"))
print(temp>5 and temp<10)
print(temp>30 or temp<=40)
print( not temp==30)
print(type(temp))
print(round(temp)) #to round off floating point numbers



#Bitwise Operations
a=10
b=4
print(a&b) #Bitwise and
print(a|b) #Bitwise or
print(a^b) #Bitwise xor
print(a>>1) #Bitwise right shift
print(a<<1) #Bitwise Left shift
print(~a) #Bitwise NOT
print(~b) #Bitwise NOT
