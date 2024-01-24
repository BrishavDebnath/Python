#Write a program to show whether a car has started or stopped
cmd=""
repeat=False
while (cmd.upper() != "EXIT"):
  cmd=input("Choose:\n1.Start\n2.Stop\n3.Help\n4.Exit\n")
  if cmd.upper()=="START":
    if repeat==True:
      print("The Car is already running! ")
    else:
      print("The Car has started!")
      repeat=True
  elif cmd.upper()=="STOP":
    if repeat==True:
       print("The car has stopped")
    else:
      print("The car has already stopped")
      repeat=False
  elif cmd.upper()=="HELP":
    print("1.start=Car will start\n2.Stop=Car will start\n3.Exit=To exit the program")
  elif cmd.upper()=="EXIT":
    print("Thanks for playing!")
    break
  else:
    print("Sorry, I dont understand the command")