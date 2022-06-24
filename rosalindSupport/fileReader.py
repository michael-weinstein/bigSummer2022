import typing
import os
from . import dnaHandler


def fasta2Dict(path:str) -> typing.Dict[str, dnaHandler.DNASequence]:
    if not os.path.isfile(path):
        raise FileNotFoundError("Unable to find file %s" %path)
    fastaDict = {}
    with open(path, 'r') as file:
        for line in file:
            if line.startswith(">"):
                currentSequenceID = line[1:].strip()
                fastaDict[currentSequenceID] = ""
            else:
                fastaDict[currentSequenceID] += line.strip()
    for sequenceID, sequence in fastaDict.items():
        fastaDict[sequenceID] = dnaHandler.DNASequence(sequence)
    return fastaDict
