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
import codecs

#prefixes and affixes of wixarika verbs
from wix.wixaffixes import pre, post

class Verb:
    def __init__(self, verb, debug=0):
        self.verb = verb.lower()
        #print(self.verb)
        self.paths = []
        self.roots = []
        self.rootslarge = []
        self.debug=debug
        Fl = codecs.open("steam.large", mode="r", encoding="utf-8")
        F = codecs.open("steam", mode="r", encoding="utf-8")
        line = F.readline()
        while 1:
            line=line.replace("\n", "")
            self.roots.append(line)
            line=F.readline()
            if not line:
                break
        if self.debug:
            print("**************************")
            print(self.roots)

        line = Fl.readline()
        while 1:
            line=line.replace("\n", "")
            self.rootslarge.append(line)
            line=Fl.readline()
            if not line:
                break
        if self.debug:
            print("**************************")
            print(self.rootslarge)


        self.start()

    def start(self, prev="", pos=0, path=[]):
        if pos > len(pre)-1:
            return
        if self.debug:
            print("New branch: ", str(pos), str(prev), str(path))
        gotone = False
        for s in pre[pos]:
            s_reg = s.replace("+", "\+")
            prev_reg=prev.replace("+", "\+")
            if self.debug:
                print("Searching ^"+prev_reg+s_reg+"+")
            reg = re.compile("^"+prev_reg+s_reg+"+")
            m = reg.match(self.verb)
            if m:
                gotone= True
                if self.debug:
                    print("Found:" + str(pos) + m.group())
                nprev = m.group()
                npath = list(path)
                npath.append((""+str(pos)+"", s))
                self.start(nprev, pos+1, npath)
                nprev = nprev.replace("+","\+")
                for root in self.roots:
                    root2 = root.replace("+","\+")
                    rootmatch=re.compile("^"+nprev+root2+"+")
                    rm = rootmatch.match(self.verb)
                    if rm:
                        if self.debug:
                            print("Found:" + "[root]" + rm.group())
                            print("Found:" + "[root]" + root)
                        nrprev = rm.group()
                        nrpath = list(npath)
                        nrpath.append(("", root))#id of steam TODO
                        
                        if self.debug:
                            print(nrprev)
                        if len(self.verb) == len(nrprev):
                            self.paths.append(nrpath)
                        self.end(prev=nrprev,path=nrpath)
                        continue
        if not gotone:
            if pos > 17:
                return
            self.start(prev, pos+1, path)
            return
    def end(self, prev="", pos=1, path=[]):
        if pos <= 0 or pos >= len(post):
            return
        if self.debug:
            print("Actual path", prev)
        if len(prev) == len(self.verb):
            if self.debug:
                print(path)
            return
        gotone=False        
        if self.debug:
            print(str(-pos), str(post[-pos]))
        for s in post[-pos]:
            if self.debug:
                print("Actual suffix:", s, "at pos", str(pos))
            s_reg = s.replace("+", "\+")
            prev_reg= prev.replace("+", "\+")
            if self.debug:
                print("Searching ^"+prev_reg+s_reg+"+")
            reg = re.compile("^"+prev_reg+s_reg+"+")
            m = reg.match(self.verb)
            if m:
                gotone= True
                if self.debug:
                    print("Found:" + str(pos) + m.group())
                nprev = m.group()
                if self.debug:
                    print("Next search:", nprev)
                npath = list(path)
                npath.append(("-"+str(pos)+"", s))
                
                if len(self.verb) == len(nprev):
                    self.paths.append(npath)
                self.end(nprev, pos+1, npath)
        if not gotone:
            self.end(prev, pos+1, path)

class Word:
    def __init__(self, model_file):
        F = codecs.open("dic", mode="r", encoding="utf-8")
        self.dic = {}
        self.symbols = '!¡"¿?,.'
        self.model = io.read_binary_model_file(model_file)

        line = F.readline()
        while line:
            line = line.split()
            if line:
                self.dic[line[0]] = line
            line = F.readline()
    def checkdic(self,word):
        if word in self.dic.keys():
            try:
                pos = self.dic[word][1]
            except:
                pos =""
            print(word, end=" ")
        else:
            if word in self.symbols:
                print(word, end=" ")
            else: 
                #print(word, "[Nid]", end=" ")
                seg = self.model.viterbi_segment(word)
                for affix in seg[0]:
                    print(affix, end=" ")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Formato:")
        print("     wmorph.py word")
        sys.exit()
    v = Verb(sys.argv[1], debug=1)
    print("Found paths")
    print(v.paths)

