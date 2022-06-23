import typing
import os

def returnEvenLinesOfStream(text:typing.TextIO) -> typing.List[str]:
    lineCollection = []
    oddLine = True
    for line in text:
        if not oddLine:
            lineCollection.append(line.strip())
        oddLine = not oddLine
    #lineCollection.append(42)
    return lineCollection

def rejoinLines(lineCollection:typing.List[str]) -> str:
    #lineCollection = [str(item) for item in lineCollection]
    rejoined = "\n".join(lineCollection)
    return rejoined

def getFileStream(path:str) -> typing.TextIO:
    if not os.path.isfile(path):
        raise FileNotFoundError("Unable to find file at %s" %path)
    return open(path, 'r')

if __name__ == "__main__":
    fileName = "rosalind_ini5 (1).txt"
    stream = getFileStream(fileName)
    evenLines = returnEvenLinesOfStream(stream)
    stream.close()
    rejoined = rejoinLines(evenLines)
    print(rejoined)