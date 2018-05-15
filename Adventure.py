room_list = []

# setting up the dungeon
# room = [description, north, east, south, west]
room = ["You are in the Garden of an old abandoned house.\n"
        "You remember that you used to explore these kind of "
        "houses in your childhood with your friends.\n"
        "There is a door to the south.", None, None, 2, None]
room_list.append(room)
room = ["You are in the Kitchen.\n"
        "There is a newspaper on the table. \n"
        "The headline says \"First maned mars mission successful!\" \n"
        "There is a door to the east and south.", None, 2, 4, None]
room_list.append(room)
room = ["You are in the North Hall.\n"
        "Its dark and dusty. Big spiderwebs are everywhere.\n"
        "There is a door to the north, east and west.\n"
        "The Hall continious to the south.", 0, 3, 5, 1]
room_list.append(room)
room = ["You are in the Bathroom.\n"
        "Light shines trough the window.\n"
        "On the mirror is a lipstick note saying \"20.3.34  Cape Canaveral\".\n"
        "There is a door to the west.", None, None, None, 2]
room_list.append(room)
room = ["You are in the Living Room.\n"
        "Big shelves full of books stand on the wall.\n"
        "There is a door to the north and east", 1, 5, None, None]
room_list.append(room)
room = ["You are in the South Hall.\n"
        "Looks just like the North Hall.\n"
        "There is a door to the east and west.\n"
        "The Hall continious to the north.", 2, 6, None, 4]
room_list.append(room)
room = ["You are in the Bedroom.\n"
        "An expensive looking telescope stand next to the window.\n"
        "There is a door to the west", None, None, None, 5]
room_list.append(room)


done = False

# start in the garden
current_room = 0

print("Welcome to Adventure! Press enter to start")
input("")

# main game loop
while not done:
    print()
    print(room_list[current_room][0])

    user_input = input("Where do you want to go? : ")

    # handle input
    if user_input == "s":
        next_room = room_list[current_room][3]
    elif user_input == "n":
        next_room = room_list[current_room][1]
    elif user_input == "e":
        next_room = room_list[current_room][2]
    elif user_input == "w":
        next_room = room_list[current_room][4]
    elif user_input == "exit":                  # quit game
        print("bey")
        break
    else:
        print()
        next_room = current_room
        print("options: \n"
              "To go north = n, East = e ,South = s ,West = w\n"
              "Quit game = exit")

    # set next room
    if next_room is None:
        print()
        print("You can't go that way")
    else:
        current_room = next_room


# todo: second story, inventory