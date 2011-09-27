#!/usr/bin/env python

import sys

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


def words0(P):
    """
    Sometimes, you can try too hard to be clever when obvious
    and straightforward will solve the problem as specified...
    """
    for ch0 in L[P[0]]:
        for ch1 in L[P[1]]:
            for ch2 in L[P[2]]:
                # Keep nesting if you realy want reults for all 7 letter...
                yield ''.join((ch0, ch1, ch2)) # ,ch3, ch4, ch5, ch6

def words1(P):
    """
    Kind of like the nested loops in words0, except it generates a big list of
    all of the values before returning; Syntatically concise. If actually extended
    for all 7 digits of a phone number, it would be awkward to read...
    """

    # For actual phone numbers, just extend this expression until you get to 'for ch6 in L[P[6]]';
    return [''.join((ch0,ch1,ch2)) for ch0 in L[P[0]] for ch1 in L[P[1]] for ch2 in L[P[2]]]

def words2(P):
    """
    Yields one word at a time by stripping the leading digit, then taking its characters
    and joining them to the front of all the possible words from the remaining digits (P[1:]).
    """
    if P == '':
        yield ''
    else: # Ha! Protect this in an 'else' clause, or we'll be back here even after we've yielded the empty string!
       for word in (word+ch for word in words2(P[:-1]) for ch in L[P[-1]]):
            yield word

def gen_words(P):
    """
    Create a set of nested generators to compute the phone words.

    'ch' iterates through the possible values for the first letter based on the digit P[0].
    Attach that letter to the start of each possible word we can create from the remaining digits.
    """
    return (word+ch for word in gen_words(P[:-1]) for ch in L[P[-1]]) if P else ['']

def itertools_words(P):
    """
    Dump the real work onto the std library itertools module;
    """
    from itertools import product, starmap

    letter_list = [L[i] for i in P]                             # '232' => ['abc', 'def', 'abc']
    letter_combinations = product(*letter_list)                 # yields ('a','d','a'), ('a','d','b'), ...
    words = starmap(lambda *x: ''.join(x), letter_combinations) # join the letters of the tuples;
    return words

def itertools_terse(P):
    """
    Same as itertools_words() but as a one-liner...
    """
    from itertools import product, starmap

    return starmap(lambda *x: ''.join(x), product(*[L[i] for i in P]))


def usage():

    print >> sys.stderr, "Usage: %s <phone-number>" % sys.argv[0]
    sys.exit(1)


if __name__ == "__main__":

    if len(sys.argv) < 2:
        usage()

    # wordgen = words0(sys.argv[1])
    # wordgen = words1(sys.argv[1])
    # wordgen = words2(sys.argv[1])
    wordgen = gen_words(sys.argv[1])
    # wordgen = itertools_words(sys.argv[1])
    wordgen = itertools_terse(sys.argv[1])

    for word in wordgen:
        print word
