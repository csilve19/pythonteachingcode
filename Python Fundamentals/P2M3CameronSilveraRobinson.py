# [] create poem mixer function, call the function with the provided test string
# [] test string: `Little fly, Thy summer’s play My thoughtless hand Has brushed away. Am not I A fly like thee? Or art not thou A man like me?`  

def poem_mixer(word_list):    
    word_list.sort()
    new_words = []
    while len(word_list)>5:
        new_words.append(word_list.pop(-5))
        new_words.append(word_list.pop(0))
        new_words.append(word_list.pop())
    else:
        return new_words

string_input = input("Welcome Cameron Silvera-Robinson enter a saying or poem: ")
word_list = string_input.split()
list_length = len(word_list)
#print(list_length)

for length in range (0,list_length):
    if len(word_list[length]) <= 3:
        word_list[length] = word_list[length].lower()
    elif len(word_list[length]) >= 7:
        word_list[length] = word_list[length].upper()         
print(" ".join(poem_mixer(word_list)))
    

poem_mixer(word_list)