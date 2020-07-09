# Guess The Number
# Rules - user have only 5 trials
# - whenever user enter a value program tells about how far from the correct number
# as close, far
# - after the trial over print "Game Over"
the_number = 45
trials = 0
print("Guess The Number Game")
print("Range[1-100] only")
while(trials < 5):
    trials += 1
    user_guess = int(input("Your best guess: "))
    match_the_guess = the_number - user_guess
    if match_the_guess < 0:
        match_the_guess *= -1
    if match_the_guess == 0:
        print("Congrats Great Prediction")
        break
    elif match_the_guess >= 1 and match_the_guess < 3:
        print("Close enough from exact number")
    elif match_the_guess > 5 and match_the_guess <= 10:
        print("Almost There")
    else:
        print("Far")
print("Number of Trials: ",trials)
if trials > 4:
    print("Game Over")