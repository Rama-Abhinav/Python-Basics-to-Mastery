"""
    🎯 Project Goal:

        Build a Python program that:

            > Takes marks of students using the array module

            > Calculates:

                >> Total marks

                >> Average

                >> Highest and lowest marks

                >> Number of students who passed (>= 35)

    ✅ Final Output Example:
    
        Enter number of students: 5
        Enter marks of student 1: 45
        Enter marks of student 2: 82
        Enter marks of student 3: 29
        Enter marks of student 4: 50
        Enter marks of student 5: 36

        --- Analysis ---
        Total Students: 5
        Total Marks: 242
        Average Marks: 48.4
        Highest Marks: 82
        Lowest Marks: 29
        Number of Students Passed: 4

"""

import array

No_of_Students = int(input("How Many Students Attended the Exam (10,20,30...etc): "))
Student_Marks_Array = array.array('i',[])
No_of_Students_Passed = 0

for Student in range(No_of_Students):
    Marks = int(input(f"Enter Marks of Student {Student + 1}: "))
    if Marks>=35:
        Student_Marks_Array.append(Marks)
        No_of_Students_Passed += 1
    else:
        Student_Marks_Array.append(Marks)

print("-----ANALYSIS------")

print(f"\nTotal Marks:{sum(Student_Marks_Array)}\nAverage Marks of {No_of_Students} is:{sum(Student_Marks_Array)/No_of_Students}\nHighest Marks:{max(Student_Marks_Array)}\nLowest Marks:{min(Student_Marks_Array)}\nNo.of Students Passed:{No_of_Students_Passed}")



