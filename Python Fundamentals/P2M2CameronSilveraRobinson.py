song_list = ["Not Enough", "I Want You", "Beach Song"]

def list_o_matic(): 
    while song_list:
        new_song = input("Welcome, Cameron Silvera-Robinson. Here are my favorite songs" + str(song_list) + "\nEnter songs I should listen to or enter \"Quit\" to exit: ")
        if new_song.upper() == "Q":
            print("GOODBYE! Thanks for the songs!")
            break 
        elif new_song == "":
            popped_song = song_list.pop()
            print(popped_song.title(), "popped from list\n")
        elif new_song.title() in song_list:
            index_to_remove = song_list.index(new_song.title())
            del song_list[index_to_remove]
            print(new_song.title(),"has been removed from list\n")
        elif new_song.title() not in song_list:
            song_list.append(new_song.title())
            print("1 instance of",new_song.title(),"appended to list\n")
    print("That's all  folks.")


    
list_o_matic()