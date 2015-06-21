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
        else:
            pass
    newphrase = [d.get(w) if w in d else w for w in sys.argv[2].lower().split()]
    print(" ".join(w.capitalize() for w in newphrase))
if __name__ == "__main__":
    main(sys.argv)