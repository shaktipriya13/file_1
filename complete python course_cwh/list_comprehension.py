lst=[1,2,3,4,5]
n=[i for i in lst]
print(n)

m=[i*i for i in lst]
print(m)

name=["rakhi","rome","omi","sumy"]
n_with_o=[i for i in name if 'o' in i]
print(n_with_o)

m4=[i for i in name if (len(i)>=4)]
print(m4)