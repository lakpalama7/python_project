from os import system
import module
from message import MESSAGE, MENU

STUDENT_LIST=[]

status=True

while status:
    print(MENU)
    choice=input("Enter your choice(1,2,3 [Type 'E' or 'e' to exit'])):").lower()
    if choice=='1':
        new_student=module.register_student()
        STUDENT_LIST.append(new_student)
    elif choice=='2':
        module.view_all_students(STUDENT_LIST)
    elif choice=='e':
        print(MESSAGE)
        status=False
    else:
        print("Invalid Choice! Please try again.")
        print("\n"*20)
        choice=input("Enter your choice(1,2,3 (Type 'E' or 'e' to exit')):)")

       
