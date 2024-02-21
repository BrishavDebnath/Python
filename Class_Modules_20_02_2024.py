def num_append(num):
  str=input("Enter string you want to input:")
  num.append(str)
  return num

def num_insert(num):
  str1=input("Enter string to insert:")
  n=int(input("Enter the index at which to insert the string:"))
  num.insert(n,str1)
  return num

def num_remove(num):
  n=int(input("Specify index to remove string:" ))
  del num[n]
  return num