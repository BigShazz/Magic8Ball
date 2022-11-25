import random
import time,sys

print('  __  __          _____ _____ _____    ___  ')
print(' |  \/  |   /\   / ____|_   _/ ____|  / _ \ ')
print(' | \  / |  /  \ | |  __  | || |      | (_) |')
print(' | |\/| | / /\ \| | |_ | | || |       > _ < ')
print(' | |  | |/ ____ \ |__| |_| || |____  | (_) |')
print(' |_|  |_/_/    \_\_____|_____\_____|  \___/ ')
print('   _______    ')
print('  /  ___  \\  ')
print(' /  / _ \\  \\')
print('|  | (_) |  | ')
print('|   > _ <   | ')
print('|  | (_) |  | ')
print(' \\  \___/  / ')
print('  \\_______/  ')

answers = ["It is certain", "It is decidedly so", "Without a doubt", "Yes, definitely",
               "You may rely on it", "As I see it, yes", "Most Likely", "Outlook Good",
               "Yes", "Signs point to yes", "Reply hazy, try again", "Ask again later",
               "Better not tell you now", "Cannot predict now", "Concentrate and ask again",
               "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very Doubtful"]

count_str = input("Hello user. How many questions would you like to ask the 8-Ball? ")

while True:
    if count_str.isdigit():
        count = int(count_str)
        break
    else:
        count_str = input("You cheeky devil, just enter a simple number this time: ")

if count <= 0:
    print("\n0!?\n")
    time.sleep(2)
    print("Well I didn't want to play with you either!\n")
    time.sleep(1)
    exit()

if count > 9000:
    time.sleep(1)
    print("\nTHATS OVER NINE THOUSAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n")
    time.sleep(2)
    print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAND\n")
    time.sleep(2)
    print("What!? Over 9000!?\n")
    time.sleep(1)
    print("There's no way that can be right!\n")
    time.sleep(1)
    exit()

if count > 1000:
    time.sleep(1)
    print("\nDid you just try and brute force me?\n")
    exit()

elif count > 10:
    print("\nYou have to be kidding me, you want to do that many questions?\nWe'll do 1 and go from there.\n", sep='')
    count = 1

def question():
    question = input("You may ask your yes or no question of the Magic 8 Ball!\n")
    print('   _______    ')
    print('  /  ___  \\  ')
    print(' /  / _ \\  \\')
    print('|  | (_) |  | ')
    print('|   > _ <   | ')
    print('|  | (_) |  | ')
    print(' \\  \___/  / ')
    print('  \\_______/  ')
    print("Thinking...")
    time.sleep(1)
    print("3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    print(random.choice(answers))

while True:
    question()
    repeat = input("Would you like to ask another question? (Y or N)")
    if not (repeat == "y" or repeat == "Y" or repeat == "yes" or repeat == "Yes"):
        print("Come back if you have more questions!")
        break