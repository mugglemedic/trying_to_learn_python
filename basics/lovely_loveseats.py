#!/usr/bin/python3
# Lovely Loveseats - Furniture store receipt generator
# Demonstrates: variables, string formatting, math operations, f-strings

# Item descriptions
lovely_loveseat_description = 'Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.'
stylish_settee_description = 'Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.'
luxurious_lamp_description = 'Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.'

# Pricing
lovely_loveseat_price = 254.00
stylish_settee_price = 180.50
luxurious_lamp_price = 52.15
sales_tax = 1.088  # Multiplier for 8.8% tax

# Customer purchases
customer_one_total = 0
customer_one_items = ''

# Add purchases
customer_one_total += lovely_loveseat_price + luxurious_lamp_price
customer_one_items += '\n' + lovely_loveseat_description + '\n' + luxurious_lamp_description

# Calculate total with tax
total_one = customer_one_total * sales_tax

# Print receipt
print('Customer One Items')
print("*" * 15)
print(customer_one_items)
print('\nCustomer One Total')
print("*" * 15)
print(f'${round(total_one, 2)}')
