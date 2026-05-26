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
    print("3.Exit System")

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
        print("EXITING THE SYSTEM.......")
        break
    else:
        print("Invalid Choice..Please Check once and Try again")