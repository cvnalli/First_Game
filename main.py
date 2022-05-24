print("Welcome to my first game!")
name = input("What is your name? ")
age = int(input("What is your age? "))

#1 is equivalent to #2
# print("Hello", name, "you are", age, "years old.") #1
print("Hello " + str(name) + ", you are " + str(age) + " years old.") #2

if age >= 18:
    print("You are old enough to play.")
    wants_to_play = input("Do you want to play? ")
    if wants_to_play == 'Yes':
        print('Let\'s play!')
else:
    print("You are not old enough to play. Sorry.")