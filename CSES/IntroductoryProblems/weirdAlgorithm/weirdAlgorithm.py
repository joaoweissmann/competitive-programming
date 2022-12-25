def main():
    n = int(input())
    print(n, end=" ")
    while (n != 1):            
        if ((n % 2) == 0):
            n = int(n / 2)
        elif ((n % 2) != 0):
            n = int(n * 3 + 1)
        print(n, end=" ")

if (__name__ == "__main__"):
    main()

