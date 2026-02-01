#!/usr/bin/python3
# Magic 8 Ball - Interactive fortune teller program
# Demonstrates: random module, input validation, loops, conditionals

import random
import time
import sys

def magic_eight_ball():
    """Run a single magic 8 ball prediction"""
    # Get user information
    name = input('What is your name? ')
    if name == "":
        question_str = 'What is your question? '
    else:
        question_str = f'What is your question, {name.title()}? '
    
    question = input(question_str)
    
    # Validate input
    time.sleep(0.5)
    if question == "":
        print('If you do not ask a question, you will never get an answer. Try again.')
        sys.exit()
    
    # Display question
    if name == "":
        print(f'\nSo, you ask the question: {question}.')
    else:
        print(f'So, {name.title()} asks the question: {question}.')
    
    # Generate random answer
    answer = random.randint(1, 9)
    answers = {
        1: 'Yes - definitely',
        2: 'It is decidedly so',
        3: 'Without a doubt',
        4: 'Reply hazy, try again',
        5: 'Ask again later',
        6: 'Better not tell you now',
        7: 'My sources say no',
        8: 'Outlook not so good',
        9: 'Very doubtful'
    }
    
    print('Hmmm...')
    time.sleep(3)  # Dramatic pause
    print(answers[answer])

# Main program loop
while True:
    magic_eight_ball()
    redo = input('\nWould you like to go again? (y/n) ')
    if redo.lower() != 'y':
        print('Thanks for playing!')
        break
