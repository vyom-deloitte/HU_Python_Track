#Map the dictionary
def MapDict():
    print("Dictionary Problem 1,map the dictionary in the following manner: ")
    keys = ["Ten", "Twenty", "Thirty"] #given key
    values = [10, 20, 30] #given value
    dictionary = {}
    for k in range(len(keys)):
        dictionary[keys[k]] = values[k]
    print(dictionary)
    print()
MapDict()


#Merge two Python dictionaries into one
def MergeDict():
    print("Dictionary problem2 ,merge two Python dictionaries into one: ")
    dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30} #given dictionary 1
    dict2 = {'Thirty': 33, 'Fourty': 40, 'Fifty': 50}#given dictionary 2
    for i in dict2:
        if i in dict1:
            dict1[i] = dict2[i]
        else:
            dict1[i] = dict2[i]
    print(dict1)
    print()
MergeDict()


#Rename key city to location in the following dictionary.
def ChangeKey():

    print("Dictionary problem 3 ,Rename key city to location in the following dictionary: ")
    sampleDict = {

        "name": "Kelly",

        "age": 25,

        "salary": 8000,

        "city": "New york" #We have to change this key "city" to "location"

    }
    print("Initially dictionary is")
    print(sampleDict)
    print("Finally after changing dictionary is")
    value = sampleDict["city"]
    del sampleDict["city"]
    sampleDict["location"] = value
    print(sampleDict)
    print()
ChangeKey()


#Convert Dictionary to list
def Convert():
    print("Dictionary problem 4 ,convert Dictionary to list: ")
    dict1 = {"HuEx": [1, 3, 4], "is": [7, 6], "best": [4, 5]}
    temp = []
    j = 0
    for i in dict1:
        temp.append(dict1[i])
        temp[j].insert(0, i)
        j += 1
        print(temp)
Convert()