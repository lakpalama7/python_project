def register_student():
    print("Welcome to Student Registration System")
    name=input("Enter Student Name:")
    age=int(input("Enter student Age:"))
    country=input("Enter Student Country:")
    new_student={"name":name,"age":age,"country":country}
    return new_student

def view_all_students(STUDENT_LIST):
    if len(STUDENT_LIST)==0:
        print("No students registered yet")
    else:
        for index, student in enumerate(STUDENT_LIST, start=1):
                print(f"---------Student No: {index}------------------")
                print(f"--------1. Student Name: {student['name']}---")
                print(f"--------2. Student age: {student['age']}------")
                print(f"--------3. Country: {student['country']}--------")
                print("************************************************")