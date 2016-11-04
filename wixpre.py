#!/usr/bin/env python3

import sys
from normwix import normwix, tokenizewix
from seg import segment, segtext

sin = 0
Fo = 0 

if __name__ == "__main__":
    
    if len(sys.argv) < 2 or len(sys.argv) > 4:
        print("Formant:")
        print("     wixpre.py inputfile [-s] [outputfile]")
        sys.exit()

    if len(sys.argv) == 4:
        if sys.argv[2] == "-s":
            sin = 1
            print("Writing to ", sys.argv[3], "without morph anotations")
            outfile = sys.argv[3]
            Fo = open(outfile, "w")

    elif len(sys.argv) == 3:
        print("Writing to ", sys.argv[2])
        outfile = sys.argv[2]
        Fo = open(outfile, "w")

    infile = sys.argv[1]
    Fi = open(infile, "r")
    text = Fi.read()
    Fi.close()
    text = normwix(text)
    text = tokenizewix(text)
    text = segtext(text, s=sin)

    if Fo == 0:
        print(text)
    else:
        print("Writing to ", sys.argv[2])
        Fo.write(text)
        Fo.close()

