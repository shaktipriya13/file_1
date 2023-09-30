l1 = [4, 8, 9, 0, 3]
t1 = (4, 8, 9, 0, 3)

results = ["True" if i == j else "False" for i, j in zip(l1, t1)]
print(results)


print('\nwithout zip function\n')
l1 = [4, 8, 9, 0, 3]
t1 = (4, 8, 9, 0, 3)

results = ["True" if i == j else "False" for i in l1 for j in t1]
#here above no "and" is used and 2 for's are used.
print(results)

#these above methods are called list comprehension
