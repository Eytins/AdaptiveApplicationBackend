def calculate_bmr(gender, weight, height, age):
    bmi = weight / ((height / 100) * (height / 100))
    if bmi < 18.5:
        margin = +500
    elif 18.5 <= bmi <= 24.9:
        margin = 0
    else:
        margin = -800
    if gender == "f":
        women = (weight * 10) + (height * 6.25) - (age * 5) - 161
        return int(women)
    else:
        men = (weight * 10) + (height * 6.25) - (age * 5) + 5
        return int(men), margin


def total_calculation(rest_bmr, user_activity_lvl: int):
    # global maintain
    maintain = [
        get_sedentary(rest_bmr),
        get_light_activity(rest_bmr),
        get_moderate_activity(rest_bmr),
        get_very_active(rest_bmr)
    ]
    return maintain[user_activity_lvl]


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
