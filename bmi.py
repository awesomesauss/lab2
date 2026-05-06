def calculate_bmi(height,weight):
    print("Height =" + str(height))
    print("Weight =" + str(weight))

    bmi = weight//(height * height)
    print(bmi)
    if bmi > 25.0:
        print("Over Weight")
        return 1
    elif bmi <= 25.0 and bmi >= 18.5:
        print("Normal Weight")
        return 0
    else:
        print("Under Weight")
        return -1


print(calculate_bmi(1.73,60))
