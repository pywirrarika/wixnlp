
class morph():
    def __init__(self, filename):
        self.F = open(filename, "r")
        self.morphs = {}

    def read(self):
        for line in self.F:
            seg = line.replace("\n", "")
            for moprh in seg.split():
                try:
                    self.morphs[morph] += 1
                except KeyError:
                    self.morphs[moprh] = 1
            print(seg)
    def print(self):
        print("Seen morphs:")
        print(self.morphs.keys())


if __name__ == "__main__":
    M = morph("trainseg.wix")
    M.read()
    M.print()
