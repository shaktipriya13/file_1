dic={"name":"harry","age":15,"class":6,"gender":"m"}
# print(dic.keys())
# print(dic.values())

for i in dic.keys():
    print(i)
print("------")
for i in dic.keys():
    print(dic[i])


for i in dic.keys():
    print("value correspomding to key-{key} is {dic[key]}")
#dictionary works
ep1={5:90,8:67,4:78}
ep2={1:89,2:78,3:56}
e=ep1
d=ep1.copy()
d.update({"an":9})
e.update({"an":9})
print(d)
print(e)
print(ep1)