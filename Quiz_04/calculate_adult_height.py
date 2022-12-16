def calculate_height(gender, mother_height, father_height):
    if gender == "boy":
        return (father_height + mother_height) / 2 + 6.5
    if gender == "girl":
        return (father_height + mother_height) / 2 - 6.5

print("----------------------------------------")
print("Calculate the adult height: ")
print("- boy")
print("- girl")
print("----------------------------------------")

gender_choice = input("Enter your choice: ")

if gender_choice == "boy":
    father_height = float(input("Enter the father's height(cm): "))
    mother_height = float(input("Enter the mother's height(cm): "))
    print("Boy's adult height: ", calculate_height(gender_choice, mother_height, father_height))

if gender_choice == "girl":
    father_height = float(input("Enter the father's height(cm): "))
    mother_height = float(input("Enter the mother's height(cm): "))
    print("Girl's adult height(cm): ", calculate_height(gender_choice, mother_height, father_height))