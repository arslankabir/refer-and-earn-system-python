your_points = 2500
perc = 100
level = 1
ref_users = 0
level_perc_amount = 2500
print("\n********************THIS IS THE REFERRAL STRUCTURE FOR 1 USER********************")
print("Level 0")
print("Number of users at level 0: ",ref_users)
while True:
    no_of_ref = int(input(f"Please enter the number of referrals at level {level}: "))
    
    level_perc_amount = level_perc_amount*(perc/100)
    
    ref_users = ref_users+no_of_ref
    if perc == 100 and level == 1:
        your_points = level_perc_amount*no_of_ref
        print(f"Level {level} Points: ",your_points)
        perc = 10
        print(f"Level {level} users: ",ref_users)
        print(f"Level {level} rewards per user: ",level_perc_amount)
    elif perc == 10 and level == 2:
        your_points = your_points + (level_perc_amount*no_of_ref)
        print(f"Level {level} Points: ",your_points)
        perc = 9
        print(f"Level {level} users: ",ref_users)
        print(f"Level {level} rewards per user: ",level_perc_amount)
    elif perc == 9 and level == 3:
        your_points = your_points + (level_perc_amount*no_of_ref)
        print(f"Level {level} Points: ",your_points)
        perc = 8
        print(f"Level {level} users: ",ref_users)
        print(f"Level {level} rewards per user: ",level_perc_amount)
    elif perc == 8 and level == 4:
        your_points = your_points + (level_perc_amount*no_of_ref)
        print(f"Level {level} Points: ",your_points)
        perc = 7
        print(f"Level {level} users: ",ref_users)
        print(f"Level {level} rewards per user: ",level_perc_amount)
    elif perc == 7 and level == 5:
        your_points = your_points + (level_perc_amount*no_of_ref)
        print(f"Level {level} Points: ",your_points)
        perc = 6
        print(f"Level {level} users: ",ref_users)
        print(f"Level {level} rewards per user: ",level_perc_amount)
    elif perc == 6 and level == 6:
        your_points = your_points + (level_perc_amount*no_of_ref)
        print(f"Level {level} Points: ",your_points)
        perc = 5
        print(f"Level {level} users: ",ref_users)
        print(f"Level {level} rewards per user: ",level_perc_amount)
    elif perc == 5 and level == 7:
        your_points = your_points + (level_perc_amount*no_of_ref)
        print(f"Level {level} Points: ",your_points)
        perc = 4
        print(f"Level {level} users: ",ref_users)
        print(f"Level {level} rewards per user: ",level_perc_amount)
    elif perc == 4 and level == 8:
        your_points = your_points + (level_perc_amount*no_of_ref)
        print(f"Level {level} Points: ",your_points)
        perc = 3
        print(f"Level {level} users: ",ref_users)
        print(f"Level {level} rewards per user: ",level_perc_amount)
    elif perc == 3 and level == 9:
        your_points = your_points + (level_perc_amount*no_of_ref)
        print(f"Level {level} Points: ",your_points)
        perc = 2
        print(f"Level {level} users: ",ref_users)
        print(f"Level {level} rewards per user: ",level_perc_amount)
    elif perc == 2 and level == 10:
        your_points = your_points + (level_perc_amount*no_of_ref)
        print(f"Level {level} Points: ",your_points)
        perc = 1
        print(f"Level {level} users: ",ref_users)
        print(f"Level {level} rewards per user: ",level_perc_amount)
    elif perc == 1 and level == 11:
        your_points = your_points + (level_perc_amount*no_of_ref)
        print(f"Level {level} Points: ",your_points)
        perc = 0.1
        print(f"Level {level} users: ",ref_users)
        print(f"Level {level} rewards per user: ",level_perc_amount)
    elif perc == 0.10 and level == 12:
        your_points = your_points + (level_perc_amount*no_of_ref)
        print(f"Level {level} Points: ",your_points)
        perc = 0.01
        print(f"Level {level} users: ",ref_users)
        print(f"Level {level} rewards per user: ",level_perc_amount)
    elif perc == 0.01 and level == 13:
        your_points = your_points + (level_perc_amount*no_of_ref)
        print(f"Level {level} Points: ",your_points)
        perc = 0.01
        print(f"Level {level} users: ",ref_users)
        print(f"Level {level} rewards per user: ",level_perc_amount)
    else:
        your_points = your_points + (level_perc_amount*no_of_ref)
        print(f"Level {level} Points: ",your_points)
        perc = 0.01
        print(f"Level {level} users: ",ref_users)
        print(f"Level {level} rewards per user: ",level_perc_amount)
    level = level + 1