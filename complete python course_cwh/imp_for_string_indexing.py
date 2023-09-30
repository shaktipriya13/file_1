a=input("enter your msg:")
temp=a
print(len(a))
for i in a:
    k=len(a)-i-1
    a[i]=temp[k]
print(a)

    # print(i," ")
# for i in a:
#     if(len(i)<3):

# When iterating through the characters of a string, i takes on the characters themselves, not their indices. So, you should use enumerate(a) to get both the character and its index.

# You cannot assign a value to a character within a string in Python because strings are immutable. Instead, you can create a new string to store the reversed version.
