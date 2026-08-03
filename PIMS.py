recorded_offenses = {}
def menu():
    print('''
    Police Patrol System
       1. Record a speeding offense
       2. View all recorded offenses
       3. Search offence records
       4. Display patrol summary
       5. Exit Program
    ''')   
def record_offense():
    valid = False
    while valid == False:
        driver = input("Diver Full Name: ").strip()
        names = [name for name in driver.split() if name]
        if driver == "":
            print("Do not leave blank")
        elif not driver.replace(" ", "").isalpha():
            print("Only letters and spaces please")
        elif len(names) != 2:
            print("Two names please")
        else:
            valid = True
    



print(recorded_offenses)


menu()
record_offense()