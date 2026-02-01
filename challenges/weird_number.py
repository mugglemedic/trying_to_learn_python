#!/usr/bin/python3
# Weird Number Classifier
# Demonstrates: conditionals, range checking, logical operators

def is_weird(n):
    """
    Classify a number as 'Weird' or 'Not Weird' based on rules:
    - If odd: Weird
    - If even and 2-5: Not Weird
    - If even and 6-20: Weird
    - If even and >20: Not Weird
    """
    if n % 2 == 1:  # Odd
        return True
    elif n % 2 == 0 and 2 <= n <= 5:  # Even, 2-5
        return False
    elif n % 2 == 0 and 6 <= n <= 20:  # Even, 6-20
        return True
    elif n % 2 == 0 and n > 20:  # Even, >20
        return False


if __name__ == '__main__':
    # For HackerRank-style input
    try:
        n = int(input('Enter a number: ').strip())
        
        if is_weird(n):
            print('Weird')
        else:
            print('Not Weird')
    except ValueError:
        print('Please enter a valid integer')
