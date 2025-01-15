#!/usr/bin/env python
# coding: utf-8

# In[1]:


## 1. print name ,student number, gmail id
print("Muhsina")
print("ST1012")
print("muhsina@gmail.com")


# In[2]:


## 2.Write Python code that prints your name, student number and email address using escape sequences. 
print("Muhsina\nST1012\nmuhsina@gmail.com")



# In[3]:


## 3. Write Python code that add, subtract, multiply and divide the two numbers. You can use the two numbers 14 and 7. 
a = 14
b = 7
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")


# In[4]:


## 4. Write Python code that displays the numbers from 1 to 5 as steps. 
for i in range(1, 6):
    print(i)


# In[5]:


## 5. Write Python code that outputs the following sentence (including the quotation marks and line break) to the screen
print("\"SDK\" stands for \"Software Development Kit\",\nwhereas \"IDE\" stands for \"Integrated Development Environment\".")


# In[8]:


## 6. Practice and check the output
print("python is an \"awesome\" language.")


# In[7]:


print("python\n\t2023")


# In[9]:


print('I\'m from Entri.\b')


# In[10]:


print("\65")


# In[11]:


print("\x65")


# In[12]:



print("Entri", "2023", sep="\n")


# In[13]:


print("Entri", "2023", sep="\b")


# In[25]:


print("Entri", "2023", sep="*", end="\b\b\b\b")


# In[26]:


## 7. Define the variables below. Print the types of each variable. What is the sum of your variables? 
##(Hint: use a type conversion function.) What datatype is the sum?

num = 23
textnum = "57"
decimal = 98.3

print(type(num))
print(type(textnum))
print(type(decimal))

sum_variables = num + int(textnum) + decimal
print("Sum:", sum_variables)
print("Type of sum:", type(sum_variables))


# In[27]:


## 8. calculate the number of minutes in a year using variables for each unit of time

# Define the variables
days_in_a_year = 365
minutes_in_hour = 60
hours_in_day = 24

# Calculate the total minutes in a year
total_minutes_in_a_year = days_in_a_year * hours_in_day * minutes_in_hour

# Print the result
print(f"The total number of minutes in a year is: {total_minutes_in_a_year}")


# In[29]:


## 9. Write Python code that asks the user to enter his/her name and then output/prints his/her name with a greeting.
name = input("Please enter your name: ")
print(f"Hi {name}, welcome to the programming world ")


# In[30]:


## 10. Write a program that asks the user to enter an amount in pounds (£) 
## and the program calculates and converts an amount in dollar ($)

pounds = float(input("Please enter amount in pounds: "))
dollars = pounds * 1.37  # Example conversion rate
print(f"£{pounds} are ${dollars:.2f}")


# In[ ]:




