name: str = 12
name2: str = 'Alexxx'
name3: str = 'Garryx'

print(name, name2, name3)


alist = name, name2

print(alist)

blist = name3, *alist

print(blist)