import re
str_1 = re.findall('\w','aBcdef_*()-=')
str_2 = re.findall('\W','aBcdef_*()-=')
print(re.findall('alex$','alexalexiialex alex'))



print(re.findall('a.b','a baaa b a ab a badb aa\nbba\tb',re.DOTALL))