n=18
number_of_guesses=1
print("number_of_guesses only limited to 5 times")

while(number_of_guesses<=5):
    guess_number=int(input("Enter the guess number:\n"))
    if(guess_number>18):
        print("You have entered larger number than required try smaller number")
    elif(guess_number<18):
        print("You have entered smaller number than required try larger number")
    else:
        print("You Won!..")
        print(number_of_guesses,"number of guesses you took to finish")
        break
    print(5-number_of_guesses,"number of guesses left")
    number_of_guesses=number_of_guesses+1
if(number_of_guesses>5):
    print("Game Over.. Sorry You lose")
