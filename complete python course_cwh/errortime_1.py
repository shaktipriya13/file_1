s={"shakti",9,6.8}
for i in s:
    s.remove(i)
print(s)

# The error you're encountering is because you're modifying the set `s` while iterating over it with a `for` loop. Modifying a collection while iterating over it can lead to unexpected behavior and errors in Python.

# When you remove an element from the set within the loop using `s.remove(i)`, it affects the iteration and the internal state of the set. As a result, you may encounter errors such as "RuntimeError: Set changed size during iteration" or "RuntimeError: dictionary changed size during iteration," depending on the version of Python you're using.

# To remove all elements from the set, you should not modify the set while iterating over it. Instead, you can create a copy of the set and then clear the original set:

s = {"shakti", 9, 6.8}
s_copy = s.copy()  # Create a copy of the set
for i in s_copy:
    s.remove(i)     # Remove elements from the original set

print(s)  # Output: set()

#think


# In this code, we iterate over the copy of the set `s_copy` and remove elements from the original set `s`. This avoids modifying the set while iterating and prevents the error.