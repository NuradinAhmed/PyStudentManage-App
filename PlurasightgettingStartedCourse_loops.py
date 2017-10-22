student_names = ["Nuradin", "Ifrah", "Amin", "Abdullahi", "Munira", "Muhidin", "Ayan"]

for names in student_names:
    if names == "Ifrah":
        continue
        print("Found her! " + names)
    elif names == "Munira":
        print("Found her! " + names)
        break
    print("Currently testing " + names)