def patternDiamond():
    #Left triangle pascal’s pattern
    rows = int(input('Enter number of rows required: '))

    k = 2 * rows - 2
    for i in range(0, rows):
        for j in range(0, k):
            print(end=" ")
        k = k - 1
        for j in range(0, i + 1):
            print("* ", end="")
        print("")

    k = rows - 2

    for i in range(rows, -1, -1):
        for j in range(k, 0, -1):
            print(end=" ")
        k = k + 1
        for j in range(0, i + 1):
            print("* ", end="")
        print("")

patternDiamond()

def patternHollowTraingle():
    #Hollow traingle pattern
    row = int(input('Enter number of rows required: '))

    for i in range(row):
        for j in range(row - i):
            print(' ', end='')  # printing space required and staying in same line

        for j in range(2 * i + 1):
            if j == 0 or j == 2 * i or i == row - 1:
                print('*', end='')
            else:
                print(' ', end='')
        print()  # printing new line

patternHollowTraingle()

def leftHollowTraingle():
    n = int(input("enter the no of rows:"))
    for r in range(0, n):
        for c in range(0, n):
            if r == 0 or c == (n - 1) or r == c:
                print('*', end='')
            else:
                print(end=' ')
        print()


leftHollowTraingle()