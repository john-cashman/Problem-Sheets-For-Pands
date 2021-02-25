#This function prints out a list of commands for the user
#The function then returns what the user chose.
#Author: John Cashman

def displayMenu ():
    print("what would you like to do?")
    print("\t (a) Add a new student")
    print("\t (v) View Students")
    print("\t (q) Quit")
    choice = input("Type one letter a/v/q:").strip() #strip gets rid of any spaces returned by the user

    return choice
def doAdd():
    print("in adding")
def doView():
    print("in viewing")

#this is the main program

choice = displayMenu()
while(choice != 'q'):
    if choice == 'a':
        doAdd()
    elif choice == 'y':
        doView()
    elif choice !='q':
        print("\n\n please select either a,v or q")
choice=commandList()

#print("you chose {} ".format(choice))