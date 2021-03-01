#This function reads in a students name
#Author: John Cashman

students = []
choice = displayMenu()
while(choice != 'q'):
    if choice == 'a':
        doAdd(students)
    elif choice == 'v':
        doView(students)
    elif choice !='q':
        print("\n\nplease select either a,v or q")
    choice=displayMenu()
