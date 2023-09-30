# The `enumerate` function in Python is a built-in function that is used to iterate over an iterable (e.g., a list, tuple, or string) while keeping track of the index (position) of the current item. It returns a tuple containing both the index and the item at that index in each iteration.

# While the output of the enumerate function doesn't display parentheses explicitly, it indeed generates tuples. In Python, tuples are often created without requiring parentheses for simplicity, especially when used in iterable contexts.

# The primary use cases for `enumerate` are:



# 1. **Simplify Looping with Indices:** Instead of using a traditional `for` loop to iterate through the elements of a sequence and manually keeping track of the index(manually tracking index mtlb jo bar bar index ko increment krna parta ha), you can use `enumerate` to do this more concisely.


fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")
# on swapping fruit and index...o/p changes
fruits=["mango","peas","apple"]
for fruit,index in enumerate(fruits):
    print(f"index {index} --- fruit {fruit}")
 

#    Output:
#    ```
#    Index 0: apple
#    Index 1: banana
#    Index 2: cherry
#    ```

# 2. **Accessing Index and Value Simultaneously:** It allows you to access both the index and the value of elements in the iterable simultaneously, which can be useful for various tasks, such as updating elements based on their position.


numbers = [10, 20, 30, 40, 50]
for index, value in enumerate(numbers):
    numbers[index] = value * 2
   

#    After this loop, `numbers` will be `[20, 40, 60, 80, 100]`.

# 3. **Creating Dictionaries or Maps:** You can use `enumerate` to create dictionaries or maps where the index serves as the key and the elements of the iterable serve as values.

   
fruits = ['apple', 'banana', 'cherry']
fruit_dict = {index: fruit for index, fruit in enumerate(fruits)}

#example 2
lst=[8,9,3,5]
dic={index:num*2 for index,num in enumerate(lst)}
print(dic)

#here,  The provided code is a Python dictionary comprehension that creates a dictionary named fruit_dict based on the fruits list using the enumerate function. 


#  fruit_dict will be `{0: 'apple', 1: 'banana', 2: 'cherry'}`.

# In summary, `enumerate` is a convenient tool in Python for iterating over sequences while maintaining the index information, making your code more readable and efficient when you need to work with both the elements and their positions in the sequence.