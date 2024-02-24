user_input = ""
while True: 
    user_input = input("Cameron Silvera-Robinson, enter word or integer: ")
    if  user_input != "":
        break 

def str_analysis(user_input):
        if user_input.isdigit() == True:
            user_input = int(user_input)
            if user_input > 99:
                print(user_input,"is a pretty big number")
            else:
                print(user_input,"is a smaller number than expected")
        elif user_input.isalpha() == True:
            print("\""+user_input+"\""+" is all alphabetical characters!")
        else:
            print("Multiple character types detected")
        


str_analysis(user_input)