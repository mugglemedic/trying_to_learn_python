#!/usr/bin/python3
# Sal's Shipping - Calculate cheapest shipping method
# Demonstrates: functions, conditionals, comparisons, user input

def calculate_ground_shipping(weight):
    """Calculate ground shipping cost based on weight"""
    flat_charge = 20.00
    
    if weight <= 2:
        rate = 1.50
    elif weight <= 6:
        rate = 3.00
    elif weight <= 10:
        rate = 4.00
    else:
        rate = 4.75
    
    return weight * rate + flat_charge

def calculate_premium_ground():
    """Premium ground shipping has a flat rate"""
    return 125.00

def calculate_drone_shipping(weight):
    """Calculate drone shipping cost based on weight"""
    if weight <= 2:
        rate = 4.50
    elif weight <= 6:
        rate = 9.00
    elif weight <= 10:
        rate = 12.00
    else:
        rate = 14.25
    
    return weight * rate

def find_cheapest_shipping(weight):
    """Compare all shipping methods and return the cheapest"""
    ground = calculate_ground_shipping(weight)
    premium = calculate_premium_ground()
    drone = calculate_drone_shipping(weight)
    
    print(f'\nShipping costs for {weight} lbs:')
    print(f'Ground Shipping: ${ground:.2f}')
    print(f'Premium Ground: ${premium:.2f}')
    print(f'Drone Shipping: ${drone:.2f}')
    
    cheapest = min(ground, premium, drone)
    
    if cheapest == ground:
        method = "Ground Shipping"
    elif cheapest == premium:
        method = "Premium Ground"
    else:
        method = "Drone Shipping"
    
    print(f'\nCheapest option: {method} at ${cheapest:.2f}')

# Test with different weights
if __name__ == '__main__':
    find_cheapest_shipping(4.8)
    find_cheapest_shipping(41.5)
