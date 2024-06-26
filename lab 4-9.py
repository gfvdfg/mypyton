def bmi(w,h) :
    cal = weigth/(heigth/100)**2
    return cal
weigth = float (input("น้ำหนัก: ") )
heigth = int (input("ส่วนสูง: "))
print ("BMI %.2f" % bmi (weigth,heigth))
    
    
if bmi(weigth,heigth) < 18.49:
    print ("น้ำหนักน้อย/ผอม")
elif bmi(weigth,heigth) < 18.5 and bmi(weigth,heigth) <= 22.9:
    print ("ปกติ/สุขภาพดี")
elif bmi(weigth,heigth) < 23 and bmi(weigth,heigth)   <= 24.9:
    print ("อ้วน/โรคอ้วน1" )
elif bmi(weigth,heigth) < 25 and bmi (weigth,heigth)  <= 29.90:
    print ("อ้วน/โรคอ้วน2")
else:
    print("อ้วน/โรคอ้วน3")