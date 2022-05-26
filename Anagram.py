# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


def find_anagrams(word1, word2):
    # [assignment] Add your code here
    first_word = sorted(word1)
    sec_word = sorted(word2)


    if len(word1) != len(word2):
        return False
    


    if first_word == sec_word:
        return True
    
    else:
        return False
    
#Don't forget to call your function

