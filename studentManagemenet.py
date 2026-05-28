A students record managemenyt system .......



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
    print("4.Exit System")

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
        print("EXITING THE SYSTEM.......")
        break
    else:
        print("Invalid Choice..Please Check once and Try again")

OUTPUT:

__Student Management System__

1.Add Student
2.Show Student Details
3.Exit System
Enter the choice:1
Enter the number of students to add:10
Enter name of student:Ram
Enter the marks of a student:98

__Student data saved succesfully__

Enter name of student:Abhi 
Enter the marks of a student:89

__Student data saved succesfully__

Enter name of student:Danu
Enter the marks of a student:99

__Student data saved succesfully__

Enter name of student:Karthik
Enter the marks of a student:78

__Student data saved succesfully__

Enter name of student:Sharath
Enter the marks of a student:87

__Student data saved succesfully__

Enter name of student:Rohit
Enter the marks of a student:85

__Student data saved succesfully__

Enter name of student:Hemanth
Enter the marks of a student:84

__Student data saved succesfully__

Enter name of student:Mahesh
Enter the marks of a student:55

__Student data saved succesfully__

Enter name of student:Kiran
Enter the marks of a student:78

__Student data saved succesfully__

Enter name of student:Amith
Enter the marks of a student:65

__Student data saved succesfully__


__Student Management System__

1.Add Student
2.Show Student Details
3.Exit System
Enter the choice:3
EXITING THE SYSTEM.......
PS C:\Users\Rajesh G R\Documents\oop project> 

STUDENT DETAILS FILE 
ADDED STUDENT MANAGEMENT SYSTEM FILE
Ram 98
Abhi 89
Danu 99
Karthik 78
Sharath 87
Rohit 85
Hemanth 84
Mahesh 55
Kiran 78
Amith 65

