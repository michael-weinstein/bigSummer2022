
def isOdd(number:int) -> bool:
    if number % 2:
        return True
    return False

def sumOfOdds(start:int, end:int) -> int:
    if not isOdd(start):
        start += 1
    numberSet = range(start, end + 1, 2)
    collector = 0
    for number in numberSet:
        collector += number
    return collector



def sumOfOdds2(start:int, end:int) -> int:
    if not isOdd(start):
        start += 1
    numberSet = range(start, end + 1, 2)
    return sum(numberSet)


if __name__ == "__main__":
    start, stop = 4620, 9112
    print(sumOfOdds(start, stop))