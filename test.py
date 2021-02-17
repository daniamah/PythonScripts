############################################################################################################
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              To display user a menu of options to choose from. Their choices are
#              Reading a file, writing to a file, removing from file,
#              saving to file and lastly exit the program.
#
# ChangeLog (Who,When,What)
#           DaniaM,02.14.2021,Started writing script, defined menu and executed read, write and exit options
#           DaniaM,02.15.2021,Executed the save and remove
#############################################################################################################

# Declare variables
dicRow = {}     # Dictionary definition
strTaskRm = ""  # Enter to be removed
strUsrOpt = ""  # To store option from the menu picked by user
lstRow = []     # List of items in a row from file
lst = []        # List of task and priorities
strMenu = "Menu of Options" "\n" "1) Display current data" "\n" "2) Add Data to List" "\n" "3) Remove an item" "\n" "4) " \
          "Save data to file" "\n" "5) Exit Program "

# Copy content of file to a List
objFile = open("ToDo.txt", "r")
for row in objFile:
    lstRow = row.split(",")
    dicRow = {"Task": lstRow[0], "Priority": lstRow[1]}
    lst.append(dicRow)
objFile.close()

# Execute script depending on user input
while (True):
 print(strMenu)
 strUsrOpt = int(input("Which option would you like to perform? [1 to 5] "))
 if strUsrOpt == 1:
     for row in lst:
         print(row["Task"] + "," + row["Priority"])

 elif strUsrOpt == 2:
     strTask = input("Enter the task: ")
     strPri = input("Enter task priority: ")
     lstRow = {"Task": strTask, "Priority": strPri}
     lst.append(lstRow)


 elif strUsrOpt == 3:
     strTaskRm = str(input("Enter task name you want to remove? "))
     lst_len = len(lst)

     i = 0
     found = False
     while (i < lst_len):
         if strTaskRm in lst[i].values():
             del lst[i]
             print(strTaskRm + " has been removed!")
             found = True
             break
         i = i + 1

     if found == False:
        print("Task not found!")

 elif strUsrOpt == 4:
     objFile = open("ToDo.txt", "w")
     for dicRow in lst:
         objFile.write(dicRow["Task"] + "," + dicRow["Priority"] + "\n")
     objFile.close()
     print("Your data has been saved!")

 elif strUsrOpt == 5:
     exit()