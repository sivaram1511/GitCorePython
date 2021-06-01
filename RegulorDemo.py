import re
match=re.finditer("a$","caabc@ SIVAaaa 09865aaaa hijkl .**a")
for m in match:
    print(m.start(),m.group())
