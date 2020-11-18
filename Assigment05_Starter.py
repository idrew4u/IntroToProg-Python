# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# ALi,Nov 17, 2020,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = ""  # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# TODO: Add Code Here
# ALi adding code to Step 1
try:
    objFile = open("ToDoList.txt", "r")
    for row in objFile:
        strData = row.split("|")
        dicRow = {"Task": strData[0], "Priority": strData[1]}
        lstTable.append(dicRow)
    objFile.close()
except:
    print()
# ALi end of changes made in Step 1

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks

    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        # TODO: Add Code Here
        # ALi adding code to Step 3
        for objRow in lstTable:
            print(objRow)
        # ALi end of changes made in Step 3
        continue

    # Step 4 - Add a new item to the list/Table
    # Asks for user input for task and priority and saves data in dictionary rows
    elif (strChoice.strip() == '2'):
        # TODO: Add Code Here
        # ALi adding code to Step 4
        newTask = input("Please enter new task: ")
        newPriority = input("Please enter it's priority: ")
        dicRow = {"Task": newTask, "Priority": newPriority}
        lstTable.append(dicRow)
        # ALi end of changes made in Step 4
        continue

    # Step 5 - Remove a new item from the list/Table
    # Asks user for input of task they want removed
    elif (strChoice.strip() == '3'):
        # TODO: Add Code Here
        # ALi adding code to Step 5
        removeTask = input("Please enter the task you wish to remove: ")
        for row in lstTable:
            if row["Task"] == removeTask:
                lstTable.remove(row)
                print(lstTable)
        # ALi end of changes made in Step 5
        continue

    # Step 6 - Save tasks to the ToDoList.txt file
    elif (strChoice.strip() == '4'):
        # TODO: Add Code Here
        # ALi adding code to Step 6
        objFile = open("ToDoList.txt", "w")
        for row in lstTable:
            objFile.write(row["Task"] + "|" + row["Priority"] + "\n")
        objFile.close()
        # ALi end of changes made in Step 6
        continue

    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        # TODO: Add Code Here
        break  # and Exit the program


