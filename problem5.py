import typing

def extractWordCount(inputString:str) -> typing.Dict[str, int]:
    inputList = inputString.split(" ")
    wordCounts = {}
    for word in inputList:
        if word not in wordCounts:
            wordCounts[word] = 0
        wordCounts[word] += 1
    return wordCounts

def printWordCounts(wordCounts:typing.Dict[str, int]) -> None:
    for word, count in wordCounts.items():
        print("%s %s" %(word, count))
    return None


if __name__ == "__main__":
    inputString = "When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be"
    wordCounts = extractWordCount(inputString)
    printWordCounts(wordCounts)