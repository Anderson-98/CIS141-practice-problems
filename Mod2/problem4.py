"""# 4. Create a program that prompts the user for their
birth year and displays a message that says "You are ___ old". 
Use an f-string in your solution to this problem.
"""
 # Prompt the user for their birth year
birth_year = int(input("Enter your birth year: "))

# Compute the user's age
current_year = 2025  # Assuming the current year is 2025
age = current_year - birth_year

# Display the message using an f-string
print(f"You are {age} years old.")
