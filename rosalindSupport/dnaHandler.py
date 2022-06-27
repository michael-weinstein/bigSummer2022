import re
import typing

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

    def gcContent(self):
        totalGC = self.g + self.c
        totalBases = totalGC + self.a + self.t
        return totalGC/totalBases

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

    def hammingDistance(self, other:["DNASequence", str]) -> int:
        """
        Measures the edit distance between the sequence object and another sequence
        :param other: The sequence to compare. Must be the same length. Can be either a string or a DNAsequence object
        :return: Integer indicating the edit distance between the two sequences
        """
        otherSeq = str(other)
        if len(self.sequence) != len(otherSeq):
            raise ValueError("Both sequences must be of the same length")
        mismatches = 0
        for selfBase, otherBase in zip(self.sequence, otherSeq):
            if selfBase != otherBase:
                mismatches += 1
        return mismatches

    def findSubstring(self, substring:str) -> typing.List[int]:
        matchIndices = []
        start = 0
        end = start + len(substring)
        while end < len(self.sequence):
            sliceText = self.sequence[start:end]
            if sliceText == substring:
                matchIndices.append(start + 1)
            start += 1
            end += 1
        return matchIndices

    @property
    def length(self):
        return len(self.sequence)

    def __len__(self):
        return self.length
