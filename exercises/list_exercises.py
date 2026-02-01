#!/usr/bin/python3
# Google Python Class - List Exercises
# Demonstrates: lists, loops, conditionals, string matching, sorting

# A. match_ends
# Count strings where length >= 2 and first and last chars match
def match_ends(words):
    count = 0
    for word in words:
        if len(word) >= 2 and word[0] == word[-1]:
            count += 1
    return count


# B. front_x
# Sort strings, but group all strings starting with 'x' first
def front_x(words):
    x_wordlist = []
    wordlist = words.copy()
    
    for word in words:
        if word[0] == 'x':
            x_wordlist.append(word)
            wordlist.remove(word)
    
    x_wordlist.sort()
    wordlist.sort()
    return x_wordlist + wordlist


# C. sort_last
# Sort list of tuples by last element in each tuple
def sort_last(tuples):
    def get_last_element(t):
        return t[-1]
    
    return sorted(tuples, key=get_last_element)


# D. remove_adjacent
# Remove adjacent duplicate elements from list
def remove_adjacent(nums):
    result = []
    for num in nums:
        if len(result) == 0 or result[-1] != num:
            result.append(num)
    return result


# E. linear_merge
# Merge two sorted lists into one sorted list
def linear_merge(list1, list2):
    merge = list1 + list2
    merge.sort()
    return merge


# Test function
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# Main test suite
def main():
    print('match_ends')
    test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
    test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
    test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

    print()
    print('front_x')
    test(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
         ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
    test(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
         ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
    test(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
         ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])

    print()
    print('sort_last')
    test(sort_last([(1, 3), (3, 2), (2, 1)]),
         [(2, 1), (3, 2), (1, 3)])
    test(sort_last([(2, 3), (1, 2), (3, 1)]),
         [(3, 1), (1, 2), (2, 3)])
    test(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]),
         [(2, 2), (1, 3), (3, 4, 5), (1, 7)])

    print()
    print('remove_adjacent')
    test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
    test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
    test(remove_adjacent([]), [])

    print()
    print('linear_merge')
    test(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),
         ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
         ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
         ['aa', 'aa', 'aa', 'bb', 'bb'])


if __name__ == '__main__':
    main()
