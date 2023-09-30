#wap to check whether all characters present in string are alphanumeric.if yes,print true else false.
s = input("Enter string:")
lc = "abcdefghijklmnopqrstuvwxyz"
uc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ns = "1234567890"
flag = 1 

for i in s:
    if i not in lc and i not in uc and i not in ns:
        flag = 0
        break  if flag == 1:
    print("String is alphanumeric")
else:
    print("String is not alphanumeric")

    
    
        




