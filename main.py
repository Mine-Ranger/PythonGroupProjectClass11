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

#######################################################################################################################################################


def create_and_print_student_marksheet():
    subjects = ["English", "Computer Science", "Physics",
                "Chemistry", "Mathematics", "Physical Education"]
    no_of_subjects = len(subjects)

    marksheet = {}

    name = input("Enter Student's Name  ")  # Getting Name

    # Getting Marks of all subjects
    for s in subjects:
        usr_input = ''
        while not usr_input.replace('.', '', 1).isdigit():
            usr_input = input("Enter the marks of "+s+"  ")
            if not usr_input.replace('.', '', 1).isdigit():
                print("Please enter a number only")
        marksheet[s] = float(usr_input)

    # Calculating Sum
    sum = 0
    for m in marksheet:
        sum += marksheet[m]

    marksheet["Sum"] = sum
    marksheet["Percentage"] = str(sum/(no_of_subjects*100))+'%'

    # Printing marksheet
    print()
    print("Name: "+name)
    for m in marksheet:
        print(m+':', marksheet[m])

#######################################################################################################################################################


def do_abbreviation_of_3_words():
    words = []
    while len(words) != 3:
        print("Please enter only 3 words")
        words = input()
        words = words.split()
    for w in words:
        print(w[0], end=" ")
    print()

#######################################################################################################################################################


def get_list_from_user():
    l = []
    n = int(input("Enter number of elements : "))
    for i in range(0, n):
        l.append(input("Enter element no"+str(i)+'\t'))
    return l


def append_an_element(List):
    List.append(input("Enter element you want to append"))
    if List[-1].isnumeric():
        List[-1] = int(List[-1])
    elif List[-1].replace('.', ' ', 1, inplace=False).isdigit():
        List[-1] = float(List[-1])


def append_list(List):
    List.append(get_list_from_user())


def insert_element(List):
    pos = int(input("On which position you want to insert the elemnt? "))
    ele = input("Enter the element you want to insert")
    List.insert(pos, ele)


def modify_element(List):
    pos = int(input("Enter the position of the element you want to modify"))
    value = input("Enter the new value you want to replace the current one")
    List[pos] = value


def delete_element(List: list):
    value = 0
    usr_input = input("Is your value a list?(yes or no)")
    if usr_input == "yes":
        value = get_list_from_user()
    else:
        value = input("Enter the value of the element you want to delete")
    List.remove(value)


def get_list_operations_menu(List):
    print("This is your list", List)
    print()
    print(' '*10+"LIST OPERATIONS MENU")
    print("1. Append an element")
    print("2. Append a list to the list")
    print("3. Insert an element at the desired position")
    print("4, Modify an element by its position")
    print("5. Delete an element by its value")


def show_5_list_operations():
    lst = []  # creating an empty list
    lst.clear()
    lst = get_list_from_user()
    get_list_operations_menu(lst)

#######################################################################################################################################################


def show_5_dictionary_methods_and_functions():
    pass


#######################################################################################################################################################

def exit_program():
    print()
    print("Thank You for using this program")
    print("Now quiting.....")
    quit()

#######################################################################################################################################################


def do_as_in_mainmenu(option):
    if option == 1:
        create_and_print_student_marksheet()
    if option == 2:
        do_abbreviation_of_3_words()
    if option == 3:
        show_5_list_operations()
    if option == 4:
        show_5_list_operations()
    if option == 5:
        exit_program()


def select(option, menu_name):
    do_as(option, menu_name)
    print()
    # Operation is completed
    if input("Type 'again' to repeat the operation or press enter to return to "+menu_name+" menu  ") == "again":
        do_as(option, menu_name)

def do_as(option, menu_name):
    if menu_name == 'main':
        do_as_in_mainmenu(option)
    if menu_name == "list operation":
        pass


def get_mainmenu():
    print(' '*10+"MAIN MENU")
    print()
    print("1. Create and print student marksheet")
    print("2. Input three words and print it in abbreviated form")
    print("3. Show any 5 list operations")
    print("4. Show 5 dictionary methods and functions")
    print("5. Exit")
    select(get_user_choice(), 'main')


while True:
    get_mainmenu()
