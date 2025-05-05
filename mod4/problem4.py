#4. A theater wants to enforce age restrictions for movie tickets. 
# Ask the user for their age, and tell them whether they can see G 
# (appropriate for under 13),\PG-13 (appropriate for 13 to 17), 
# or R (appropriate for over 18) rated movies.

# get the users age 
age = int(input("Pleas give me your age: "))
# depneding on age print what type of movies they can see
if age < 13:
    print("you can watch G-reated moives.")
elif 13 <= age <= 17:
    print("you can watch G and PG-13 rated movies.")
else:
    print("youi can watch G, PG-13, and R-rated movies.")
