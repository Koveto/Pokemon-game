# 4.2 temperature.py

# This program assists a technician in the process
# of checking a substance's temperature.

# Named constant to represent the maximum temperature.
MAX_TEMP = 102.5

# Get the substance's temperature.
temperature = float(input("Enter the substance's Celsius temperature: "))

# As long as necessary, instruct the user to
# adjust the thermostat.
while temperature > MAX_TEMP:
    print('The temperature is too high.')
    print('Turn the thermostat down and wait')
    print('5 minutes. Then take the temperature')
    print('again and enter it.')
    temperature = float(input('Enter the new Celsius temperature: '))

# Remind the user to check the temperature again
# in 15 minutes.
print('The temperature is acceptable.')
print('Check it again in 15 minutes.')

# 4.9 speed_converter.py

# This program converts the speeds 60 kph
# through 130 kph (in 10 kph increments)
# to mph.
START_SPEED = 60    # Starting speed
END_SPEED = 131     # Ending speed
INCREMENT = 10      # Speed increment
CONVERSION_FACTOR = 0.6214 # Conversion factor

# Print the table headings
print('KPH\tMPH')
print('--------------')

# Print the speeds.
for kph in range(START_SPEED, END_SPEED, INCREMENT):
    mph = kph * CONVERSION_FACTOR
    print(f'{kph}\t{mph:.1f}')

# 4.13 property_tax.py

# This program displays property taxes.

TAX_FACTOR = 0.0065         # Represents the tax factor.

# Get the first lot number
print('Enter the property lot number or enter 0 to end.')
lot = int(input('Lot number: '))

# Continue processing as long as the user
# does not enter lot number 0.
while lot != 0:
    # Get the property value.
    value = float(input('Enter the property value: '))

    # Calculate the property's tax
    tax = value * TAX_FACTOR

    # Display the tax.
    print(f'Property tax: ${tax:,.2f}')

    # Get the next lot number.
    print('Enter the next lot number or enter 0 to end.')
    lot = int(input('Lot number: '))

# 4.15 retail_no_validation.py

# This program calculates retail prices.
MARK_UP = 2.5   # The markup percentage
another = 'y'   # Variable to control the loop

# Process one or more items.
while another == 'y' or another == 'Y':
    # Get the item's wholesale cost.
    wholesale = float(input("Enter the item's wholesale cost: "))

    # Calculate the retail price.
    retail = wholesale * MARK_UP

    # Display the retail price.
    print(f'Retail price: ${retail:,.2f}')

    # Do this again?
    another = input('Do you have another item? ' +
                    '(Enter y for yes): ')
    
# 4.17 test_score_averages.py

# This program averages test scores. It asks the user for the
# number of students and the number of test scores per student.

# Get the number of students.
num_students = int(input('How many students do you have? '))

# Get the number of test scores per student.
num_test_scores = int(input('How many test scores per student? '))

# Determine each student's average test score.
for student in range(num_students):
    # Initialize an accumulator for the test scores.
    total = 0.0

    # Display the student number.
    print(f'Student number {student + 1}')
    print('-----------------')

    # Get the student's test scores.
    for test_num in range(num_test_scores):
        print(f'Test number {test_num + 1}', end='')
        score = float(input(': '))

        # Add the score to the accumulator.
        total += score
    
    # Calculate the average test score for this student.
    average = total / num_test_scores

    # Display the average.
    print(f'The average for student number {student + 1} '
          f'is: {average:.1f}')
    print()
