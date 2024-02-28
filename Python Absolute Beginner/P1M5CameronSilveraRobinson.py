## [ ] create, call and test the adding_report() function

def adding_report(report):
    total = 0
    items = ""
    print("Input an integer to add to the total or \"Q\" to quit\n")
    while True:
        if report.upper() == "T":
            user_input = input('Enter an integer or "Q"): ')
            if user_input.isdigit():
                total = int(user_input) + total
            elif user_input.upper().startswith("Q"):
                print("\nTotal\n",total,"\n Calculated by: Cameron Silvera-Robinson")
                break
            else: 
                print("\"" + user_input + "\"" + " is an invalid input")
        elif report.upper() == "A":
            user_input = input('Enter an integer or "Q": ')
            if user_input.isdigit():
                total = int(user_input) + total
                items += user_input + "\n" 
            elif user_input.upper().startswith("Q"):
                print("\nTotal\n",total,"\n Calculated by: Cameron Silvera-Robinson")
                break
            else:
                print("\"" + user_input + "\"" + " is an invalid input")

adding_report("a")
            