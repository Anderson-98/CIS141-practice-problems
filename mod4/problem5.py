#5. A store charges $5 for shipping on any order under $50. 
#If the order amount is $50 or more, shipping is free. 
#Ask the user for the order total and print the total cost, including shipping.

# Ask the user for the order total
order_total = float(input("Enter your order total: "))

# Determine shipping cost
shipping_cost = 5 if order_total < 50 else 0

# Calculate the final total
total_cost = order_total + shipping_cost

# Print the total cost, including shipping
print(f"Total cost including shipping: ${total_cost:.2f}")
