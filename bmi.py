def calculate_bmi(height,weight):
    print("Height =" + str(height))
    print("Weight =" + str(weight))

    bmi = weight//(height * height)
    print(bmi)
    if bmi > 25.0:
        return "Over weight"
    elif bmi <= 25.0 and bmi >= 18.5:
        return "Normal Weight"
    else:
        return "Under weight"


print(calculate_bmi(1.73,60))
