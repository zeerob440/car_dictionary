''' 1 create a function that that sets make, model and year.
    2 the function should create a dict that has the correct setting and contains the functions already created
    3 the function should return a dict so users can assign any new car they want to it.
    4 car types should be updated without affecting other cars 
'''

'''Proudly Engineered by Zachary Roberts 6 MAR 2026
    "Four Wheel and a Seat!" -Planes, Trains, and Automobiles- 1986
'''
# declarations 
greet: str = 'Welcome to car_dictionary!'
def add_car():
    pass # build later, add functions to input car values make, model and year
print(greet)

selection: str = input('Would you like to enter a new car? Select "Y" or "N": ')
# create input validation here
if selection == 'y':
    pass#build later
elif selection == 'n':
    pass# build later
else: raise ValueError('Enter "Y" to enter an new car or "N" to not enter a new car.')

'''
General plan for the build create a list of dictionaries, each dict in the list will be a new car, insert new cars in the dictionary
'''
