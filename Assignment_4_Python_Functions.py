#!/usr/bin/env python
# coding: utf-8

# 1.What does the len() function do in Python? Write a code example using len() to find the length of a list?
#    
#   len() Function
# The len() function in Python returns the number of items in an object. The object can be a list, string, dictionary, etc. 

# In[1]:


# Example to find the length of a list
list = [1, 2, 3, 4, 5]
length_of_list = len(list)
print("Length of the list:", length_of_list)


# 2.Write a Python function greet(name) that takes a person's name as input and prints "Hello, [name]!".
# 

# In[4]:


def greet(name):
    print(f"Hello, {name}!")
    
greet("Usam")


# 3.Write a Python function find_maximum(numbers) that takes a list of integers and returns the maximum value without using the built-in max() function. Use a loop to iterate through the list and compare values.

# In[7]:


def find_maximum(numbers):
    if not numbers:
        return None
    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value

# Example 
numbers = [35, 55, 22, 49, 61]
print("Maximum value:", find_maximum(numbers))


# 4.Explain the difference between local and global variables in a Python function. Write a program where a global variable and a local variable have the same name and show how Python differentiates between them.
# 

# In[ ]:


Local Variables: These are variables declared inside a function and can only be accessed within that function.
                 They are created when the function is called and destroyed when the function exits.


# Global Variables: These are variables declared outside any function and can be accessed and 
#                   modified inside functions using the global keyword.

# In[8]:


# Global variable
x = 10

def my_function():
    # Local variable
    x = 5
    print("Inside the function, x =", x)

my_function()
print("Outside the function, x =", x)


# 5.Create a function calculate_area(length, width=5) that calculates the area of a rectangle. If only the length is provided, the function should assume the width is 5. Show how the function behaves when called with and without the width argument.
# 

# In[9]:


def calculate_area(length, width=5):
    return length * width


print("Area with length 10 and default width:", calculate_area(10))
print("Area with length 10 and width 7:", calculate_area(10, 7))


# In[ ]:




