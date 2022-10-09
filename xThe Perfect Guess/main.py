import random

randNum = random.randint(1, 100)
print(randNum)
usrGuess= None
guesses=0

while(usrGuess != randNum):
    try:    
        usrGuess= int(input("Enter your guess: "))
        guesses +=1
        
        if (usrGuess== randNum):
                    print("Your guess was right!!!!")
        else:
            if(usrGuess>randNum):
                        print("Your guess was bigger enter a smaller guess")
            else:
                        print("Your guess was smaller enter a bigger guess")
    except Exception as e:
        print("Enter a integer not a string")   
        
print(f"You gussed the number in {guesses} guesses")

with open("C:\\Users\\Bilal Sheikh\\Desktop\\Coding Stuff\\Python\\practice\\YOUTUBE\\xThe Perfect Guess\\Hi-Score.txt") as f:
    hiscore= int(f.read())

if(guesses<hiscore):
    print("Congrats!!! You just beat the High Score")
    with open("C:\\Users\\Bilal Sheikh\\Desktop\\Coding Stuff\\Python\\practice\\YOUTUBE\\xThe Perfect Guess\\Hi-Score.txt", "w") as f:
        f.write(str(guesses))