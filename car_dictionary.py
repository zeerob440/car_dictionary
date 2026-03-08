''' 1 create a function that that sets make, model and year.
    2 the function should create a dict that has the correct setting and contains the functions already created
    3 the function should return a dict so users can assign any new car they want to it.
    4 car types should be updated without affecting other cars 
'''

'''Proudly Engineered by Zachary Roberts 6 MAR 2026
    "Four Wheel and a Seat!" -Planes, Trains, and Automobiles- 1986
'''
# declarations 
greet: str = 'Welcome to car_dictionary!\n'
exit: str = 'Exiting program!\n'
def add_car():
    make: str = input('Enter car make: ')
    model: str = input('Enter car mode: ')

    while True:
        try:
            year: int = int(input('Enter year: '))
            break
        except: ValueError
        print ('Enter an integer!\n')
    
    return make, model, year


#cars is a list of dictionaries. each dictionary element in the cars list is an individual car. 
cars: list = []
print(greet)

while True:
    selection: str = input('Would you like to enter a new car? Select "y" or "n": ')
    #selection =  selection.lower()
    if selection.lower() == 'y' or selection.lower() == 'n':
        print('user input validated')
        break
    else:
         print('Enter y or n')

if selection == 'y':
    add_car()
    # append cars list here: 
else:
    print(exit)





          



#General plan for the build create a list of dictionaries, each dict in the list will be a new car, insert new cars in the dictionary

