#Python weight converter
weight = float(input("enter your weight: "))
unit = input("enter your unit of weight kg/lb: ")

if unit == "kg":
    weight = weight * 2.205
    unit = "lbs"
    print(f"Your weight in {unit} is {weight:.3f}")
elif unit == "lb":
    weight = weight / 2.205
    unit = "kgs"
    print(f"Your weight in {unit} is {weight:.3f}")
else:
    print(f"unit {unit} is not valid!")









'''
if unit == "kg":
    result = weight * 2.205
    print(f"Tvoje váha z kg na lbs je {result}")


else:
    result = weight / 2.205
    print(f"Tvoje váha z lbs na kg je {result}")
    '''
