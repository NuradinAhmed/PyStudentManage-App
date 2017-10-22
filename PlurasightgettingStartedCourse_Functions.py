students = []


def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase.append(student["name"].title())
    return students_titlecase


def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)


def add_student(name, student_id=332):
    student = {"name": name, "student_id": student_id}
    students.append(student)


def save_file(student):
    try:
        f = open("student.text", "a") #a - appending to new or existing file.
        f.write(student + "\n") #"\n" - brings down to a new line for every students name entered.
        f.close() #we close to avoid a memory leak.
    except Exception:
        print("could not save file")


def read_file():
    try:
        f = open("student.text", "r") #r - reading a text file.
        for student in f.readlines():
            add_student(student)
        f.close()
    except Exception:
        print("Could not read file")


read_file()
print_students_titlecase()

student_name = input("Enter student name: ")
student_id = input("Enter student Id: ")


add_student(student_name, student_id)
save_file(student_name)