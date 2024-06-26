def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def interpret_bmi(bmi):
    if bmi < 18.5:
        return "น้ำหนักน้อยกว่าเกณฑ์"
    elif 18.5 <= bmi < 23:
        return "น้ำหนักปกติ "
    elif 23 <= bmi < 25:
        return "น้ำหนักเกิน "
    elif 25 <= bmi < 30:
        return "โรคอ้วน "
    else:
        return "โรคอ้วนอันตราย "
