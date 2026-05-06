def calculate_bmi(height,weight):
    print("Height =" + str(height))
    print("Weight =" + str(weight))

    bmi = weight//(height * height)
    print(bmi)
    if bmi > 25.0:
        return 1
    elif bmi <= 25.0 and bmi >= 18.5:
        return 0
    else:
        return -1


print(calculate_bmi(1.73,60))
