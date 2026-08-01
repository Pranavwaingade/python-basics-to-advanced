import random
import time
play_again="Y"
while play_again == "Y":
    print("1.Easy \n2.Medium \n3.Hard ")
    level=int(input("\nEnter Difficulty Level:-"))
    number_range=0
    if(level == 1):
        number_range=50
    elif(level == 2):
        number_range=100
    elif(level == 3):
        number_range=500
    else:
        print("Invalid Choice \nPlease Select 1, 2 or 3")
        continue
    num=random.randint(1,number_range)
    start_time=time.perf_counter()
    print(num)
    user_num=0
    attempts=0
    while user_num != num:
        user_num=int(input("Enter Your number:- "))
        attempts+=1
        if user_num > num:
            print("⬇️ Try a Smaller Number")
        elif user_num < num:
            print("⬆️ Try a Bigger Number")
        difference=abs(user_num - num)
        if difference == 0:
            break
        elif difference <= 5:
            print("🔥 Very Close!")
        elif difference <=15:
            print("😊 Close")
        elif difference <=30:
            print("😐 Not Close")
        elif difference > 30:
            print("🥶 Far Away!")


        

    end_time=time.perf_counter()
    total_time=end_time-start_time
    score=max(0, 100 - (attempts* 5))
    print('Congatulations....!🎉')
    print("Attempts :",attempts)
    print("Time     :",total_time)
    print("Score    :",score) 
    if score >= 85:
        print("Badges   :Gold 🥇")
    elif score >=65:
        print("Badges   :Silver 🥈")
    else:
        print("Badges   :Bronze 🥉")

    play_again = input("Do you want to play again (Y/N): ").upper()


