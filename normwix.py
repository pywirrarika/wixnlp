#!/usr/bin/env python3

# Copyright (C) 2016.
# Author: Jesús Manuel Mager Hois
# e-mail: <fongog@gmail.com>
# Project website: http://turing.iimas.unam.mx/wix/

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
import re

def normwix(text):
    text = text.lower()
    text = re.sub(r"´", "'", text, flags=re.IGNORECASE)
    #text = re.sub(r"'", "", text, flags=re.IGNORECASE)
    text = re.sub(r"v", "w", text, flags=re.IGNORECASE)
    text = re.sub(r"(c|qu)", "k", text, flags=re.IGNORECASE)
    text = re.sub(r"[0-9]+", "", text, flags=re.IGNORECASE)
    text = re.sub(r"ch", "ts", text, flags=re.IGNORECASE)
    text = re.sub(r"rr", "x", text, flags=re.IGNORECASE)
    text = re.sub(r" +", " ", text, flags=re.IGNORECASE)
    text = re.sub(r"[üï]", "+", text, flags=re.IGNORECASE)
    text = re.sub(r"^ ", "", text, flags=re.IGNORECASE)
    text = re.sub(r"(?<!t|\[)s", "ts", text, flags=re.IGNORECASE)
    text = re.sub(r"[áàä]", "a", text, flags=re.IGNORECASE)
    text = re.sub(r"[éèë]", "e", text, flags=re.IGNORECASE)
    text = re.sub(r"[íì]", "i", text, flags=re.IGNORECASE)
    text = re.sub(r"[óòö]", "o", text, flags=re.IGNORECASE)
    text = re.sub(r"[úù]", "u", text, flags=re.IGNORECASE)


    text = re.sub(r"([a-z+])\1+", r"\1", text, flags=re.IGNORECASE)
    return text


def tokenizewix(text):
    text = re.sub(r"(?<![\s])([.|,|,\-,\"|:|;|¿|?|¡|!])", r" \1", text)
    text = re.sub(r"([.|,|,\-,\"|:|;|¿|?|¡|!])(?<![\s])", r"\1 ", text)
    return text

if __name__ == "__main__":
    l = 4
    if len(sys.argv) < 2:
        print("normwix.py normalize and tokenize text in wixárika (huichol) ")
        print("language. It has GPL licence, so feel free to share it.")
        print("     normwix.py [-a|-n|-t|-p|-h] inputfile [outputfile]")
        print("         -a all: normalize and tokenize")
        print("         -n normalize")
        print("         -t tokenize")
        print("         -p print output")
        print("         -h this help")
        sys.exit()
    op = sys.argv[1]
    if not "-" in op:
        l = 3
        op = "a"
        infile = sys.argv[1]
    else:
        infile = sys.argv[2]
        if "p" in op:
            l = 2 
        else:
            outfile = sys.argv[3]
            Fo = open(outfile, "w")


    Fi = open(infile, "r")
    text = Fi.read()
    Fi.close()
    if ("n" in op) or ("a" in op):
        text = normwix(text)
    if ("t" in op) or ("a" in op):
        text = tokenizewix(text)
    try:
        Fo.write(text)
        Fo.close()
    except:
        print(text)
