print("Willkommen zum supercoolen BMI-Rechner\n")

weight_input = input("Bitte gib dein Gewicht in kg ein:")
height_input = input("Bitte gibt deine Größe in m ein:")

weight = float(weight_input)
height = float(height_input)

bmi = weight / (height * height)

print("Dein BMI ist " + str(bmi))