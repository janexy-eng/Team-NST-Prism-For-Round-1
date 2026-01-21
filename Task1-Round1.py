import random
running=True
correct_ans=random.randint(1,50)
att=0
while True:
    att+=1
    user_guess=int(input())
    if user_guess>correct_ans:
        print("That's above the target!")
    elif user_guess<correct_ans:
        print("That's below the target!")
    else:
        print(f"Correct! You guessed it in {att} attempts!")
        running=False

