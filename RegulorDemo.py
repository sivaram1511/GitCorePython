import re
match=re.finditer("[abc]","abbabababbbabb")
for m in match:
    print(m.start(),m.end(),m.group())
