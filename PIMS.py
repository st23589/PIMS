#PIMS CODE SYSTEM
#Create the dictionary used for the rest of the code
recorded_offenses = {}
#Outstanding warrents used for detection
outstanding = ['Connor Riley','Rhys Henwood','Max Homan','Niek Erkkila','Jack Lilly']
def menu():
    #Prints the main Menu
    print('''
    Police Patrol System
       1. Record a speeding offense
       2. View all recorded offenses
       3. Search offense records
       4. Display patrol summary
       5. Exit Program
    ''')   

def name_verify():
    #Verifys the names of 
    valid = False
    while valid == False:
        driver = input('Name of Driver: ')
        names = [name for name in driver.split() if name]
        if driver == "":
            print("Do not leave blank")
        elif not driver.replace(" ", "").isalpha():
            print("Only letters and spaces please")
        elif len(names) != 2:
            print("Two names please")
        else:
            valid = True
            return driver.lower().title().strip()
def licence_plate_verify():
    valid = False
    while valid == False:
        plate = input('Plate of Car: ')
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
                return plate
            else:
                print('Please have 6 numbers and 2 letters')
        else:
            print('Please begin plate with two letters') 

def fine_calculator(over):
    if over >= 1 and over <= 10:
        fine = '$30'
    elif over <= 20:
        fine = '$80'
    elif over <= 30:
        fine = '$170'
    elif over <= 40:
        fine = '$400'
    else:
        fine = '$630'
    return fine
def warrant_check(name, outstanding):
    if name in outstanding:
        print('This person has an outstanding Warrant Be warned')
def record_offense():
    driver = name_verify()
    warrant_check(driver, outstanding)
    plate = licence_plate_verify()
    valid = False
    while valid == False:
        try:
            limit = int(input('Area Limit: '))
            if limit <= 110 and limit >= 30:
                valid = True
            else:
                print('Not a valid Limit')
        except ValueError:
            print('NOT A NUMBER')
            valid = False
    valid = False
    while valid == False:
        try:
            speed = int(input('Car Speed: '))
            if speed > limit:
                valid = True
            else:
                print('Not over Limit')
        except ValueError:
            print('NOT A NUMBER')    
    differance = speed - limit    
    fine = fine_calculator(differance)
    recorded_offenses[driver] = [plate, speed, limit, differance, fine]
def view_records():
    if len(recorded_offenses) != 0:
        print('driver   licence    limit  speed   over   fine')
        for record in recorded_offenses:
            print(record, end=('   '))
            for details in recorded_offenses[record]:
                print(details, end=('     '))
    else:
        print('No offenses recorded')
    print()
def search_records():
    if len(recorded_offenses) != 0:
        name = name_verify()
        if name in recorded_offenses:
            print(name, end=('   '))
            for details in recorded_offenses[name.lower().title()]:
                print(details, end=('     '))        
            else:
                print('Not in database')
    else:
        print('No offenses recorded')
    print()
def patrol_summary():
    highest = 0
    total_speed = 0
    total_fine = 0 
    print(f'Total Offenses:   {len(recorded_offenses)}')
    for record in recorded_offenses:
        fine_str = recorded_offenses[record][4]
        fine = int(fine_str.replace("$", ""))
        total_fine += fine
        speed = recorded_offenses[record][3]
        if speed > highest:
            highest_offense = record
            highest = speed
        total_speed += speed
    print(f'Total fines issued:   ${total_fine}')
    print(f'Average Speed Over Limit:   {total_speed/len(recorded_offenses)}')
    print(f'Highest offence:   {highest_offense} ({highest} km/h over)')

exit = False
print('Welcome to PIMS')
while exit == False:
    menu()
    select = input('Please put the number of where you would like to go: ')
    if select == '1':
        record_offense()
    elif select == '2':
        view_records()
    elif select == '3':
        search_records()
    elif select == '4':
        patrol_summary()
    elif select == '5':
        print('Thank you for using PIMS')
        exit = True
    else:
        print('INVALID ANSWER TRY AGAIN')
        