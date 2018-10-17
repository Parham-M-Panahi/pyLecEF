#!/usr/bin/python3 -tt
# exercises for strings and lists in python

# Fill in the code for the functions below.
# Don't worry about test() and main(), they're just set up
# to call the functions with a few different input to test the code
# printing 'OK' when your functions work as intended,
# and printing 'X' when they don't.
# the starting code for each function includes a 'return'
# which is a placeholder for your code.

# A. both_ends
# Given a string s, return a string made of the first 2
# and the last 2 chars of the original string,
# so 'string' yields 'stng',
# and 'winner' yields 'wier'. However, if the string length
# is less than 2, return instead the empty string.
def both_ends(s):
    # TODO: code goes here
    return

# B. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'
# Return the resulting string
# So 'This book is not that bad!' yields
# 'This book is good!'
def not_bad(s):
    # TODO: code goes here
    return

# C. remove_adjacent
# Given a list of numbers, return a list where
# all adjacent equal elements have been reduced to a single element,
# so [1, 2, 2, 3] returns [1, 2, 3]. you may create a new list or 
# modify the passed in list.
def remove_adjacent(nums):
    # TODO: code goes here
    return


# The test function simply tests your code,
# You don't need to change it or anything,
# You can read it if you like.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = ' X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


def main():
    print('A. both_ends')
    test(both_ends('spring'), 'spng')
    test(both_ends('Hello'), 'Helo')
    test(both_ends('a'), '')
    test(both_ends('xyz'), 'xyyz')
    print()

    print('B. not_bad')
    test(not_bad('This movie is not so bad'), 'This movie is good')
    test(not_bad('This dinner is not that bad'), 'This dinner is good')
    test(not_bad('This tea is not hot'), 'This tea is not hot')
    test(not_bad("It's bad yet not"), "It's bad yet not")
    print()

    print('C. remove_adjacent')
    test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
    test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
    test(remove_adjacent([]), [])
    print()


if __name__ == '__main__':
    main()

