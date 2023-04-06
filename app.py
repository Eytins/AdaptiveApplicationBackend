from flask import Flask, request
import clr_calculator as clr

app = Flask(__name__)


# python -m flask --app app run
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


# request body:
# {
#     "gender": "m",  // "m" represents male, "f" represents female
#     "height": 180,
#     "weight": 60,
#     "age": 24,
#     "activity": 0  // 0,1,2,3 represent 'sedentary', 'light', 'moderate', 'active'
# }
@app.route("/get_recommend_calories", methods=['POST'])
def get_recommend_calories():
    if request.method == "POST":
        req = request.get_json()
        g = req['gender']
        w = req['weight']
        h = req['height']
        a = req['age']
        activity = req['activity']
        rest_bmr, margin = clr.calculate_bmr(g, w, h, a)
        cur = clr.total_calculation(rest_bmr, activity)
        return {
            "current_clr": cur,
            "recommended_clr": cur + margin,
            "margin": margin,
        }
    else:
        return "Wrong request!"
