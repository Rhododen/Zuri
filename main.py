# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}
import string

def read_file_content(filename):
    # [assignment] Add your code here 
    f = open(filename, 'r')
    return f


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    my_dict = dict()
    text = text.read()
    for each_line in text:
        text = text.strip()
        text = text.upper()
        text = text.translate(text.maketrans('', '', string.punctuation))
        new_text = text.split(" ")


    for word in new_text:
        if word in my_dict:
            my_dict[word] = my_dict[word] + 1
        else:
            my_dict[word] = 1
    print(my_dict)     
    return my_dict

count_words()