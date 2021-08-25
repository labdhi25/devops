import re
x=input("Enter  Name :")
if re.search("\d",x):
  raise Exception("Name not entered in prescribed format")
else :
    print("Your name is ",x)
