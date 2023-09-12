# 2-13 input.py

# Get the user's name, age, and income.
name = input('What is your name? ')
age  = int(input('What is your age? '))
income = float(input('What is your income? '))

# Display the data
print('Here is the data you entered:')
print('Name:',name)
print('Age:',age)
print('Income:',income)

# 2-15 sale_price.py

# This program gets an item's original price and
# calculates its sale price, with a 20% discount.

# Get the item's original price
original_price = float(input("Enter the item's original price: "))

# Calculate the amount of the discount
discount = original_price * 0.2

# Calculate the sale price
sale_price = original_price - discount

# Display the sale price
print('The sale price is',sale_price)

# 3-1 test_average.py

# This program gets three test scores and displays
# their average. It congratulates the user if the
# average is a high score.

# The HIGH_SCORE named constant holds the value that is
# considered a high score.
HIGH_SCORE = 95

# Get the three test scores.
test1 = int(input('Enter the score for test 1: '))
test2 = int(input('Enter the score for test 2: '))
test3 = int(input('Enter the score for test 3: '))

# Calculate the average test score.
average = (test1 + test2 + test3) / 3

# Print the average
print(f'The average score is [average].')

# If the average is a high score,
# congratulate the user.
if average >= HIGH_SCORE:
    print('Congratulations!')
    print('That is a great average!')

# 3-2 auto_repair_payroll.py

# Named constants to represent the base hours and
# the overtime multiplier.
BASE_HOURS = 40             # Base hours per week
OT_MULTIPLIER = 1.5         # Overtime multiplier

# Get the hours worked and the hourly pay rate.
hours = float(input('Enter the number of hours worked: '))
pay_rate = float(input('Enter the hourly pay rate: '))

# Calculate and display the gross pay.
if hours > BASE_HOURS:
    # Calculate the gross pay with overtime.
    # First, get the number of overtime hours worked.
    overtime_hours = hours - BASE_HOURS

    # Calculate the amount of overtime pay.
    overtime_pay =  overtime_hours * pay_rate * OT_MULTIPLIER

    # Calculate the gross pay.
    gross_pay = BASE_HOURS * pay_rate + overtime_pay
else:
    # Calculate the gross pay without overtime.
    gross_pay = hours * pay_rate

# Display the gross pay.
print(f'The gross pay is ${gross_pay:,.2f}.')

# 3-4 sort_names.py

# This program compares strings with the < operator.

# Get two names from the user.
name1 = input('Enter a name (last name first): ')
name2 = input('Enter another name (last name first): ')

# Display the names in alphabetical order.
print('Here are the names, listed alphabetically.')

if name1 < name2:
    print(name1)
    print(name2)
else:
    print(name2)
    print(name1)

# 3-5 loan_qualifier.py

# This program determines whether a bank customer
# qualifies for a loan.

MIN_SALARY = 30000.0    # the minimum annual salary
MIN_YEARS = 2           # the minimum years on the job

# Get the customer's annual salary.
salary = float(input('Enter your annual salary: '))

# Get the number of years on the current job.
years_on_job = int(input('Enter the number of years employed: '))

# Determine whether the customer qualifies.
if salary >= MIN_SALARY:
    if years_on_job >= MIN_YEARS:
        print('You qualify for the loan.')
    else:
        print(f'You must have been employed '
              f'for at least {MIN_YEARS} '
              f'years to qualify.')
else:
    print(f'You must earn at least $'
          f'{MIN_SALARY:,.2f} '
          f'per year to qualify.')

# 3-6 grader.py

# This program gets a numeric test score from the
# user and displays the corresponding letter grade.

# Named constants to represent the grade thresholds
A_SCORE = 90
B_SCORE = 80
C_SCORE = 70
D_SCORE = 60

# Get a test score from the user.
score = int(input('Enter your test score: '))

# Determine the grade
if score >= A_SCORE:
    print('Your grade is A.')
else:
    if score >= B_SCORE:
        print('Your grade is B.')
    else:
        if score >= C_SCORE:
            print('Your grade is C.')
        else:
            if score >= D_SCORE:
                print('Your grade is D.')
            else:
                print('Your grade is F.')

