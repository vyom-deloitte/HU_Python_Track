from itertools import permutations
from collections import Counter
class Stringclass:
    def __init__(self,inpt):
        self.string=inpt
    def length(self):
        return len(self.string)
    def tolist(self):
        return list(self.string)


# class EqualSumPairs:
#     def totalcount(self):


class SearchCommonElements(Stringclass):
    def commonElements(self):
        d=dict(Counter(list(self.string)))
        res=[]
        for j in d:
            if d[j]>=2:
                res.append(j)
        return res


class Pairpossible(Stringclass):

    def pair(self):
        self.perm=permutations(list(self.string))
        li=[]
        for i in self.perm:
            li.append(i)
            print(list(i), end=" ")
    def show(self):
        return self.li


print(" Enter your number string")
userinput=input()
objstringclass=Stringclass(userinput)
print("Length of string is: ",objstringclass.length())
print("String converted to list: ",objstringclass.tolist())
objpairpossible=Pairpossible(userinput)
print("All possible pairs are: ")
objpairpossible.pair()
objsearchcommonelements=SearchCommonElements(userinput)
print()
print("Common elements are: ",objsearchcommonelements.commonElements())
