print("Operations on strings")
print("Concatenating two strings")
str1=input("Enter first string:")
str2=input("Enter second string:")
str3=str1+str2
print("Concatenated string:",str3)
print("\n")
print("Appending two strings")
str4=input("Enter a string:")
str5=input("Enter a string to be appended:")
str4+=str5
print("Appended string is:",str4)
print("\n")
print("Multiplying strings")
str6=input("Enter a string:")
n=int(input("Enter number of times to multiply the string:"))
print(str6*n)
print("\n")
print("Converting a string into lowercase")
str7="HELLO WORLD"
print("Before conversion:",str7)
print("After Conversion:",str7.lower())
print("\n")
print("Converting a string into uppercase")
str8="hello world"
print("Before Conversion:",str8)
print("After Conversion:",str8.upper())
print("\n")
print("Finding a substring in a string")
str9=input("Enter a string:")
str10=input("Enter substring:")
print(str9.find(str10,0,len(str9)))
print("\n")
print("Replacing a substring in a given string")
str11="Python for programming"
print("Before replacing:",str11)
print("After replacing:",str11.replace("for","4"))
print("\n")
print("Swapping cases of characters in a given string")
str12=input("Enter a string:")
print("Swapping cases,we get:",str12.swapcase())
print("\n")
print("Length of a String")
str13=input("Enter a string:")
print("Length of the entered string is:",len(str13))