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
from .normwix import normwix, tokenizewix
from .seg import segment, segtext

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

