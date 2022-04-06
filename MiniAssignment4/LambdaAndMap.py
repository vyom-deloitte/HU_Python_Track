#Using a lambda function take inputs as 4 integers and give the output for equation ax^2+bx+c
def Lambda():
    print("Problem1,Using a lambda function take inputs as 4 integers and give the output for equation ax^2+bx+c")
    print()
    a = int(input("Enter the value of a - "))
    b = int(input("Enter the value of b - "))
    c = int(input("Enter the value of c - "))
    x = int(input("Enter the value of x - "))
    res = lambda a, b, c, x: a * x * x + b * x + c
    print(res(a, b, c, x))
    print()
Lambda()

# Using map() function and lambda and count() function create a list consisted of the number of occurence of both letters: A and a.
# arr=["Alaska", "Alabama", "Arizona", "Arkansas", "Colorado", "Montana", "Nevada"]
def Map():
    print("Problem2,Using map() function and lambda and count() function create a list consisted of the number of occurence of both letters: A and a")
    print()
    arr = ["Alaska", "Alabama", "Arizona", "Arkansas", "Colorado", "Montana", "Nevada"]
    print(arr)

    # counting number of occurences of A
    resA = list(map(lambda n: n.count("A"), arr))
    print("Number of occurences of A: ", resA)

    # counting number of occurences of a
    resa = list(map(lambda n: n.count("a"), arr))
    print("Number of occurences of a: ", resa)

Map()