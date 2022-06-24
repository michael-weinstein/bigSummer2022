
class DNASequence:

    def __init__(self, sequence:str):
        self.sequence = sequence
        self._baseCounts = self.getBaseCounts()
        # self.a = self.baseCounts["A"]
        # self.c = self.baseCounts["C"]
        # self.g = self.baseCounts["G"]
        # self.t = self.baseCounts["T"]

    def getBaseCounts(self):
        baseCounts = {
            "A":0,
            "C":0,
            "G":0,
            "T":0
        }
        for base in self.sequence:
            baseCounts[base] += 1
        return baseCounts

    def __str__(self):
        return self.sequence

    @property
    def a(self):
        return self._baseCounts["A"]

    @a.setter
    def a(self, value:int):
        self._baseCounts["A"] = value

    @property
    def c(self):
        return self._baseCounts["C"]

    @c.setter
    def c(self, value:int):
        self._baseCounts["C"] = value

    @property
    def t(self):
        return self._baseCounts["T"]

    @t.setter
    def t(self, value:int):
        self._baseCounts["T"] = value

    @property
    def g(self):
        return self._baseCounts["G"]

    @g.setter
    def g(self, value:int):
        self._baseCounts["G"] = value




if __name__ == "__main__":
    sequence = "TAAAGCGTGGCCAGGGCATTCCAACTCCTTCATTTAGCACAACGGTGGCCAGCGCATAAGTCTCGTAGTACGTTGAGGTTAAGCGGATCACACTCCCGGTGTTCTGTTAGGCACAGAATCTTACCGACTACCCTCTACTCGTATGCGCTTCCGGCCTATCTCTGCTTATAATATTATCCTGCTTCCCTTCAGCTGCTGTGTCAACTGTCTACGCTATTTGGTACTGAAGACTCTTAGAATTGGGCCATACGGATTACTCATGACAGCACAATTTCAATATGGTATGAGATAGATAAGGCGCTTATGTGGGAGTACCGTTTTTGAGGGTCCTACTGGATCAAACCCCGAAGCTTTCATATGGGTCTCATTAGCGAAGGTGTCAGGGACAAGGAATGAAACCTACTAGCGACGATTGGAGTTAATCACCTCCCTCCCTACGACCACTGATTTATGTCCAGTTGCTGAGAACGTCATGGGACCCGCCACAAGGTACAGCCGGGTCAGTTGTGCCAGCCCATTAATGACCCACCCTATCTTGAGGGTCATGCAATCCGTTCTGTTAGGTCGGGACGCGCACGGTGTGGGGAGTTGTGGGAGACCCCAGTCTATTAGCTTGCCTCTCAGACTGTCTCGGTTACGATTGCACATTTTCCGGAATTCTACACCCATCCGGGGTAACAGCGCTGTGGTCTCGGGAAAGCGAGGTCCGCAGGGACCTCTTAGGCCAATTACATATAGCGTTGAACGCTCGGAATAGACGGGGCGTGCATGGAGTGCACGGGGTTGGCCAAGCTGTAAGAAATCGATACTATATACATCAAACTCTCGAAGGTGAGGTTGGAGCATGAGGAAGATGGCTAATGTGTATAAGAAACCTGTTCTCCTT"
    seqHandler = DNASequence(sequence)
    outputs = (seqHandler.a, seqHandler.c, seqHandler.g, seqHandler.t)
    print("%s %s %s %s" %outputs)
    seqHandler.a = 5
    print(seqHandler.a)
    print(seqHandler._baseCounts["A"])