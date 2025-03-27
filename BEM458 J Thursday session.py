#######################################################################################################################################################
# 
# Name: James Crummack
# SID: 710026464
# Exam Date: 27/03/2025
# Module: BEMM458 - Programming for Business Analytics
# Github link for this assignment:  https://github.com/UniversityExeterBusinessSchool/practiceassessment-thursday-james-crummack/edit/main/BEM458%20J%20Thursday%20session.py
#
# ######################################################################################################################################################
# Instruction 1. Read the questions and instructions carefully and complete scripts.

# Instruction 2. Only ethical and minimal use of AI is allowed. You might use AI to give advice on how to use a tool or programming language.  
#                You must not use AI to create the code. You might make use of AI to aid debugging of the code.  
#                You must indicate clearly how and where you have used AI.

# Instruction 3. Copy the output of the code and insert it as a comment below your code e.g # OUTPUT (23,45)

# Instruction 4. Ensure you provide comments for the code and the output to show contextual understanding.

# Instruction 5. Upon completing this test, commit to Git, copy and paste your code into the word file and upload the saved file to ELE.
#                There is a leeway on when you need to upload to ELE, however, you must commit to Git at 
#                the end of your session.

# ######################################################################################################################################################
# Question 1 - Loops
# Create a list and use a for loop to answer the following question:
# You are given a dictionary called key_comments. Your allocated keys are the first and last digit of your SID.
# Find the start and end position of each of the items in the sentence using the find command.
# Create and populate a list called my_list with a tuple of (start location, end location) for each value in comments 
 

customer_feedback = """Your recent order experience has been satisfactory overall. While there were some minor issues,
we appreciate the effort made to resolve them promptly."
"""

# List of words to search for
key_comments = {
    0: 'satisfactory',
    1: 'order',
    2: 'effort',
    3: 'issues',
    4: 'promptly',
    5: 'appreciate',
    6: 'experience',
    7: 'resolve',
    8: 'overall',
    9: 'minor'
}

# Write your search code here and provide comments. 
# Intitialise empty list
my_list = []

# For loop to iterate through the dictionary
for key, comment in key_comments.items():
    
    start = customer_feedback.find(comment) # Find start and end position
    end = start + len(comment) # Calculate end position
    
    my_list.append((start, end)) # Add the tuple of the positions to the list
    
print(my_list) # Print the list of tuples

##########################################################################################################################################################

# Question 2 - Functions
# Scenario - You are working in an e-commerce firm as a business analyst, and your manager has tasked you to generate weekly reports on financial metrics like 
# Operating Profit Margin, Revenue per Customer, Customer Churn Rate, and Average Order Value. Use Python functions 
# that will take the values and return the metric needed. Use the first two and last two digits of your ID number as the input values.

# Insert first two digits of ID number here: 71
# Insert last two digits of ID number here: 64

# Write your code for Operating Profit Margin
def operating_profit_margin(revenue, total_expenses):
    profit = (revenue - total_expenses)
    profit_margin = (profit / revenue) * 100
    return profit_margin

# Write your code for Revenue per Customer
def revenue_per_customer(revenue, customer):
    return (revenue / customer)

# Write your code for Customer Churn Rate
def custoner_churn_rate(total_customers, lost_customers):
    return lost_customers / total_customers

# Write your code for Average Order Value
def average_order_value(revenue, num_orders):
    return (revenue / num_orders)

# Call your designed functions here

print(operating_profit_margin(71, 64))
print(revenue_per_customer(71, 64))
print(custoner_churn_rate(71, 64))
print(average_order_value(71, 64))

# AI used to look up formulae for different terms.

##########################################################################################################################################################

# Question 3 - Regression
# A retail store has collected data on seasonal sales and price changes. The table below shows different price levels and their corresponding demand.
# Develop a linear regression model and determine:
# 1. The price at which the store can maximize revenue
# 2. The demand when the price is set at £52

"""
Price (£)    Demand (Units)
---------------------------
20           300
25           280
30           260
35           240
40           210
45           190
50           160
55           140
60           120
65           100
70           85
"""

# Write your code here
import sklearn
from sklearn.linear_model import LinearRegression

model = LinearRegression() # Initialise the model
price = [[20], [25], [30], [35], [40], [45], [50], [55], [60], [65], [70]] # Define price , as 2d array for sklearn linear regression.
demand = [300, 280, 260, 240, 210, 190, 160, 140, 120, 100, 85] # Define demand, as a 1d array.

model.fit(price, demand) # Fit the model

# 1 - Price that maximises revenue
# Optimal price = -b0 / (2 * b1), b0 is the y intercept and b1 is the coefficient.

 # Extract Coefficients from the model
b0 = model.intercept_
b1 = model.coef_[0]

# Calculate the optimal price to maximise revenue
if b1 < 0:  # Check that demand decreases with price
    optimal_price = -b0 / (2 * b1) # Calculate where the derivative of the revenue function is 0 (maximum)
    print(f"The price that maximizes revenue is: {optimal_price:.2f}")
else:
    print("The model does not indicate a decreasing demand with price.")


# 2 - Demand when the prive is at £52
predicted_demand = model.predict([[52]]) # Predict the demand at price 52
print(f"{predicted_demand[0]} is the demand when the price is set at £52") # Print statement for predicted demand at £52

# Used AI to look up documentation for sklearn as I was having import issues.


##########################################################################################################################################################

# Question 4 - Debugging; Plotting and data visualization chart

import random
import matplotlib.pyplot as plt

# Generate 100 random numbers between 1 and student id number
max_value = int(input("Enter your Student ID: "))
random_numbers = [random.randint(1, max_value) for i in range(0,100)]

# Plotting the numbers in a line chart
plt.plot(random_numbers, marker='o', markerfacecolor='green', markeredgecolor='red', linestyle='dashed', label='Random Numbers', color='blue')
plt.title("Line Chart of 100 Random Numbers")
plt.xlabel=("Index")
plt.ylabel=("Random Number")
plt.legend()
plt.grid(True)
plt.show()

