#!/usr/bin/env python
# coding: utf-8

# # Topic :List
# Exercise
# 

# In[2]:


## Q1.Create a list of 5 random numbers and print the list.

import random

# Create a list of 5 random numbers
random_list = [random.randint(1, 100) for i in range(5)]
print("List of 5 random numbers:", random_list)


# In[3]:


## Q2.Insert 3 new values to the list and print the updated list.

new_values = [101, 102, 103]
random_list.extend(new_values)
print("Updated list with new values:", random_list)


# In[4]:


# 3.Try to use a for loop to print each element in the list.

for number in random_list:
    print(number)


# # Topic: Dictionary
# Exercise 
# 

# In[5]:


#Q1. Create a dictionary with keys 'name', 'age', and 'address' and values 'John', 25, and 'New York' respectively.
# Create the dictionary
person_dict = {
    'name': 'John',
    'age': 25,
    'address': 'New York'
}
print("Dictionary:", person_dict)


# In[7]:


# Q2.Add a new key-value pair to the dictionary created in Q1 with key 'phone' and value '1234567890'

# Add a new key-value pair to the dictionary

person_dict['Phone'] = '1234567890'
print("Updated dictionary:", person_dict)


# # Topic: Set
# Exercise  
# 

# In[8]:


# Q1.Create a set with values 1, 2, 3, 4, and 5.

number_set = {1, 2, 3, 4, 5}
print("Set:", number_set)


# In[9]:


# Q2. Add the value 6 to the set created in Q1.

number_set.add(6)
print("Updated set with value 6:", number_set)


# In[10]:


# Q3. Remove the value 3 from the set created in Q1.

number_set.remove(3)
print("Updated set without value 3:", number_set)


# # Topic:Tuple
# Exercise 
# 

# In[12]:


# Q1. Create a tuple with values 1, 2, 3, and 4

num_tuple = (1, 2, 3, 4)
print("Tuple:", num_tuple)


# In[13]:


# Q2. Print the length of the tuple created in Q1.


tuple_length = len(num_tuple)
print("Length of the tuple:", tuple_length)


# In[ ]:




