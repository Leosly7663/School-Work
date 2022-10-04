
my_input = ""
while my_input != "5":
    my_input = input(
        "Please choose from the following menu:\n"
        + "1 - Display list of dogs\n"
        + "2 - Add a dog to the shelter\n"
        + "3 - Remove a dog from the shelter\n"
        + "4 - Display the operating cost of the shelter\n"
        + "5 - Exit the program\n")
    if my_input == "1":
        # Display the list of dogs
    elif my_input == "2":
        # Add a dog object
    elif my_input == "3":
        # Remove a dog object
    elif my_input == "4":
        # Display the operating cost
    elif my_input == "5":
        # Display "Goodbye"
    else:
        # Display invalid input