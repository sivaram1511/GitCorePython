import re
p=input("Enter phone number")
m=re.fullmatch("[7-9][0-9]{9}",p)
if m!=None:
    print("Valid number is ",p)
else:
    print("invalid number")


