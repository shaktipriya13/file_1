def concatenate(*args):
    res=" "
    for str in args:
        res=res+str+" "
        # res+=str+" "....we acn also write this.
    print(res)
concatenate("hi","my","name","is","shakti")
#. The final output is the concatenation of all the input strings.
# The arguments are collected into a tuple.
#in variable length keyword arguments,*args are used for positional arguments 
# alt+z for word wrap
#also read: Combining *args and **kwargs:
