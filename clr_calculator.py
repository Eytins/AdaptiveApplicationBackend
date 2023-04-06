def main():
    welcome()
    gender = sex()
    weight = get_weight()
    height = get_height()
    age = get_age()
    rest_bmr = calculate_bmr(gender, weight, height, age) 
    total_calculation(rest_bmr)

x = ""

def welcome():
    print("Welcome to your calories calculator!\nFind out How many calories should you eat daily.\n")


def sex():    
    sexes = ["male","female","M","F","f","m","Male","Female"]
    while True:
        sex = str(input("Do you identify as male or female? "))
        while sex not in sexes:
            sex = str(input("Please enter either 'male' or 'female' "))
        else:
            return sex
            break


def get_weight():
    weight_kg = float(input("Enter your weight in kilograms: "))
    while weight_kg <= 0:
        weight_kg = float(input("Invalid input. Please enter your weight in kilograms: "))
    else:
        return weight_kg


def get_height():
    height_cm = float(input("Enter your height in Centimeters: "))
    while height_cm <= 0:
        height_cm = float(input("Invalid input. Please enter your height in Centimeters: "))
    else:
        return height_cm


def get_age():
    age_yrs = int(input("Enter your age in years: "))
    while age_yrs <= 0:
        age_yrs = int(input("Invalid Input. Please enter your age in years: "))
    else:
        return age_yrs


def calculate_bmr(gender, weight, height, age):
    global maintain

    male = ["male", "M" , "m", "Male"]
    female = ["female", "F", "f", "Female"]
    bmi = weight/((height/100)*(height/100))
    global x
    global maintain
    if bmi < 18.5:
        x = ("You are underweight. You need to eat more calories to gain weight. The recommended weight that one should gain over a course of a month is suggested to be 1kg for males and 0.5kg for females. Gaining more than the recommended weight can have side effects and show signs of anxiety and over-eating and much more. Hence, you need to consume 300-500 calories more than your daily intake.")
    elif bmi >= 18.5 and bmi <= 24.9:
        x = ("You are healthy. You need to eat the same amount of calories to maintain your weight.")
    else:
        x = ("You are overweight. You need to eat less calories to lose weight. The recommended weight that one should lose over a course of a month is suggested to be 1.5kgs to 2.5kgs. Losing more than the recommended weight can mean that you are putting more pressure on your bodily functions. Hence, you need to eat 500-1000 calories less than your daily intake.")
    if gender == female:
        women = (weight * 10) + (height * 6.25) - (age * 5) - 161
        return int(women)
    else:
        men = (weight * 10) + (height * 6.25) - (age * 5) + 5
        return int(men)

maintain = 2000

def total_calculation(rest_bmr):
    user_activity_lvl = get_user_activity()    

    global maintain

    maintain = {
      "sedentary" : get_sedentary(rest_bmr), 
      "light" : get_light_activity(rest_bmr), 
      "moderate" : get_moderate_activity(rest_bmr), 
      "active" : get_very_active(rest_bmr)
      }

    if user_activity_lvl == "sedentary":
        print("You need to eat " + str(maintain["sedentary"]) + " calories a day to maintain your current weight. " + x)

    if user_activity_lvl == "light":
        print("You need to eat " + str(maintain["light"]) + " calories a day to maintain your current weight. " + x)

    if user_activity_lvl == "moderate":
        print("You need to eat " + str(maintain["moderate"]) + " calories a day to maintain your current weight. " + x)

    if user_activity_lvl == "active":
        print("You need to eat " + str(maintain["active"]) + " calories a day to maintain your current weight. " + x)
    

 
def get_user_activity():
    activity_lvl = ["sedentary", "light", "moderate", "active"]
    while True:
        user_lvl = str(input("\nWhat is your activity level?\n\nSedentary is little to no exercise.\nLightly active is light exercise/sports 1 - 3 days/week.\nModerately active is moderate exercise/sports 3 - 5 days/week.\nVery active is hard exercise every day, or 2 xs/day 6 - 7 days/week.\n\nPlease enter: 'sedentary', 'light', 'moderate',  or 'active' "))
        
        while user_lvl not in activity_lvl:
            user_lvl = str(input( "Invalid input. Please enter: 'sedentary', 'light', 'moderate',  or 'active' "))
        else:
            return user_lvl
            break


def get_sedentary(rest_bmr):
    sedentary = rest_bmr * 1.25
    return sedentary

def get_light_activity(rest_bmr):
    light = rest_bmr * 1.375
    return light

def get_moderate_activity(rest_bmr):
    moderate = rest_bmr * 1.550
    return moderate

def get_very_active(rest_bmr):
    active = rest_bmr * 1.75
    return active


if __name__ == '__main__':
    main()