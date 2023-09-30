#wap to count the total no. of occurences of specific characters in the given string using for loop.
s=input("enter string:")
c=input("enter character to find in string:")
n=0
for i in s:
    if(c==i):
        n+=1

print("total no. of occurences=",n)
        
