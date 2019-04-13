#loops the whole game
keepPlaying = True
while (keepPlaying):
    print("Welcome to create your own MadLib Story!")
    break

#user enters words
noun1 = input('Enter a noun: ')
place = input('Enter a place: ')
pronoun = input("Enter a pronoun: ")
action =  input('Enter an action: ')
noun2 = input('Enter a noun: ')
noun3 = input('Enter a noun: ')
adjective1 = input('Enter an adjective: ')
adjective2 = input('Enter an adjective: ')
emotion = input('Enter an emotion: ')
adjective3 = input("Enter an adjective: ")
adjective4 = input("Enter an adjective: ")

#entered words are put into  story
print('Once upon a time there lived a' + ' ' + noun1)
print(noun1 + ' ' + 'needed to' + ' ' + action + ' ' + 'at' + ' ' + place)
print(noun1 + ' ' + 'started on their journey')
print(noun1 + ' ' + 'brought some' + ' ' + noun2 + ' ' + 'along')
print('Then appeared a' + ' ' + noun3)
print('It was' + ' ' + adjective1 + ' ' + 'and' + ' ' + adjective2)
print(noun1 + ' ' + 'was' + ' ' + emotion)
print(pronoun + ' ' + "ran and ran and never stopped")
print(pronoun + ' ' + "ran until they fell in")
print(pronoun + ' ' + "fell into the void")
print("the void became a dark hole in which" + ' ' + pronoun + ' ' + "landed in a" + ' ' + adjective3 + ' ' + "place")
print("This place was unlike their home")
print("A" + ' ' + adjective4 + ' ' + "that all worries faded away")
print(noun1 + ' ' + "didn't know what to do, or how to get back")
print(pronoun + ' ' + "needed to find a way to get back")
print("And so" + ' ' + noun1 + ' ' + 'started to walk and walk')
print()
