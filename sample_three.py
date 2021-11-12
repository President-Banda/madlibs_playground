print("Welcome to Mad Lib Generator")


def main():
    # Getting user input
    noun = str(input("Please enter a noun: "))
    action = str(input("Please enter a action: "))
    colour = str(input("Please enter a colour: "))

    # Printing all the sentences
    print(noun, "was eating ice cream")
    print("While", action, "in the ocean")
    print("Which was", colour, "in colour")
    print("How is that true?")

    # Restart Function
    restart()


# Restart Function
def restart():
    replay = str(input("Would you like to replay the game? (y/n): "))  # Getting user input
    if replay == "y":  # Check if the input is equal to "y"
        main()  # If it is than run main() again
    elif replay == "n":  # Else if the input is "n"
        print("Goodbye!!")  # Print a goodbye message
        quit()  # Quit the programme
    else:  # Else if the input is not y or n then
        print("Please enter a correct input!!")  # Print a statement to the user
        restart()  # Repeat the Function


# Main game Loop
while True:
    main()