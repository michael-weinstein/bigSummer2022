

class DNASequence:

    def __init__(self, sequence:str):
        self.sequence = sequence
        self._baseCounts = self.getBaseCounts()

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

    def toRNA(self):
        return self.sequence.replace("T","U")

    def reverseComplement(self):
        complement = {
            "A":"T",
            "T":"A",
            "C":"G",
            "G":"C"
        }
        revComp = ""
        for base in self.sequence[::-1]:
            revComp += complement[base]
        return revComp

    @property
    def a(self):
        return self._baseCounts["A"]

    @property
    def c(self):
        return self._baseCounts["C"]

    @property
    def t(self):
        return self._baseCounts["T"]

    @property
    def g(self):
        return self._baseCounts["G"]


if __name__ == "__main__":
    sequence = "AATGAAACGAGTCGATGGTTCAGCGTAACTTGAACTCTGCTCCGTGGCACCACGCTAGGAGTGGTCAGTGCACCGCGATCTAATCTCTTCCTACTGTGACGCGGCACGGGCGACCCCGGGAGGTCGGAATTGTAGCGCGGGAGCGATCAGTTCCAGTGGTGATAGGCCTCGCGCTAGAGGCGCGATACAGTTTCTGTTGAATGGGCAGCTGACACGGCGGTCGGATACTAGCGGCGGGCCCGGGTAGCACAGCGTACAAATGGGAGCATATTATTCACTGGATACTTGAAATCGTTATTTCAACTGATAGTTTAAACGCAACCAGAGTCAATATATGGGTCTAGAAGCGGATCTGCGTTAGCACGGCATGAACGGCCGAGCGCCAATAGGGCGAGATTGGTTATCCCGAGCTAGCGCACTGCTGAACTCTTGGCCCCGCGTTGCGGGACGGGCAAAGTCGCAGCTGCGGTCCGTGGAGCACATGGCTCGCGTTTTCTTACCAACTCTTGGCCAATCACCGACGTCGACTAGTCTATCTACGTCAAAGTGCAGGCGATTCGCGGGAGCGGTCGGTCAGATCTTGTGTCCACCGGGAGCCAGGTAAGGCGTACCTAAAGCGTACATAAAACCCCAAGACGTTTGATATCGTGGGCCTAGCGTATTGCCCTGTGGTACCCAGTATGACGAACCTGTTCACCGCTACGTTACGTGCAGCTGATCTACTGTTCCCCTGGACGATTCACCCGGCTTATTAAGATGAGCCACGCCGGATGCCGACATAATATGCATCTGTTGGGGCCGTACCGTGTGAGTGGGATGCAAAACTGTGTAACCCCATTGTGTCCGTTAAGGGTCATAGCGGGACTCACCAGTAGCTTGAGACGTGAATGTGTTAGACGACTGGTTCTTCCTGTCTCCGAGGTA"
    seqHandler = DNASequence(sequence)
    print(seqHandler.reverseComplement())
