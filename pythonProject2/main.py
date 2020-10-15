import re
string="I'm not yelling at you "
print(string)
new=re.sub('[A-Z]','',string)
print(new)
new2=re.sub('[a-z]','',string)
print(new2)
new3=re.sub('[" "]','',string)
print(new3)
string=string +"678-231"
new4=re.sub('[^0-9]','',string)
print(new4)
