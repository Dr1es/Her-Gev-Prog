#!/usr/bin/python

import sys
from collections import defaultdict

def main(argv):
    f = open(sys.argv[1])
    d = defaultdict()
    for line in f:
        x = line.split()
        if x[0] == "[NN]" or x[0] == "[NNP]":
            d.setdefault(x[2], x[4])
    #print(d)
    print(len(d))
    phrase = sys.argv[2]
    phrase1 = phrase.split()
    for x in phrase1:
        for key, value in d.iteritems():
            if x == key:
                print(value)
    #print(paraphrase)

if __name__ == "__main__":
    main(sys.argv)