#2. Prompt the user for their name and their age. Calculate their age next year.
Use string concatenation to print "Hello, <name>! You are <age1> years old. Next year, you will be <age2> years old."

# Prompt the user for their name
name = input("Enter your name: ")

# Prompt the user for their age
age = int(input("Enter your age: "))

# Calculate the age next year
age_next_year = age + 1

# Display the message using string concatenation
print("Hello, " + name + "! You are " + str(age) + " years old. Next year, you will be " + str(age_next_year) + " years old.")
