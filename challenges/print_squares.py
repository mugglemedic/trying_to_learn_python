#!/usr/bin/python3
# Print Squares
# Demonstrates: loops, range, exponentiation

def print_squares(n):
    """Print squares of all non-negative integers less than n"""
    if n < 0:
        print("Error: n must be non-negative")
        return
    
    for i in range(n):
        print(i**2)


if __name__ == '__main__':
    # For HackerRank-style input
    try:
        n = int(input('Enter n: '))
        print_squares(n)
    except ValueError:
        print('Please enter a valid integer')
