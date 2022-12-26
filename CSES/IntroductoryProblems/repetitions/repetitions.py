def main():
    dna = input()
    bestCount = 0
    currCount = 0
    prev = ""
    for i, curr in enumerate(dna):
        if (i == 0):
            currCount = 1
        else:
            if (curr == prev):
                currCount += 1
            else:
                currCount = 1
        if (currCount > bestCount):
            bestCount = currCount
        prev = curr
    print (bestCount)

if (__name__ == "__main__"):
    main()
