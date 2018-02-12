#!/usr/bin/env python3

import sys 
import optparse

from wixnlp.wmorph import Verb
from wixnlp.morphgrams import Mgrams, M3grams

def test(debug=False):

    wix_seg_model= "segtest/model0.bin"
    wix_seg_model1= "segtest/model.bin"
    wix_seg = "segtest/testseg.wix"
    wix_non_seg = "segtest/testnseg.wix"
    wix_seg_train = "segtest/trainseg.wix"

    # Hyp files
    wix_wixnlp_alone_hyp = "segtest/wixnlp-alone.hyp.wix"
    wix_wixnlp_hyp = "segtest/wixnlp.hyp.wix"
    wix_wixnlp3_hyp = "segtest/wixnlp3.hyp.wix"


    Fseg = open(wix_seg, "r")
    Fnon = open(wix_non_seg, "r")

    FWixnlpA = open(wix_wixnlp_alone_hyp, "w")
    FWixnlp = open(wix_wixnlp_hyp, "w")
    FWixnlp3 = open(wix_wixnlp3_hyp, "w")

    non = Fnon.read().split("\n")

    #Load wixnlp segmentator
    mgrams = Mgrams(debug=debug)
    mgrams.train(wix_seg_train)
    mgrams.load()

    m3grams = M3grams(debug=debug)
    m3grams.train(wix_seg_train)
    m3grams.load()

    for i in range(len(non)):
        print(non[i])
        v = Verb(non[i])

        ### Simple WixNLP Segmentation
        path_op = []
        max = 0
        for p in v.paths:
            if len(p) > max:
                path_op = p
                max = len(p)
        pa = [e[1] for e in path_op]
        if len(pa) == 0:
            print(non[i], file=FWixnlpA)
        else:
            print(" ".join(pa), file=FWixnlpA) 

        ### MGrams Segmentation
        path = mgrams.best(v.paths)
        path3 = m3grams.best(v.paths)
        if len(path) == 0:
            print(non[i], file=FWixnlp)
        else:
            print(" ".join(path), file=FWixnlp)

        if len(path3) == 0:
            print(non[i], file=FWixnlp3)
        else:
            print(" ".join(path3), file=FWixnlp3)


def segment(word, model='3grams', verbose=True):
    wix_seg_train = "segtest/trainseg.wix"
    v = Verb(word)

    if model=='simple':
        path_op = []
        max = 0
        for p in v.paths:
            if len(p) > max:
                path_op = p
                max = len(p)
        pa = [e[1] for e in path_op]
        if len(pa) == 0:
            print(word)
        else:
            print(" ".join(pa))
        pass

    elif model=='2grams':
        mgrams = Mgrams(debug=verbose)
        mgrams.train(wix_seg_train)
        mgrams.load()
        path = mgrams.best(v.paths)
        if len(path) == 0:
            print(word)
        else:
            print(" ".join(path))

    elif model=='3grams':

        m3grams = M3grams(debug=verbose)
        m3grams.train(wix_seg_train)
        m3grams.load()
        path3 = m3grams.best(v.paths)

        if len(path3) == 0:
            print(word)
        else:
            print(" ".join(path3))

    else:
        print('Unknown model')
        return 0



if __name__ == '__main__':

    parser = optparse.OptionParser("usage: %prog [options] word")
    parser.add_option("-v", "--verbose", action="store_true", dest="debug", default=False, help="Print verbose output")
    parser.add_option("-m", "--model", dest="model", default="3grams", type="string", help="Model for segmentation: simple, 2grams, 3grams")

    (options, args) = parser.parse_args()

    debug = options.debug
    model = options.model

    if len(args) == 0:
        test(debug=debug)
    elif len(args) == 1:
        word = args[0] 
        segment(word, model=model, verbose=debug)

    else:
        parser.error("Too much arguments")
        


