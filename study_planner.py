def calculate_remaining(target, completed, days) :
    if target < 0 or completed < 0 :
        print("Enter only nonnegative values")
        return 0
    if completed >= target :
        print("Congrats you made completed your goal!!!")
        return 0
    if days < 0 :
        print("you are out of days to study.")
        return 0
    remaining = target - completed 
    dailyHours = remaining/days
    print(f"You have {remaining:.2f} hours left to study")
    print(f"Study {dailyHours:.2f} per day to reach your target")
    return remaining 

target = float(input("Enter how many hours you want to study for this week."))
completed = float(input("How many hours have you already completed?"))
days = int(input("How many days do you have left to meet your deadline?"))

calculate_remaining(target, completed, days) 
