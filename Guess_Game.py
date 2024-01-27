a = 7
i = 1
while (i<=3):
  guess=int(input("Guess a Number:\n"))
  if guess==a:
    print("Congrats! You win!")
    break
  else:
    if i==3:
      break
    print("Wrong Guess! Try again!")
    i+=1
if i==3:
  print("You Lose!")
