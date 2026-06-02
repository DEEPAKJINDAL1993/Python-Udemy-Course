try:
    height = float(input("Enter your height in m: "))
    weight = float(input("Enter your weight in kg: "))

    if height > 3:
        raise ValueError("Height should not be greater than 3m")
    if height < 0:
        raise ValueError("Height is negative")
    if weight > 500:
        raise ValueError("Weight should not be greater than 500kg")
    if weight < 0:
        raise ValueError("Weight is negative")

except ValueError as err:
    print(f"Please enter a valid number. {err}")

else:
    bmi = weight / (height * height)
    print(f"Your BMI is {bmi:.2f}")
