from itertools import permutations
import pickle
from nltk.util import ngrams
def train_ngrams():
    Fes = open("../corpus/corpus.norm.es").read().split()
    data = {}

    permlen = 0

    for word in Fes:
        chrs = [c for c in word]
        twograms = ngrams(chrs,2)
        for g in twograms:
            try:
                data[g]=data[g]+1
            except KeyError:
                data[g]=1
            permlen = permlen + 1

    ngramses = {}
    for par in data.keys():
        ngramses[par] = data[par]/float(permlen)

    with open('esgrams.pickle', 'wb') as f:
        pickle.dump(ngramses, f, pickle.HIGHEST_PROTOCOL)


    Fes = open("../corpus/corpus.norm2.wix").read().split()
    data = {}

    chars = "abcdefghijkllmnopqrrstuvwxyzñáéíóúü+-1234567890'?¿!¡$&;.,ÁÉÍÓÚ:"
    permlen = 0

    for word in Fes:
        chrs = [c for c in word]
        twograms = ngrams(chrs,2)
        for g in twograms:
            try:
                data[g]=data[g]+1
            except KeyError:
                data[g]=1
            permlen = permlen + 1

    ngramswix = {}
    for par in data.keys():
        ngramswix[par] = data[par]/float(permlen)

    with open('wixgrams.pickle', 'wb') as f:
        pickle.dump(ngramswix, f, pickle.HIGHEST_PROTOCOL)

    print(data)

def classif(word, esmodel, wixmodel, verb=0):

    if verb:
        print(word)
    #with open('wixgrams.pickle', 'rb') as f:
    #    wixmodel= pickle.load(f)

    #with open('esgrams.pickle', 'rb') as f:
    #    esmodel= pickle.load(f)

    chrs = [c for c in word]
    twograms = ngrams(chrs,2)
    pes = 0
    pwix = 0
    i = 1
    for g in twograms:
        i=i+1
        try:
            pes = pes + esmodel[g]
        except KeyError:
            pass
    es = pes/float(i)

    i = 1
    twograms = ngrams(chrs,2)
    for g in twograms:
        i=i+1
        try:
            pwix = pwix + wixmodel[g]
        except KeyError:
            pass
    wix = pwix/float(i)

    if verb: 
        print("P(wix|word) =", str(wix))
        print("P(esp|word) =", str(es))

    if wix < es:
        if verb:
            print("ES")
        return 1
    else:
        if verb:
            print("WIX")
        return 0

if __name__ == "__main__":
    train_ngrams()
