#!/usr/bin/python3
# Leap Year Checker
# Demonstrates: conditionals, modulo operator, algorithm implementation

def is_leap(year):
    """
    Determine if a year is a leap year.
    
    Rules:
    1. Divisible by 400 -> leap year
    2. Divisible by 100 -> NOT leap year
    3. Divisible by 4 -> leap year
    4. Otherwise -> NOT leap year
    """
    leap = False
    
    if year % 400 == 0:
        leap = True
    elif year % 100 == 0:
        leap = False
    elif year % 4 == 0:
        leap = True
    
    return leap


# Test cases
if __name__ == '__main__':
    test_years = [2024, 1900, 2000, 2001, 2004, 1800, 2400]
    
    print('Leap Year Checker')
    print('-' * 30)
    for year in test_years:
        result = "Leap Year" if is_leap(year) else "Not Leap Year"
        print(f'{year}: {result}')
