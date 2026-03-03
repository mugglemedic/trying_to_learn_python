#!/bin/python

# import argparse

__version__ = '0.1'

# Welcome and collect required data
print(f'Thank you for using mortgage calculator version {__version__}!')

principal = input('What is your prinicipal (loan) amount? ')

apr = input('''
What is your annual intrest rate? Enter a number value only.
(ex: 5.2% should be entered as \"5.2\" )'''
            )

down_payment = input(
    'If you placed a down payment, enter it now. If not enter 0. ')

loan_term = input('How many years is your term? ')

# Stuff for later: start date, taxes, insurance and fees.


