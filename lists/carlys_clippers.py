#!/usr/bin/python3
# Carly's Clippers - Hair salon business analysis
# Demonstrates: lists, loops, list comprehensions, calculations

# Data
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]  # Number of customers per style

# Calculate average price
total_price = sum(prices)
average_price = total_price / len(prices)
print(f'Average Haircut Price: ${average_price}')

# Apply $5 discount to all prices
new_prices = [price - 5 for price in prices]
print(f'\nNew prices after $5 discount:')
print(new_prices)

# Calculate total revenue
total_revenue = 0
for i in range(len(hairstyles)):
    total_revenue += prices[i] * last_week[i]
print(f'\nTotal Revenue: ${total_revenue}')

# Calculate average daily revenue
average_daily_revenue = total_revenue / 7
print(f'Average Daily Revenue: ${average_daily_revenue:.2f}')

# Find cuts under $30 (after discount)
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]
print(f'\nHaircuts under $30:')
print(cuts_under_30)
