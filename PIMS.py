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
def name_verify():
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
            return driver
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
def search_records():
    print('driver', 'licence', 'limit' , 'speed', 'over', 'fine')
    for record in recorded_offenses:
        print(record)
  
menu()

record_offense()
print(recorded_offenses)