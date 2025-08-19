import random
random_num=random.randint(1,10)
while(True):
    guess=int(input("enter any number from 1 to 10 :"))
    if(guess>10):
        print("⚠️ You entered out of range! Please enter between 1 and 10.")
        continue
    else:
        if(guess==random_num):
            print("🎉 Correct! You guessed the number.")
            break
        else:
            print("❌ Wrong! The random number was:", random_num)
    

