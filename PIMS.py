recorded_offenses = {}
outstanding = ['Connor Riley','Rhys Henwood','Max Homan','Niek Erkkila','Jack Lilly']
def menu():
    print('''
    Police Patrol System
       1. Record a speeding offense
       2. View all recorded offenses
       3. Search offense records
       4. Display patrol summary
       5. Exit Program
    ''')   
def name_verify(driver):
    valid = False
    while valid == False:
        names = [name for name in driver.split() if name]
        if driver == "":
            print("Do not leave blank")
        elif not driver.replace(" ", "").isalpha():
            print("Only letters and spaces please")
        elif len(names) != 2:
            print("Two names please")
        else:
            valid = True
def licence_plate_verify(plate):
    valid = False
    while valid == False:
        letter = 0
        digits = 0   
        letters = []
        for char in plate:
            if char.isdigit() == True:
                digits += 1
            elif char.isalpha() == True:
                letter += 1
            letters.append(char)
        if letters[0].isalpha() == True and letters[1].isalpha() == True: 
            if digits == 6 and letter == 2:
                valid = True
            else:
                print('Please have 6 numbers and 2 letters')      
        else:
            print('Please begin plate with two letters') 
def fine_calc():
    
def warrant_check(name, outstanding):
    if name in outstanding:
        print('This person has an outstanding Warrant Be warned')
def recorded_offenses():
    driver = name_verify(input('Name of Driver: '))
    warrant_check(driver, outstanding)
    


print(recorded_offenses)


menu()
record_offense()