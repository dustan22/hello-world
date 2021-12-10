#Dictionaries
#A dictionary is a collection of key/value pairs

alien_0 = {'color': 'green', 'points' : 5}

print(alien_0['color'])
print(alien_0['points'])

#add new key/value pairs
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_0['color'] = 'yellow'

#remove key/value pairs
del alien_0['points']
print(alien_0)

#looping through key/value pairs
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)

if 'middle' not in user_0.keys():
    print("Middle is not in user_0 keys")


from collections import OrderedDict

# An ordered dictionary maintaines entires in the order they were added.
favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")
