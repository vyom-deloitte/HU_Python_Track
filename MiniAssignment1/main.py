from itertools import permutations
from collections import Counter
class Stringclass:
    string="nba"
    def __init__(self):
        print("Enter the string")
        self.string = input()


    def length(self):
        return len(self.string)
    def tolist(self):
        return list(self.string)


class EqualSumPairs:
    def totalcount(self):
        self.count=permutations(list(self.string))
        print(self.count)


class SearchCommonElements(Stringclass):
    StringClassString = ""
    PairPossibleString = ""

    arr = []

    def __init__(self, a, b):
        self.StringClassString = a
        self.PairPossibleString = b

    def common(self):
        dict = {}
        for char in self.StringClassString:
            if char in dict:
                continue
            else:
                dict[char] = 1;
        for char in self.PairPossibleString:
            if char in dict:
                self.arr.append(char)
                dict.pop(char)

    def printList(self):
        print("The common elements are :: ")
        print(self.arr)


class Pairpossible(Stringclass):
    arr = []
    string="abcd"
    def __init__(self):
        print("Enter the second string")
        self.string = input()

    def pair(self):
        for i in range(len(self.string)):
            for j in range(i + 1, len(self.string)):
                self.arr.append(self.string[i] + self.string[j])
    def show(self):
        print(self.arr)



class EqualSumPairs(Pairpossible):
    arr = Pairpossible.arr
    def __init__(self):
        pass
    def countPairs(self):
        # print(self.arr)
        count = 0
        dict = {}
        for i in range(len(self.arr)):
            sum = int(self.arr[i][0]) + int(self.arr[i][1])
            # print(sum)
            if str(sum) in dict:
                dict[str(sum)] = dict[str(sum)] + 1
            else:
                dict[str(sum)] = 1
        for key, val in dict.items():
            if val == 1:
                count = count + 1
        return count


objstringclass=Stringclass()
print("Length of string is: ",objstringclass.length())
print("String converted to list: ",objstringclass.tolist())
objpairpossible=Pairpossible()
print("All possible pairs are: ")
objpairpossible.pair()
objpairpossible.show()

objsearchcommonelements=SearchCommonElements(objstringclass.string,objpairpossible.string)
objsearchcommonelements.common()
objsearchcommonelements.printList()
eqsc=EqualSumPairs()
print("unique sum count",eqsc.countPairs())

