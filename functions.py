#dictionary of students
students = []

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

#start the loop here
quit_loop = True

while quit_loop:
    student_list = get_students_titlecase()

    student_name = input("Enter Student Name: ")
    student_id = int(input("And their ID: "))
    add_student(student_name, student_id)

    if input("Do you want to add more students? ").upper() != "Y":
        quit_loop = False
    pass

print_students_titlecase()