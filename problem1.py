

def squareOfHyotenuse(aVal:int, bVal:int) -> int:
    aSquared = aVal ** 2
    bSquared = bVal ** 2
    hypotenuseSquared = aSquared + bSquared
    if hypotenuseSquared > 2:
        print("It's bigger than 2")
    return hypotenuseSquared

print("The imported package has __name__ of %s" %__name__)


if __name__ == "__main__":
    print("Hit the block")
    print(squareOfHyotenuse(909, 916))


