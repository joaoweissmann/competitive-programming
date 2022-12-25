def main():
    n = int(input())
    
    s = set()
    for i in range(n):
        s.add(i+1)
    
    line = input()
    for x in line.split():
        s.remove(int(x))
    
    for i in s:
        print (i, sep=" ", end=" ")

if (__name__=="__main__"):
    main()

