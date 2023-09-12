# CSCI 372
# Assignment 1, Question 1
# Write a program to convert Celsius to Fahrenheit values.

# Ask user for Celsius temperature.
tempCelsius = float(input("Please enter a temperature in Celsius: "))

# Convert temperature to Fahrenheit.
tempFahrenheit = (tempCelsius * 9/5) + 32

# Display resulting temperature.
print(str(tempCelsius) + " degrees Celsius is " +
      str(tempFahrenheit) + " degrees Fahrenheit.")
