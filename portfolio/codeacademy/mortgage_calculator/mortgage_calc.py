#!/bin/python

# import argparse

__version__ = '0.1'

# Welcome and collect required data
print(f'Thank you for using mortgage calculator version {__version__}!')
print('DISCLAIMER: This software can only calculate fixed-term loans.')
# print('')

principal = float(input('What is your prinicipal (loan) amount? $'))

apr = float(input('''
What is your annual intrest rate? Enter a number value only.
(ex: 5.2% should be entered as \"5.2\") %: '''
                  ))

down_payment = float(input(
    'If you placed a down payment, enter it now. If not enter 0. $'))

loan_term = float(input('How many years is your term? '))

# Stuff for later: start date, taxes, insurance and fees.

# define functions for what info the user requests


def calc_monthly_payment():
    # M = P * [r(1+r)^n] / [(1+r)^n - 1]
    # P = principal loan amount
    # r = monthly interest rate (annual rate / 12)
    # n = total number of payments (years × 12)
    P = float(principal - down_payment)
    r = float((apr/100) / 12)
    n = loan_term * 12
    return P * (r * (1 + r) ** n) / ((1+r)**n - 1)


print(f'Your monthly paymeny is ${calc_monthly_payment():.2f}')


def total_loan_ammount():
    pass


def interest_ammount():
    pass

# eventually make a table to show how an increased payment
# could decrease the number of years
# add warning to this bc of early settlement charges.
