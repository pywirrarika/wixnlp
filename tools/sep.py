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


def split(infile):
    root = infile
    text = open(infile+".wixes", "r")
    es = open(root+".wix", "w")
    wix = open(root+".es", "w")

    i = 0
    for line in text:
        if "=" in line:
            line = line.split("=")
            if line[0] == "" or line[1]=="":
                print("Error en:", line)
                sys.exit()

            es.write(line[0] + "\n")
            w = line[1].replace("\n", "")
            wix.write(w + "\n")
            i = i + 1
        else:
            print("Ignored: ", line, end="")
    print("     We got ", str(i), "aligned phrases.")
    text.close()
    wix.close()
    es.close()


def merge(infile):
    root = infile
    text = open(infile+".wixes", "w")
    es = open(root+".wix", "r")
    wix = open(root+".es", "r")

    esline = es.readline()
    wixline = wix.readline()
    while (esline and wixline):
        esline = esline.replace("\n", "")
        wixline = wixline.replace("\n", "")
        text.write(esline+" = "+wixline+"\n")
        esline = es.readline()
        wixline = wix.readline()
   
    text.close()
    wix.close()
    es.close()


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("sep.py splits or merges an wixes file. An wixes file contains a pair")
        print("of phrases in wixárika and spanish, separeted by an = symbol")
        print("The in file must be *.wixes; or a root that shares .es and .wix")
        print("usage: sep.py infile [-s|-m]")
        print("     -s split the file (default)")
        print("     -m merge two files")
        sys.exit()

    infile = sys.argv[1] 

    try:
        op = sys.argv[2] 
    except:
        op = "-s" 

    if "s" in op:
        split(infile)
    else:
        merge(infile)

