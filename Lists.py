cars = ['Lexus', 'Tesla', 'Ferrari', 'Porsche']
print(cars)
print(cars[0])
cars.append('BMW')
print(cars)
del(cars[2])
print(cars)
popped_car = cars.pop()
print(cars)
print("Popped_car = " + popped_car)
cars.append('Lexus')
print(cars)
cars.remove('Lexus') #Note remove only removes the first instance in a list
print(cars)
cars.sort()
print("Sorted list = " + str(cars))
print("Last value in list is " + cars[-1])
print("Last two values in list are " + str(cars[-2:]))
for car in cars[:2]:
    print(car)

for car in cars:
    print(car)

for value in range(1,5):
    print(value)

numbers = list(range(1,5))
print("numbers = " + str(numbers))

print("Here's an example of a list comprehension:")
squares = [value**2 for value in range(1,11)]
print(squares)

#How to copy a list
cars2 = cars[:]
print(cars2)

#a tuple is a list of constants.  Use parentheses.
tuple1 = (1,2,3,400)
print(tuple1[2])

#Python has a style guide called PEP 8

# Checking for a value in a list
print(cars)
print("Audi in cars? " + str('Audi' in cars))
print("Porsche in cars? " + str('Tesla' in cars))
print("Audi not in cars? " + str('Audi' not in cars))

#how to check if a list if empty
empty_list = []
if empty_list:
    print("list is not empty")
else:
    print("list is empty")


