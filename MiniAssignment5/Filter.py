from functools import reduce
# Convert a number to positive if it's negative in the list.
# Only pass those that are converted from negative to positive to the new list.
def FilterNegative():
    print("Problem 1")
    lst1 = [-1000, 500, -600, 700, 5000, -90000, -17500]
    print(lst1)
    print("Result :")
    res = list(map(lambda x: -x, list(filter((lambda x: x < 0), lst1))))
    print(res)
    print()

FilterNegative()

# Take the first two values, run the function on them.
# Then take the result and the next value and have a multiplication between them. etc.
# When no more values are left, return the last result.
def ReduceProb():
    print("Problem 2")
    lst1 = [-1000, 500, -600, 700, 5000, -90000, -17500]
    print(lst1)
    print("Result :")
    print(reduce(lambda x, y: x * y, lst1))
    print()

ReduceProb()

#  Using zip and dict functions create a dictionary which has its key-value pairs coming from lst1 and lst2.
# lst1=["Netflix", "Hulu", "Sling", "Hbo"]
# lst2=[198, 166, 237, 125]
def ZipDict():
    print("Problem 3")
    lst1 = ["Netflix", "Hulu", "Sling", "Hbo"]
    print(lst1)
    lst2 = [198, 166, 237, 125]
    print(lst2)
    print("Result :")
    res= zip(lst1, lst2)
    print(dict(res))
    print()

ZipDict()