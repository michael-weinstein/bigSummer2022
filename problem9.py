import rosalindSupport



if __name__ == "__main__":
    fastaDict = rosalindSupport.fileReader.fasta2Dict("rosalind_gc.txt")
    gcList = []
    for seqID, dna in fastaDict.items():
        gcList.append((dna.gcContent(), seqID))
    gcList.sort()
    for line in gcList:
        print(line)