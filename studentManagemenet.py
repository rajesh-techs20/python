.......A students record managemenyt system .......



class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print("Name:",self.name)
        print("Marks:",self.marks)
students=[]

while True:
    print("\n__Student Management System__\n")
    print("1.Add Student")
    print("2.Show Student Details")
    print("3.Search Student")
    print("4.Topper")
    PRINT("5.Delete student")
    print("6.Exit System")

    choice=int(input("Enter the choice:"))

    if choice==1:
        n=int(input("Enter the number of students to add:"))
        for i in range(n):
            name=input("Enter name of student:")
            marks=int(input("Enter the marks of a student:"))
            s=student(name,marks)
            students.append(s)
            with open("Students.details","a") as f:
                f.write(name+" "+str(marks)+"\n")
            print("\n__Student data saved succesfully__\n")
    elif choice==2:
        if len(students)==0:
            print("Students Details Not found")
        else:
            for student in students:
                students.display()
    elif choice==3:
        search=input("Enter the name of student to search:")
        for student in students:
            if search==student.name:
                print("Student Found!")
                print("Student Marks is",student.marks)
                break
            else: 
                print("Student Not Found")
    elif choice==4:
        topper=students[0

        for student in students:
            if student.marks>topper.marks:
                topper=student
                print("Topper of the class is",student.name,"scored",student.marks)
    elif choice==5:
        delete=input("Enter the name of student to delete:")
        for student in students:
            if delete==student.name:
                students.remove(student)
                print("Student deleted successfully")
                break
    else: 
        print("Student Not found")
            
    elif choice==6:
        print("EXITING THE SYSTEM.......")
        break
    else:
        print("Invalid Options,Please try again")
        print("Invalid Choice..Please Check once and Try again")

 
