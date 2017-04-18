import re

def plurales(es):
    newes = re.sub(r'([aeoi])$', r'\1s', es)
    if newes:
        es = newes
    newes = re.sub(r'([lnr])$', r'\1es', es)
    if newes:
        es = newes

    #if newesr2:
    #    es = newesr2
    return es
    

d = "/home/gog/wixes/dic.txt"

F = open(d)

for line in F:
    (wix, es) = line.split(" = ")
    es = es[:-1]
    if "[s]" in wix:
        wixnew = wix.split(" [s]")
        if wixnew[-1] == "":
            wixnew = wixnew[:-1]
        if len(wixnew) > 1:
            ples = plurales(es)
            print("".join(wixnew[:-1]), "=", es) 
            if wixnew[-1][0] == " ":
                print("-".join(wixnew[:-1]),"-",wixnew[-1][1:], " = ", ples, sep="")
            else: 
                print(wixnew)
        else:
            print(wixnew[0], "=", es)

    
    if "[p]" in wix:
        wixnew = wix.replace(" [p]", "")
        print(wixnew, "=", es)


