s1={3,89,8.7,"true",45}
s2={45,"carla"}
s1=s2=s1.symmetric_difference(s2)
print(s1)
print(s2)
# you also use multiple assignments (s1 = s2 = ...) in a single line. In Python, when you use multiple assignments like this, the value on the right side is assigned to both variables (s1 and s2).
 
# symmetric_difference(s2) operation is performed on the original s1 set, which results in a new set containing elements that are in either s1 or s2, but not in both. This set is returned by the method call. 