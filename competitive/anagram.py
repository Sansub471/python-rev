
# Check if two strings are anagram
# Anagrams have same characters but in different order
# E.g. 'act' and 'tac'
# Both characters and their frequency same

def charCount(string:str)->dict:
    char_count = {}
    string = string.lower()
    for char in string:
        if char not in char_count.keys():
            char_count[char] = 1
        else:
            char_count[char] += 1
    return char_count


def Anagram(a:str, b:str):
    if charCount(a) == charCount(b):
        return True
    else:
        return False
    

print(Anagram('fact', 'tfac'))

# Examples :
# "listen" and "silent"
# "triangle" and "integral"
# "debit card" and "bad credit"
# "astronomer" and "moon starer"
# "schoolmaster" and "the classroom"
# "cinema" and "iceman"
# "debit" and "bited"
# "funeral" and "real fun"
# "anagram" and "nag a ram"
# "restful" and "fluster"

anagrams = [
    ["listen", "silent"],
    ["triangle", "integral"],
    ["debitcard", "badcredit"],
    ["astronomer", "moonstarer"],
    ["schoolmaster", "theclassroom"],
    ["cinema", "iceman"],
    ["debit", "bited"],
    ["funeral", "realfun"],
    ["anagram", "nagaram"],
    ["restful", "fluster"]
]

for word1, word2 in anagrams:
    print(Anagram(word1, word2))

# Tip : For first word increment the value for each character and for second word decrement the value
# In the end, if all values are zero then the words are anagram otherwise not.
