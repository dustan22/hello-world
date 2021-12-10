
#default gender is boy, lastname is optional argument
def greet_user(firstname, gender='boy', lastname=''):  
    #This is a docstring for auto documentation.  Uses triple quotes
    """Display a simple greeting"""   
    if lastname:
        print('Hello, ' + firstname + ' ' + lastname + ' ' + gender + '!')
    else:
        print('Hello, ' + firstname + ' ' + gender + '!')
#Call function using positional arguments
greet_user('Elliott', 'boy')


#Now call the function with keyword arguments so that order 
#doesn't matter in the function call
greet_user(gender='boy', firstname='Holden')

greet_user(firstname='Elliott')
greet_user('Watson','dog','Skidmore')


#another example
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

#simulate printing each design, until none are left.
#Move each design to completed_models after printing.
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print("Printing model: " + current_design)
    completed_models.append(current_design)

#To send a coopy of a list to a function use [:] after the list name when
# #passing the list.  This will leave the original list unmodified.


#Passing an abritrary number of arguments:
def make_pizza(*toppings):
    """Print the list of toppings that have been requested"""
    print(toppings)
    for topping in toppings:
        print("Topping: " + topping)

make_pizza('mushrooms', 'anchovies', 'pickles')


#Here's an exmaple to accept as many name-value pairs as you like
def build_profile(first, last, **user_info): #The double asterisks creates an empty dictionary
    profile = {}  #Make an empty dictionary
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key]=value
    return profile

user_profile = build_profile('Neils', 'Bohr',
                            location='Copenhagen',
                            field='physics')
print(user_profile)


