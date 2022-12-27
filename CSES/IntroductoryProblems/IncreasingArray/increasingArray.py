def main():
    n = int(input())
    line = input()
    v = []
    for el in line.split():
        v.append(int(el))
    count = 0
    for i in range(len(v)):
        if i == 0:
            continue
        else:
            curr = v[i]
            prev = v[i-1]
            if (curr < prev):
                count += prev - curr
                v[i] += prev - curr
    print (count)

if (__name__ == "__main__"):
    main()
