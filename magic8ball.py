#!/usr/bin/python3
import sys
import time
import random


def magic_eight_ball():

    # import needed module
    # set variables
    answer = random.randint(1, 9)

    name = input('What is your name? ')
    if name == "":
        question_str = 'What is your question? '
    else:
        question_str = f'What is your question, {name.title()}? '
    question = input(question_str)
    # set variables for answers
    # then when you're done, realize you could have just
    # made a list and set a random variable to call to it.
    # sigh.
    one = 'Yes - definitely'
    two = 'It is decidedly so'
    three = 'Without a doubt'
    four = 'Reply hazy, try again'
    five = 'Ask again later'
    six = 'Better not tell you now'
    seven = 'My sources say no'
    eight = 'Outlook not so good'
    nine = 'Very doubtful'
    # brief delay, otherwise it's a little jarring
    time.sleep(0.5)
    # if user doesnt enter name, print without attempt to
    # repeat the name.
    if question == "":
        print('If you do not ask a question, you will never get an answer. Try again.')
        sys.exit()
    elif name == "":
        print(f'\nSo, you ask the question: {question}.')
    else:
        print(f'\nSo, {name.title()}  asks the question: {question}.')

    print('Hmmm...\n')
    # dramatic... pause!
    time.sleep(3)

    match answer:
        case 1:
            print(one)
        case 2:
            print(two)
        case 3:
            print(three)
        case 4:
            print(four)
        case 5:
            print(five)
        case 6:
            print(six)
        case 7:
            print(seven)
        case 8:
            print(eight)
        case 9:
            print(nine)

# This was mostly AI 
while True:
    magic_eight_ball() 
    redo = input('\nWould you like to go again? (y/n) ')
    if redo.lower() != 'y': # didn't even occur to me to make this lower case.
        print('Thanks! Have a mystical day!')
        break
