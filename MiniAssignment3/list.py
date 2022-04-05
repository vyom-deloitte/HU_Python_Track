from collections import Counter
# 1.	Return all the duplicate values from list of arraylist
def DupValue():
    print("List problem 1, return all the duplicate values from list of arraylist: ")
    arry = [[1, 1, 3, 2], [9, 8, 8, 1], [0, 4, 5, 0, 0, 1, 4]] #given list
    print(arry)
    for i in arry:
        d = dict(Counter(i))
        for j in d:
            if d[j] > 1:
                print(j, "->", d[j], end=" ")
        print()
    print()
DupValue()

#Merge two lists
def MergeList():
    print("List Problem 2,merge two lists: ")
    mergedList = []
    list1 = ["Hello", "take"] #given list1
    list2 = ["Dear", "Sir"]   #given list2
    print("First list : ")
    print(list1)
    print("Second list : ")
    print(list2)
    for i in list1:
        for j in list2:
            mergedList.append(i + " " + j)
    print("Merged list : ")
    print(mergedList)
    print()
MergeList()


#Given a nested list extend it by adding the sub list ["h", "i", "j"]
def ExtendList():
    print("List Problem 3,Extend list by adding the sub list ")
    list = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"] #given list
    print(list)
    sub_list = ["h", "i", "j"] #given sublist
    list[2][1][2].extend(sub_list)
    print(list)
ExtendList()


