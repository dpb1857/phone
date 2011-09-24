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
def words(P):

    # For actual phone numbers, just extend this expression through 'for l6 in L[P[6]]';
    # Truncated here so we can visually check the result;
    return [''.join((l0,l1,l2)) for l0 in L[P[0]] for l1 in L[P[1]] for l2 in L[P[2]]]

def usage():

    print >> sys.stderr, "Usage: %s <phone-number>" % sys.argv[0]
    print >> sys.stderr, "  phone-number must be a 7-digit string"
    sys.exit(1)


if __name__ == "__main__":

    if len(sys.argv) < 2:
        usage()

    print words(sys.argv[1])
    
