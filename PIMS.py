#PIMS CODE SYSTEM
#Create the dictionary used for the rest of the code
recorded_offenses = {}
#Outstanding warrents used for detection
outstanding = ['Connor Riley','Rhys Henwood','Max Homan','Niek Erkkila','Jack Lilly']
def menu():
    #Prints the main Menu
    print('=' * 35)
    print('''Police Patrol System
       1. Record a speeding offense
       2. View all recorded offenses
       3. Search offense records
       4. Display patrol summary
       5. Exit Program''')   
    print('=' * 35)

def name_verify():
    #Verifys the names of anyone put into the system
    valid = False
    while valid == False:
        #asks for driver name
        driver = input('Name of Driver: ')
        #splits the name into a list
        names = [name for name in driver.split() if name]
        if driver == "":
            #checks the name isn't blank
            print("Do not leave blank")
        elif not driver.replace(" ", "").isalpha():
            #checks the name is only letters
            print("Only letters and spaces please")
        elif len(names) != 2:
            #checks if it has a first and last name
            print("Two names please")
        else:
            #returns the drivers name as a title and stripped of any unwanted spaces
            return driver.lower().title().strip()
def licence_plate_verify():
    #verifys licence plate number
    valid = False
    while valid == False:
        #asks for plate
        plate = input('Plate of Car: ')
        letter = 0
        digits = 0   
        letters = []
        #creates a list of letters and numbers and counts the number of letters and numbers
        for char in plate:
            if char.isdigit() == True:
                #adds one for each digit
                digits += 1
            elif char.isalpha() == True:
                #adds one for each letter
                letter += 1
            #adds charector to the list
            letters.append(char)
            #if the first two charectors are letters 
        if letters[0].isalpha() == True and letters[1].isalpha() == True: 
            #if there are 6 numbers and 2 letters
            if digits == 6 and letter == 2:
                #returns verified plate
                return plate.upper()
            else:
                print('Please have 6 numbers and 2 letters')
        else:
            print('Please begin plate with two letters') 
def speeds():
    valid = False
    while valid == False:
    #finds the limit and verifys it
        try:
            limit = int(input('Area Limit: '))
            #checks that the limit is between 30 and 110
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
            #checks that the car speed is over the limit
            if speed > limit:
                valid = True
            else:
                print('Not over Limit')
        except ValueError:
            print('NOT A NUMBER') 
    #finds differance in speed
    differance = speed - limit
    return differance, limit, speed
def fine_calculator(over):
    #calculates fine 
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
    #after its all done returns the fine
    return fine    
def record_offense():
    #records an offense
    #calls the name verify function
    driver = name_verify()
    #checks the persons name against the outstanding warrents
    if driver in outstanding:
        print('This person has an outstanding Warrant Be warned')
    #calls the plate verify function
    plate = licence_plate_verify()
    differance, limit, speed = speeds()
    #calls fine calculator using differance
    fine = fine_calculator(differance)
    #records the offense
    recorded_offenses[driver] = [plate, speed, limit, differance, fine]
def view_records():
    #view all records
    #only works if recorded offenses are more than zero
    if len(recorded_offenses) != 0:
        #prints key
        print('=' * 55)
        print('driver         licence    limit  speed   over   fine')
        print('=' * 55)
        #for each recorded offense
        for record in recorded_offenses:
            # prints the name
            print(record, end=('   '))
            for details in recorded_offenses[record]:
                #prints the details of the offender
                print(details, end=('     '))
        print()
    else:
        print('No offenses recorded')
    print()
def search_records():
    #search for a specific record
    #only works if recorded offenses are more than zero
    if len(recorded_offenses) != 0:
        #calls name verify function
        valid = False
        while valid == False:
            choice = input('Would you like to search for plate or name? ').lower()
            if choice == 'name':
                name = name_verify()
                if name in recorded_offenses:
                    #if the name is in the record
                    #prints the name
                    print(name, end=('   '))
                    for details in recorded_offenses[name]:
                        #prints the details 
                        print(details, end=('     '))       
                else:
                    print('Not in database')
                    valid = True
            elif choice == 'plate':
                plate = licence_plate_verify()
                # find all names whose details list contains the plate
                matching_keys = [key for key, values in recorded_offenses.items() if plate in values]
                if matching_keys:
                    for name in matching_keys:
                        print(name, end='   ')
                        for details in recorded_offenses[name]:
                            print(details, end='     ')
                else:
                    print('Not in database')
                valid = True  # exit loop after search

            else:
                print('NOT VALID OPTION')
    else:
        print('No offenses recorded')
        valid = True    
    print()
def patrol_summary():
    #gives a summary of the patrol
    highest = 0
    total_speed = 0
    total_fine = 0 
    #shows total offenses recorded
    print(f'Total Offenses:   {len(recorded_offenses)}')
    #for every offense in the record
    for record in recorded_offenses:
        fine_str = recorded_offenses[record][4]
        #finds the fine they were given
        fine = int(fine_str.replace("$", ""))
        #turns the fine into an interger
        total_fine += fine
        #adds fine to total fine
        speed = recorded_offenses[record][3]
        #finds speed of offender
        if speed > highest:
            #finds the highest offender and speed they were traveling
            highest_offense = record
            highest = speed
        #adds speed to total speed
        total_speed += speed
    #prints the total of all the fines
    print(f'Total fines issued:   ${total_fine}')
    #prints out average of the speed over limit
    print(f'Average Speed Over Limit:   {total_speed/len(recorded_offenses)}')
    #prints the highest speed over limit and their name
    print(f'Highest offence:   {highest_offense} ({highest} km/h over)')
#sets exit to false
exit = False
#welcomes the user
print('Welcome to PIMS')
#while the users doesn't want to enter
while exit == False:
    menu()
    #makes the user select where they want to go
    select = input('Please put the number of where you would like to go: ')
    if select == '1':
        #calls record offense function
        record_offense()
    elif select == '2':
        #calls view records function
        view_records()
    elif select == '3':
        #calls search records function
        search_records()
    elif select == '4':
        #calls patrol summary
        patrol_summary()
    elif select == '5':
        #exits the code
        print('Thank you for using PIMS')
        exit = True
    else:
        #doesn't let the user enter wrong answer
        print('INVALID ANSWER TRY AGAIN')
        