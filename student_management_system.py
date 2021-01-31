import os
import platform

global list_std  # Making list_std as super global variable
list_std = ["siddya", "ventya", "karnya"]  # List of student


def management_std():
    """
         Function for student management system
    """
    global bye  # Making bye as super global variable
    bye = "bye..............."
    print("""
    Enter 1 : To view student's list
    Enter 2 : To add new student
    Enter 3 : To search student
    Enter 4 : To remove student
    Enter 5 : To exit
    """)

    try:  # Using exception for validation
        user_input = int(input("Please select an above option : "))  # Will take input from user
    except ValueError:
        print("\n Hy! that's not a number")  # Error message

    else:
        print("")

    # Checking using option
    if user_input == 1:
        print("List students \n")
        for students in list_std:
            print("=> {}".format(students))

    elif user_input == 2:
        new_std = input("Enter new student : ")
        if new_std in list_std:
            print("\n this student {} already in the database")

        else:
            list_std.append(new_std)
            print("\n => {} successfully add \n".format(new_std))
            for students in list_std:
                print("=> {}".format(students))

    elif user_input == 3:
        src_std = input("Enter student name to search : ")
        if src_std in list_std:
            print("\n => record found of student {}".format(src_std))

        else:
            print("\n => no record foundof student {}".format(src_std))

    elif user_input == 4:
        rem_std = input("Enter student name to remove : ")
        if rem_std in list_std:
            list_std.remove(rem_std)
            print("\n => student {} successfully delete \n".format(rem_std))
            for students in list_std:
                print("\n no recored found of this students {}".format(rem_std))

    elif user_input == 5:
        exit_ops = input("\n Are you sure (y/n) : ")
        if exit_ops == "y":
            exit()
        else:
            management_std()

    elif user_input < 1 or user_input > 5:
        print("Please enter valid option")


management_std()


def run_again():

    run_agn = input("\n Do you want to run again y/n : ")
    if run_agn.lower() == 'y':
        if platform.system() == "Windows":
            print(os.system('cls'))
        else:
            print(os.system('clear'))
        management_std()
        run_again()

    elif run_agn.lower() == "n":
        quit()

    else:
        print("\n Please choose the correct alphabet....")
        run_again()


run_again()
