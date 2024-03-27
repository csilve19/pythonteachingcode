# [] create Element_Quiz

#import the file into the Jupyter Notebook environment
import os
os.system("curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/elements1_20.txt -o elements1_20.txt")

#opening and reading and setting 'curser'
elements = open("elements1_20.txt", "r")
elements.seek(0)
elem_str = elements.readlines()

#element_list
elem_list = []

#open the file with the first 20 elements
for line in elem_str:
    elem_list += line.lower().strip().split(',') #read one line at a time to get element names, remove any whitespace (spaces, newlines) and save each element name, as lowercase, into a list
    if len(elem_list) >= 20:
        break
        
#Intro to quiz and requird name placement
print("\nWelcome Cameron Silvera-Robinson list any 5 of the first 20 elements in the Period table")

#get_names funciton for the user to guess five times with no empty or repeat guesses and returning list 
elem_guess =[]   
def get_names():
    counter = 0 
    while counter < 5:
        guess = input("Enter the name of an element: ")
        guess = guess.lower()
        if guess in elem_guess:
            print(guess.title(),"was already entered\t <--no duplicates allowed")
            pass
        elif guess == "":
            print("Empty guesses are not allowed, try again.")
            pass
        else:
            elem_guess.append(guess)
            counter += 1
    return elem_guess
    
    
#element quiz    
def element_quiz(elem_guess):
    correct_guesses = []
    incorrect_guesses = []
    
    for guess in elem_guess:
        if guess in elem_list:
            correct_guesses.append(guess)
        else:
            incorrect_guesses.append(guess)
    
    # print output

    correct_percentage = len(correct_guesses) / len(elem_guess) * 100
    
    print("\n")
    print(correct_percentage, "% correct!")
    print("Found: ", correct_guesses)
    print("Not Found: ", incorrect_guesses)


#calling functions 
elem_guess = get_names()
element_quiz(elem_guess)