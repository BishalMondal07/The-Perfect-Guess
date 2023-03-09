import random
number =  random.randint(1,100)
print("Guess a number between 1 to 100")
guesses = 0
guess = None

while (guess != number) :
    guess = int(input("Enter the number :"))
    guesses += 1
    if(guess>number):
        print("You guessed it wrong! Enter a smaller number")
    elif (guess<number):
        print("You guessed it wrong! Enter a larger number")
    elif(guess==number):
        print("You guessed it right!")

print("You guessed the number in", guesses ,"guesses")
with open("hiscore.txt", "r") as f:
    hiscore = int(f.read())

if(guesses<hiscore):
    print("You have just broken the high score!")
    with open("hiscore.txt", "w") as f:
        f.write(str(guesses))


