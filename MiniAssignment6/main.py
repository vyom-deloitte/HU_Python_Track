# write a decorator which will take a function and execute it twice.
# Function is -
# def multiply(num1, num2):
#     print(num1 * num2)
def decorator(func):
    print("Problem 1, write a decorator which will take a function and execute it twice.")
    def inner(x, y):
        func(x, y)
        func(x, y)

    return inner

@decorator
def multiply(x, y):
    print("Answer of multiplication is ::", x * y)

multiply(3, 5)


# Create a generator to return the fibonnaci sequence starting from the first element
# up to (n). The first numbers of the sequence are: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,
# 89, . . .
def fibonacci(n):
    print()
    print("Problem 2, Create a generator to return the fibonnaci sequence starting from the first element.")
    if n == 1:
        return 0
    if n == 2:
        yield 0
        yield 1

    first = 0
    yield first
    second = 1
    yield second
    count = 3
    while count <= n:
        next = first + second
        yield next
        first = second
        second = next
        count = count + 1
generator = fibonacci(50)
for i in generator:
    print(i)