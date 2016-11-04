#!/usr/bin/env python3

import sys
import re

def normwix(text):
    text = text.lower()
    text = re.sub(r"´", "'", text, flags=re.IGNORECASE)
    #text = re.sub(r"'", "", text, flags=re.IGNORECASE)
    text = re.sub(r"v", "w", text, flags=re.IGNORECASE)
    text = re.sub(r"c", "k", text, flags=re.IGNORECASE)
    text = re.sub(r"[0-9]+", "", text, flags=re.IGNORECASE)
    text = re.sub(r"ch", "ts", text, flags=re.IGNORECASE)
    text = re.sub(r"rr", "x", text, flags=re.IGNORECASE)
    text = re.sub(r" +", " ", text, flags=re.IGNORECASE)
    text = re.sub(r"^ ", "", text, flags=re.IGNORECASE)
    text = re.sub(r"[áàä]", "a", text, flags=re.IGNORECASE)
    text = re.sub(r"[éèë]", "e", text, flags=re.IGNORECASE)
    text = re.sub(r"[íìï]", "i", text, flags=re.IGNORECASE)
    text = re.sub(r"[óòö]", "o", text, flags=re.IGNORECASE)
    text = re.sub(r"[úùü]", "u", text, flags=re.IGNORECASE)

    #text = text.replace("á", "a")

    text = re.sub(r"([a-z])\1+", r"\1", text, flags=re.IGNORECASE)
    return text


def tokenizewix(text):
    text = re.sub(r"[^\s]([.|,|,\-,\"|:|;|¿|?|¡|!])", r" \1", text)
    text = re.sub(r"([.|,|,\-,\"|:|;|¿|?|¡|!])[^\s]", r"\1 ", text)
    return text

if __name__ == "__main__":

    l = 4
    op = sys.argv[1]
    if not "-" in op:
        l = 3
        op = ""
    else:
        if "p" in op:
            l = 3 
        else:
            outfile = sys.argv[3]
            Fo = open(outfile, "w")

    if len(sys.argv) != l:
        print("Formant:")
        print("     normwix.py [-a|-n|-t|-p] inputfile [outputfile]")
        sys.exit()

    infile = sys.argv[2]
    Fi = open(infile, "r")
    text = Fi.read()
    Fi.close()
    if ("n" in op) or ("a" in op):
        text = normwix(text)
    if ("t" in op) or ("a" in op):
        text = tokenizewix(text)
    if "p" in op:
        print(text)
    else:
        Fo.write(text)
        Fo.close()

