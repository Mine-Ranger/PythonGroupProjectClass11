def get_usr_choice(no_of_options):
    selected_option = 0
    while True:
        print()
        usr_input = input("Enter your choice (1-"+str(no_of_options)+"): ")
        if usr_input.isnumeric():
            selected_option = int(usr_input)
            if selected_option < 1 or selected_option > no_of_options:
                print("Please choose a number between 1 and "+str(no_of_options))
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
    List.append(input("Enter element you want to append "))


def append_list(List):
    List.append(get_list_from_user())


def insert_element(List):
    pos = int(input("On which position you want to insert the elemnt? "))
    ele = input("Enter the element you want to insert ")
    List.insert(pos, ele)


def modify_element(List):
    pos = int(input("Enter the position of the element you want to modify "))
    value = input("Enter the new value you want to replace the current one ")
    List[pos] = value
 

def delete_element(List: list):
    value = 0
    usr_input = input("Is your value a list?(yes or no) ")
    if usr_input == "yes":
        value = get_list_from_user()
    else:
        value = input("Enter the value of the element you want to delete ")
    List.remove(value)


def get_list_operations_menu(init_lst, curr_lst):
    print("\nThis the list you have given:", init_lst)
    print("This is current list:", curr_lst)
    print()
    print(' '*10+"LIST OPERATIONS MENU")
    print("1. Append an element")
    print("2. Append a list to the list")
    print("3. Insert an element at the desired position")
    print("4. Modify an element by its position")
    print("5. Delete an element by its value")
    print("6. To quit to main menu")
    do_as_in_list_operations_menu(get_usr_choice(6), init_lst, curr_lst)


def do_as_in_list_operations_menu(choice, init_lst, curr_lst):
    if choice == 1:
        append_an_element(curr_lst)
    if choice == 2:
        append_list(curr_lst)
    if choice == 3:
        insert_element(curr_lst)
    if choice == 4:
        modify_element(curr_lst)
    if choice == 5:
        delete_element(curr_lst)
    if choice == 6:
        get_mainmenu()
    # List operations ended
    if exit_prompt('list operations')=='again':
        do_as_in_list_operations_menu(choice, init_lst, curr_lst)

    get_list_operations_menu(init_lst, curr_lst)


def show_5_list_operations():
    init_lst = []  # creating an empty list
    init_lst.clear()
    init_lst = get_list_from_user()
    curr_lst = init_lst.copy()
    get_list_operations_menu(init_lst, curr_lst)

#######################################################################################################################################################
def get_dict_from_user():
    n= int(input("Enter the number of entries in the dictionary "))
    dictionary={}
    for i in range(0, n):
        key= input("Enter the key")
        value= input("Enter the value")
        dictionary[key]= value
    return dictionary


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
    do_as_in_mainmenu(option)
    print()
    # Operation is completed
    if exit_prompt(menu_name)=='agian':
        do_as_in_mainmenu(option)


def exit_prompt(menu_name):
    return input("Type 'again' to repeat the operation or press enter to return to "+menu_name+" menu  ")

def get_mainmenu():
    print(' '*10+"MAIN MENU")
    print()
    print("1. Create and print student marksheet")
    print("2. Input three words and print it in abbreviated form")
    print("3. Show any 5 list operations")
    print("4. Show 5 dictionary methods and functions")
    print("5. Exit")
    select(get_usr_choice(5), 'main')


while True:
    get_mainmenu()
