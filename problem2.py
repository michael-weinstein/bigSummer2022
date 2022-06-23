
def getSlice(string:str, start:int, end:int) -> str:
    slice = string[start:end + 1]
    return slice


if __name__ == "__main__":
    string = "9xzGwG3EsRYN9jSpq8o510xRzoFTSpalaxarZGJVl9tentaculatumIBQGiZOSL1yLjEgOFG9RrfDFayrBIjFNZ6VPw7Jx72Hl1mlIp2olrFrcM5tnorKRtwEnv6WUVwEtfylMjjTY152pDRcXRaavr9loEqVDAcl4wGJNTie5p9kvnMy5Rk4Rv4WjmaMQwNBrGz."
    start1 = 28
    end1 = 33
    start2 = 42
    end2 = 53
    slice1 = getSlice(string, start1, end1)
    slice2 = getSlice(string, start2, end2)
    print("%s %s" %(slice1, slice2))
