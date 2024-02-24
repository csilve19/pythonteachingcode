# [] create words after "G" following the Assignment requirements use of functions, menhods and kwyowrds
# Sample quote: "Wheresoever you go, go with all your heart" ~ Confucius (551 BC - 479 BC)

qoute = input("Enter a famous saying: ")
word = ""

for character in qoute:
    if character.isalpha():
        word += character
    else:
        if word.lower() >= "h":
            print(word.upper())
            word = ""
        else:
            word = ""
            
if word.lower() >= "h":
    print(word.upper())