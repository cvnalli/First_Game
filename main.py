print("Welcome to my first game!")
name = input("What is your name? ")
age = int(input("What is your age? "))

#1 is equivalent to #2
# print("Hello", name, "you are", age, "years old.") #1
print("Hello " + str(name) + ", you are " + str(age) + " years old.") #2

#Character Stats
health = 10

if age >= 18:
    print("You are old enough to play.")
    wants_to_play = input("Do you want to play (yes/no)?")
    if wants_to_play.lower() == 'yes':
            print("You are staring with " + str(health) + " health. Let\'s play!")
#Make decision left or right?
            left_or_right = input("First choice... Left or Right (left/right)? ")
            if left_or_right == "left": #left choice done
                ans = input("You followed the path and reached the lake. Do you swim across or go around? (across/around)? ")
                if ans == 'around':
                    print("You went around and reached the other side of the lake.")
                elif ans == 'across':
                    print("You managed to get across, but you were attacked by a croc. You lost 5 health.")
                    health -= 5
                    print("You now have " + str(health) + " health.")
                ans = input("You notice a house and a river. Which do you go to? (river/house) ")
                if ans == "house":
                    print("You enter the house and were attacked by a thug! You lost 5 health")
                    health -= 5   
                    if health <= 0:
                        print("You now have zero health. You lose...")
                    else:
                        print("You survived the fight. You win!")
                else:
                    print("You slipped and fell in the river. You died...")              
            else:
                print("You are impaled by spikes.")
else:
    print("You are not old enough to play. Sorry.")