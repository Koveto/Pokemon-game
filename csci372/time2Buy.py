# CSCI 372
# Assignment 1, Question 3
# Write a program to calculate how many months it will take you
# to save up enough money for a down payment.

# Ask user for cost, salary, and savings
total_cost = float(input("Please enter the cost of your dream house: "))
annual_salary = float(input("What is your annual salary? $"))
portion_saved = float(input("What percentage of your salary are you saving? ")) / 100

portion_down_payment = 0.25
current_savings = 0.0
r = 0.04 # interest return
months = 0

while current_savings < (total_cost * portion_down_payment):
    months += 1
    current_savings += (annual_salary / 12) * portion_saved
    current_savings += current_savings*r/12

print("It will take you " + str(months) + " months to save enough money for the down payment.")