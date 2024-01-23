#if-else function
#1
temp=float(input("Enter the temperature: "))
if temp >= 40 and temp <=50:
  print("it is too hot today!")
  print("take enough fluids.")
elif temp>=30:
  print("It is awesme today!")
elif temp <=20:
  print("It's cool")
elif temp >30 and temp <40:
  print("It is hot today!")
else:
  print("Enjoy whatever it is!")

#2
#Write a program to enter a user choice for selecting a specialization in SoCS.
percent=float(input("Enter your entrance exam percentage: "))
if percent>=90 and percent <=100:
  print("You can choose:\n1.AI/ML\n2.Data Science")
elif percent >=80 and percent<90:
  print("You can choose:\n1.Cybersecurity\n2.Cloud Computing")
elif percent>=50 and percent<80:
  print("You can choose:\n1.Gaming")
else:
  print("You are not eligible for any CoSC course.\nThank you. ")

#3
#weight conversion example
weight=float(input("Enter the weight: "))
unit=input("K(g) or L(bs): ")
if unit.upper() == "K":
  weight=weight//0.45
  print("The output in Lbs is:",weight)
else:
  weight=weight*0.45
  print("The output in Kgs is:",weight)

#4
#Write a program to modify above example to convert Kgs into gms.
weight=float(input("Enter the weight: "))
unit=input("K(gs) or G(ms)?\nChoose 'K' or 'G': ")
if unit.upper()=="K":
  weight=weight*1000
  print("The weight in G(ms) is:",weight)
elif unit.upper()=="G":
  weight=weight//1000
  print("The weight in K(gs) is:",weight)
else:
  print("Only K(gs) to G(ms) or vice versa conversion allowed")



#While Loops
#1
i=0
while(i<=10):
  print(i*"*")
  i+=1
print("something")

#2
i=10
while(i>=1):
  print(i*"*")
  i-=1
print("something")


#3
#Write a program to check whether a number guessed by the user is the correct or not.

a = 7
i = 0
while (i<3):
  guess=int(input("Try to guess a number"))
  if guess==a:
    print("You've guessed the correct number")
    break
  else:
    print("Try again")
    i+=1
if i==3:
  print("You Lose!")


#Another(Better) way to write code for the problem above

sec_num=7
guess_count=0
guess_limit=3
while guess_count<guess_limit:
  guess=int(input("Guess: "))
  guess_count+=1
  if guess==sec_num:
    print("Correct!")
    break
else:
  print("Sorry You Failed!")
