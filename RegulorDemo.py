import re
match=re.finditer("\W","abc@ SIVA 09865 hijkl .**")
for m in match:
    print(m.start(),m.group())
