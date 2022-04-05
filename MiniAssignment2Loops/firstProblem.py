def patternFirst():
    n = int(input('Enter number of rows required: '))
    rows=n
    cols=n
    arr = [[0 for j in range(cols)] for i in range(rows)]
    arr[0][0] = 1
    for i in range(1, rows):
        arr[i][0] = 1
        for j in range(1, cols):
            arr[i][j] = arr[i - 1][j - 1] + arr[i - 1][j]
    print("The triangle is : ")
    for i in range(rows):
        for j in range(cols):
            print(arr[i][j], end='')
        print()

patternFirst()
