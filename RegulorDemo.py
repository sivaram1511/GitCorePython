import re
match=re.finditer("\D","ab 2576@ XHSs nkLAKAJ.")
for m in match:
    print(m.start(),m.group())
