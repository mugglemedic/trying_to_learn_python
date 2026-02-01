#!/usr/bin/python3
# Google Python Class - String Exercises
# Demonstrates: string methods, slicing, conditionals, return statements

# A. donuts
# Return string of form 'Number of donuts: <count>'
# If count is 10 or more, use 'many' instead of count
def donuts(count):
    if count < 10:
        return f'Number of donuts: {count}'
    else:
        return 'Number of donuts: many'


# B. both_ends
# Return first 2 and last 2 chars of string
# Return empty string if length < 2
def both_ends(s):
    if len(s) < 2:
        return ''
    return s[0:2] + s[-2:]


# C. fix_start
# Replace all occurrences of first char (except first) with '*'
def fix_start(s):
    return s[0] + s[1:].replace(s[0], "*")


# D. mix_up
# Swap first 2 chars of each string and combine with space
def mix_up(a, b):
    return b[:2] + a[2:] + ' ' + a[:2] + b[2:]


# Test function
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# Main test suite
def main():
    print('donuts')
    test(donuts(4), 'Number of donuts: 4')
    test(donuts(9), 'Number of donuts: 9')
    test(donuts(10), 'Number of donuts: many')
    test(donuts(99), 'Number of donuts: many')

    print()
    print('both_ends')
    test(both_ends('spring'), 'spng')
    test(both_ends('Hello'), 'Helo')
    test(both_ends('a'), '')
    test(both_ends('xyz'), 'xyyz')

    print()
    print('fix_start')
    test(fix_start('babble'), 'ba**le')
    test(fix_start('aardvark'), 'a*rdv*rk')
    test(fix_start('google'), 'goo*le')
    test(fix_start('donut'), 'donut')

    print()
    print('mix_up')
    test(mix_up('mix', 'pod'), 'pox mid')
    test(mix_up('dog', 'dinner'), 'dig donner')
    test(mix_up('gnash', 'sport'), 'spash gnort')
    test(mix_up('pezzy', 'firm'), 'fizzy perm')


if __name__ == '__main__':
    main()
