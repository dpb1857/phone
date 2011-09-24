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

# Generate the words we can make from a phone number using list comprehensions;
def words1(P):

    # For actual phone numbers, just extend this expression through 'for letter6 in L[P[6]]';
    # Truncated here so we can visually check the result;
    #
    # This is straightword, but has the disadvantage that we're generating the entire list 
    # in memory before we return it;

    return [''.join((letter0,letter1,letter2)) for letter0 in L[P[0]] for letter1 in L[P[1]] for letter2 in L[P[2]]]

def words2(P):
    """
    Yields one word at a time by stripping the leading digit, then taking its characters
    and joining them to the front of all the possible words from the remaining digits (P[1:]).
    """
    if P == '':
        yield ''
    else: # Ha! Protect this in an 'else' clause, or we'll be back here even after we've yielded the empty string!
        for word in (ch+words for ch in L[P[0]] for words in words2(P[1:])):
            yield word

def gen_words(P):
    """
    Create a set of nested generators to compute the phone words;
    """
    return (ch+words for ch in L[P[0]] for words in gen_words(P[1:])) if P else ['']


def usage():

    print >> sys.stderr, "Usage: %s <phone-number>" % sys.argv[0]
    print >> sys.stderr, "  phone-number must be a 7-digit string"
    sys.exit(1)


if __name__ == "__main__":

    if len(sys.argv) < 2:
        usage()

    if False:
        wordfunc = words1(sys.argv[1])

    if True:
        wordfunc = gen_words(sys.argv[1])

    for word in wordfunc:
        print word
