str = input()
ind = str.find('h')
ind2 = str.rfind('h')
s = len(str)
print(str[0:ind], str[ind2 + 1:s], sep="")