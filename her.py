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
    frase = sys.argv[2]
    frase1 = frase.split()
    for word in frase1:
        if word in d:
            word = d.values()
    print(frase1)

main(sys)