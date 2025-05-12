#1. Prompt the user for a positive integer n. 
# Use a while loop to sum all the integers from 1 up to n. Print the final sum.


n = int(input("Enter a positive integer: "))
while n < 1:
    n = int(input("please enter a positive integer: "))
sum_total = 0 
counter = 1
while counter <= n:
    sum_total += counter
    counter += 1
print("The sum of numbers from 1 to", n, "is:", sum_total)
