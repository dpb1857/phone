#!/usr/bin/env python

"""
Script to demonstrate techniques for mapping phone numbers to words.
"""

# pylint: disable=invalid-name,line-too-long

import argparse

# Map phone key to the symbols it represents
L = {'0': '0',
     '1': '1',
     '2': 'abc',
     '3': 'def',
     '4': 'ghi',
     '5': 'jkl',
     '6': 'mno',
     '7': 'prs',
     '8': 'tuv',
     '9': 'wxy'
    }

def wordsNestedLoops(P):
    """
    Generate words via nested 'for' loops.

    Sometimes, you can try too hard to be clever when obvious
    and straightforward will solve the problem as specified...
    """
    if len(P) < 3:
        raise Exception("min ph# length is 3 for nested loop version")

    for ch0 in L[P[0]]:
        for ch1 in L[P[1]]:
            for ch2 in L[P[2]]:
                # Keep nesting if you realy want reults for all 7 letter...
                yield ''.join((ch0, ch1, ch2)) # ,ch3, ch4, ch5, ch6

def wordsListComp(P):
    """
    Generate words via list comprehensions.

    Kind of like the nested loops in words0, except it generates a big list of
    all of the values before returning; Syntatically concise. If actually extended
    for all 7 digits of a phone number, it would be awkward to read...
    """
    if len(P) < 3:
        raise Exception("min ph# length is 3 for nested loop version")

    # For actual phone numbers, just extend this expression until you get to 'for ch6 in L[P[6]]';
    return [''.join((ch0, ch1, ch2)) for ch0 in L[P[0]] for ch1 in L[P[1]] for ch2 in L[P[2]]]

def words_recursive(P):
    """
    A traditional recursive solution.
    """
    if not P:
        return ['']

    words = []
    # Do the recursion in the outer loop;
    for word in words_recursive(P[:-1]):
        for ch in L[P[-1]]:
            words.append(word+ch)

    return words

def words_gen1(P):
    """
    Yields one word at a time by stripping the leading digit, then taking its characters
    and joining them to the front of all the possible words from the remaining digits (P[1:]).
    """
    if P == '':
        yield ''
        return

    for word in (word+ch for word in words_gen1(P[:-1]) for ch in L[P[-1]]):
        yield word

def words_gen2(P):
    """
    Create a set of nested generators to compute the phone words; this time a one-liner.

    'ch' iterates through the possible values for the first letter based on the digit P[0].
    Attach that letter to the start of each possible word we can create from the remaining digits.
    """
    return (word+ch for word in words_gen2(P[:-1]) for ch in L[P[-1]]) if P else ['']

def words_itertools(P):
    """
    Dump the real work onto the std library itertools module;
    """
    from itertools import product, starmap

    letter_list = [L[i] for i in P]                             # '232' => ['abc', 'def', 'abc']
    # pylint: disable=star-args
    letter_combinations = product(*letter_list)                 # yields ('a','d','a'), ('a','d','b'), ...
    words = starmap(lambda *x: ''.join(x), letter_combinations) # join the letters of the tuples;
    return words

def words_itertools_terse(P):
    """
    Same as itertools_words() but as a one-liner...
    """
    from itertools import product, starmap

    return starmap(lambda *x: ''.join(x), product(*[L[i] for i in P]))

def main():
    "main function body"

    parser = argparse.ArgumentParser(description="Phone Number Word Generator")
    parser.add_argument("method", choices=["recursive", "nestedloops", "listcomp", "gen1", "gen2", "iter", "iterterse"])
    parser.add_argument("number", help="Phone number")
    args = parser.parse_args()

    if args.method == "recursive":
        wordgen = words_recursive(args.number)

    elif args.method == "nestedloops":
        wordgen = wordsNestedLoops(args.number)

    elif args.method == "listcomp":
        wordgen = wordsListComp(args.number)

    elif args.method == "gen1":
        wordgen = words_gen1(args.number)

    elif args.method == "gen2":
        wordgen = words_gen2(args.number)

    elif args.method == "iter":
        wordgen = words_itertools(args.number)

    elif args.method == "iterterse":
        wordgen = words_itertools_terse(args.number)

    for word in wordgen:
        print word


if __name__ == "__main__":
    main()
