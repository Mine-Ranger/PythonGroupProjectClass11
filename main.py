def print_student_marksheet():
    pass


def do_abbreviation_of_3_words():
    words = []
    while len(words) != 3:
        print("Please enter only 3 words")
        words = input()
        words = words.split()
    for w in words:
        print(w[0], end=" ")
    print()


def show_5_list_operations():
    pass


def show_5_dictionary_methods_and_functions():
    pass


def exit_program():
    print()
    print("Thank You for using this program")
    print("Now quiting.....")
    quit()


def get_user_choice():
    selected_option = 0
    while True:
        print()
        usr_input = input("Enter your choice (1-5): ")
        if usr_input.isnumeric():
            selected_option = int(usr_input)
            if selected_option < 1 or selected_option > 5:
                print("Please choose a number between 1 and 5")
            else:
                return selected_option
        else:
            print("Please Enter a number only")


def do_as_in_option(choice):
    if choice == 1:
        print_student_marksheet()
    if choice == 2:
        do_abbreviation_of_3_words()
    if choice == 3:
        show_5_list_operations()
    if choice == 4:
        show_5_list_operations()
    if choice == 5:
        exit_program()


def select(choice):
    do_as_in_option(choice)
    print()
    # Operation is completed
    if input("Type 'again' to repeat the operation or press enter to go to main menu  ") == "again":
        do_as_in_option(choice)


def get_mainmenu():
    print(' '*10+"MAIN MENU")
    print()
    print("1. Create and print student marksheet")
    print("2. Input three words and print it in abbreviated form")
    print("3. Show any 5 list operations")
    print("4. To show 5 dictionary methods and functions")
    print("5. Exit")
    select(get_user_choice())


while True:
    get_mainmenu()
