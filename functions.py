#dictionary of students
students = []

#added a change here.
def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase.append(student["name"].title())
    return students_titlecase


def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)


def add_student(name, student_id):
    student = {"name": name, "student_id": student_id}
    students.append(student)


def save_file(name, sid):
    try:
        stu = {name, sid }
        f = open("students.txt", "a")
        f.write(str(stu) + "\n")
        f.close()
        pass
    except Exception:
        print("Could Not save file.")
        pass


def read_file():
    try:
        f = open("students.txt", "r")
        for student in f.readlines():
            strin = student.split(",")
            add_student(strin[0], strin[1])
        f.close()
    except Exception:
        print("Could not read file.")
        pass

#start the loop here
quit_loop = True

while quit_loop:
    read_file()
    print_students_titlecase()

    student_list = get_students_titlecase()

    student_name = input("Enter Student Name: ")
    student_id = int(input("And their ID: "))
    add_student(student_name, student_id)
    save_file(name=student_name, sid=student_id)

    if input("Do you want to add more students? ").upper() != "Y":
        quit_loop = False
    pass

