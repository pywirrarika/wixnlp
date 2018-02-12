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



import pickle
import os
from optparse import OptionParser

class M3grams():
    def __init__(self, debug=False):
        self.debug = debug
        self.morphgrams = {}

    def train(self, filename):
        "Train the model"
        morphfreq = {}
        binfilename=os.path.join(os.path.dirname(__file__), 'wix/morph3grams.pickle')
        count = 0

        F = open(filename).read().split("\n")

        # Counting frequencies of morphems pairs in the corpus. We use segmented 
        # words by -. 
        for line in F:
            morphs= line.split()
            for i in range(len(morphs)):
                try:
                    prev2 = morphs[i-2]
                    prev1 = morphs[i-1]
                    now = morphs[i]
                except IndexError:
                    prev2 = "#"
                    now = morphs[i]
                    try:
                        prev1 = morphs[i-1]
                        now = morphs[i]
                    except IndexError:
                        prev1 = "#"
                count = count + 1
                #if self.debug:
                #    print(prev2, prev1, now)
                try:
                    morphfreq[(prev2, prev1, now)] = morphfreq[(prev2, prev1, now)] + 1
                except KeyError:
                    morphfreq[(prev2, prev1, now)] = 1

        # Then we generatethe propabailites
        for gram in morphfreq.keys():
            self.morphgrams[gram] = float(morphfreq[gram])/float(count)

        with open(binfilename, "wb") as F:
            pickle.dump(self.morphgrams, F, pickle.HIGHEST_PROTOCOL)


    def load(self, filename=os.path.join(os.path.dirname(__file__), 'wix/morph3grams.pickle')):
        with open(filename, 'rb') as f:
            self.morphgrams = pickle.load(f)
        #if self.debug:
        #    print("Size of model:", str(len(self.morphgrams)))

    def prob(self, segword):
        """ Return the probability of a given list of wixarika morphemes"""
        count = 0
        sum_prob = 0
        for i in range(len(segword)):
            try:
                prev2 = segword[i-2]
                prev1 = segword[i-1]
                now = segword[i]
            except IndexError:
                prev2 = "#"
                now = segword[i]
                try:
                    prev1 = segword[i-1]
                    now = segword[i]
                except IndexError:
                    prev1 = "#"
 

            try:
                sum_prob = sum_prob + self.morphgrams[(prev2, prev1, now)]
            except KeyError:
                pass

            count = count+1
        prob = sum_prob / count
        return prob

    def best(self, words, tag=False):
        """Returns the most probable segmentation option of a list"""
        max = -1
        seg = []
        ane = []
        for word in words:
            if tag:
                li = [m[1]+m[0] for m in word]
            else:
                li = [m[1] for m in word]
            if "'ane" in li or "ane" in li:
                ane.append(li)
                continue
            prob = self.prob(li)
            if self.debug:
                print(str(li), ":", str(prob))
            if prob > max:
                seg = li
                max = prob

        if ane:
            max = -1
            seg = []
            for word in ane:
             prob = self.prob(li)
            if self.debug:
                print(str(li), ":", str(prob))
            if prob > max:
                seg = li
                max = prob

        return seg
        
# This script trains a 2-gram model where the grams
# are morphemes of a segmented wixarika corpus. 

class Mgrams():
    def __init__(self, debug=False):
        self.debug = debug
        self.morphgrams = {}

    def train(self, filename):
        "Train the model"
        morphfreq = {}
        binfilename=os.path.join(os.path.dirname(__file__), 'wix/morphgrams.pickle')


        F = open(filename).read().split("\n")
        count = 0
        #if self.debug:
        #    print("Corpus size:", len(F))

        # Counting frequencies of morphems pairs in the corpus. We use segmented 
        # words by -. 
        for line in F:
            #wixline = line.split("=")[0]
            morphs = line.split()
            for i in range(len(morphs)):
                try:
                    prev = morphs[i-1]
                    now = morphs[i]
                except IndexError:
                    prev = "#"
                count = count + 1
                try:
                    morphfreq[(prev, now)] = morphfreq[(prev, now)] + 1
                except KeyError:
                    morphfreq[(prev, now)] = 1

        # Then we generatethe propabailites
        for gram in morphfreq.keys():
            self.morphgrams[gram] = float(morphfreq[gram])/float(count)

        #print(count)
        #print(self.morphgrams)

        with open(binfilename, "wb") as F:
            pickle.dump(self.morphgrams, F, pickle.HIGHEST_PROTOCOL)


    def load(self, filename=os.path.join(os.path.dirname(__file__), 'wix/morphgrams.pickle')):
        with open(filename, 'rb') as f:
            self.morphgrams = pickle.load(f)
        #if self.debug:
        #    print("Size of model:", str(len(self.morphgrams)))

    def prob(self, segword):
        """ Return the probability of a given list of wixarika morphemes"""
        count = 0
        sum_prob = 0
        for i in range(len(segword)):
            try:
                prev = segword[i-1]
                now = segword[i]
            except IndexError:
                now = segword[i]
                prev = "#"

            try:
                sum_prob = sum_prob + self.morphgrams[(prev, now)]
            except KeyError:
                pass

            count = count+1
        prob = sum_prob / count
        return prob

    def best(self, words, tag=False):
        """Returns the most probable segmentation option of a list"""
        max = 0
        seg = []
        for word in words:
            if tag:
                li = [m[1]+m[0]for m in word]
            else:
                li = [m[1] for m in word]
            prob = self.prob(li)
            if self.debug:
                print(str(li), ":", str(prob))
            if prob > max:
                seg = li
                max = prob
        return seg
        


if __name__ == "__main__":
    
    x = [[('1', 'xe'), ('', 'wit+')], [('1', 'xe'), ('', 'wi'), ('-1', 't+')], [('1', 'xe'), ('', 'wi'), ('-11', 't+')], [('1', 'xe'), ('', 'wi'), ('-12', 't+')], [('1', 'xe'), ('', 'wi'), ('-19', 't+')], [('1', 'xe'), ('', 'wi'), ('-21', 't+')], [('1', 'xe'), ('', 'wi'), ('-23', 't+')]]
    
    mgrams = Mgrams(debug=True)
    mgrams.load()
    mgrams.best(x)


        
