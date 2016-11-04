#!/usr/bin/env python3

import sys
import codecs
from wmorph import Verb

class Word:
    def __init__(self):
        F = codecs.open("dic", mode="r", encoding="utf-8")
        self.dic = {}
        self.symbols = '!¡"¿?,.'

        line = F.readline()
        while line:
            line = line.split()
            if line:
                wr = line[0].replace('\n', '')
                self.dic[wr] = line
            line = F.readline()

    def checkdic(self,word):
        if word in self.dic.keys():
            return (word, 1)
        else:
            if word in self.symbols:
                return (word, 1)
            else: 
                return (word, 0)


def segment(line, joinm=1, s=0):
    debug=0
    F = codecs.open("dic", mode="r", encoding="utf-8")
    w = Word()
    
    tokens = line.split()

    words = []

    for token in tokens:
        word = Verb(token)
        typ = w.checkdic(token)
        if debug:
            print(typ)
        if typ[1] == 1:
            if debug:
                print("NOT VERB:", token)
            words.append(token)
        else:
            print("VERB:", token, str(word.paths))
            pathsize = 100000
            chpath=0
            for p in word.paths:
                if len(p) < pathsize:
                    chpath = p
                    pathsize = len(p)
            if chpath:
                for affix in chpath:
                    if not s:
                        words.append(str(affix[1])+str(affix[0]))
                    else:
                        words.append(str(affix[1]))

    if joinm:
        return " ".join(words)
    return words

def segtext(text, s=0):
    lines = text.split("\n")
    seglines = []
    for line in lines:
        seglines.append(segment(line, s=s))
    return "\n".join(seglines)

if __name__ == "__main__":
    alo = "'ik+ p+tuxa"
    words = segment(alo)
    print(words)



