import random

def predict_risk(data):
    risk_score = random.randint(10, 95)

    if risk_score > 70:
        status = "High Risk"
    elif risk_score > 40:
        status = "Medium Risk"
    else:
        status = "Low Risk"

    return risk_score, status