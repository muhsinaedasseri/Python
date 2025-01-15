#!/usr/bin/env python
# coding: utf-8

# # Exercise 1:

# In[2]:


#Write a program that reads an integer value between 1 and 12 from the user and prints output the corresponding 
#month of the year.

# MonthNames.py
month_number = int(input("Enter the month: "))
months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]

if 1 <= month_number <= 12:
    print(f"Month {month_number} is {months[month_number - 1]}")
else:
    print("Invalid month number. Please enter a value between 1 and 12.")


# # exercise 2:

# In[5]:


# Cinema Ticket Price

full_price = 6.0
age = int(input("Enter your age: "))

if age < 16:
    ticket_price = full_price / 2
elif age >= 60:
    ticket_price = full_price / 3
else:
    ticket_price = full_price

print(f"Your ticket costs £{ticket_price:.2f}")


# # exercise 3:

# In[ ]:


# body mass index

weight = float(input("Enter your weight in (kg): "))
height = float(input("Enter your height in (m): "))

bmi = weight / (height ** 2)
print(f"Your BMI is: {bmi:.2f}")

if bmi < 18.5:
    category = "underweight"
elif 18.5 <= bmi < 24.9:
    category = "normal"
elif 25 <= bmi < 29.9:
    category = "overweight"
else:
    category = "obese"

print(f"You are in the \"{category}\" range.")


# # Exercise 4

# In[7]:


# Write a Python program to receive 3 numbers from the user and print the greatest among them.

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

greatest_num = max(num1, num2, num3)
print(f"The greatest number is: {greatest_num}")


# # exercise 5

# In[12]:


# Find the factorial of a given number using loops(note the number is received from the user)

# Factorial using loop

number = int(input("Enter a number:"))                     

# Initialize factorial to 1
factorial = 1

# Calculate factorial using a loop
for i in range(1, number + 1):
    factorial *= i

print(f"The factorial of {number} is {factorial}")


# # Exercise 6
# 

# In[13]:


# Reverse a number using while loop

number = int(input("Enter a number: "))
reversed_number = 0

while number != 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number //= 10

print(f"The reversed number is {reversed_number}")


# # Exercise 7

# In[14]:


# Finding the multiples of a number using loop

number = int(input("Enter a number: "))
limit = int(input("Enter the limit: "))

print(f"Multiples of {number} up to {limit}:")
for i in range(1, limit + 1):
    if i % number == 0:
        print(i)


# # Exercise 8
# 

# In[15]:


while True:
    value = input("Enter a value: ")
    if value == 'done':
        print("Done")
        break
    print(value)


# # Exercise 9

# In[19]:


#FizzBuzz

for i in range(1, 11):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)


# # Exercise 10

# In[17]:


# pattern printing

for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()


# In[ ]:




