salaries = {
    'siry':3000,
    'tom':7000,
    'jack':2000,
}






a = max(salaries,key=(lambda x:salaries[x]))
print(a)