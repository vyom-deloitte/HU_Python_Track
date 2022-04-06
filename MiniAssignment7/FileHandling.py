#Write a python program to identify the longest words in a file, a.txt
def longest_words(filename):
    with open(filename, 'r') as infile:
        words = infile.read().split()
    max_len = len(max(words, key=len))
    return [word for word in words if len(word) == max_len]

print("longest word in a file is: ")
print(longest_words('a.txt'))