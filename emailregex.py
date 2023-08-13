import re

conditions="^[a-z]+[\._]?[a-z 0-9]+[@\w]+[.]\w{2,3}$"

email=input("Enter your Email : ")

if re.search(conditions,email):
    print("Your email is verified")
    
else:
    print("Invalid Email")