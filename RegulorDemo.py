import re
match=re.finditer("a*","abc@ SIVAa 09865a hijkl .**")
for m in match:
    print(m.start(),m.group())
