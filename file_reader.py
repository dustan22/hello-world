#the keyword "with" closes the file once it is no longer needed.  The file's contents are only available within the "with" block
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())

with open('pi_digits.txt') as file_object:
    for line in file_object:
        print(line.rstrip())

#To access file contents outside the "with" block, one can store them in a list
with open('pi_digits.txt') as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print("pi-string = " + pi_string)
print("Length of pi_string is " + str(len(pi_string)))

#This part searches the first million digits of pi for a string of numbers
filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

birthday = input("Enter your birthday in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")

#Writing to a file
filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.")
    
