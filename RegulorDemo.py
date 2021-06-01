import re
s=input("Enter the pattern to check..")
m=re.match(s,"abcdscdracbsvg")
if m!=None:
    print(m.start(),m.group())
else:
    print("not matched")
