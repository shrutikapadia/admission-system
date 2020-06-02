import csv
import random

branches = ["CSE", "IT", "ME", "EE", "EC", "IC", "CH", "Civil", "Auto"]  #total branches available
college_details = []

#Generate the college_details.csv for 50 colleges (ques-1) part-(a).

def college_details():
    colleges = []
    college_detail = [["CollegeCode", "CSE", "IT", "ME", "EE", "EC", "IC", "CH", "Civil", "Auto"]]
    with open('college_details.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(college_detail[0])  #writing code of college in first coloum.
        capacity = [0, 60, 120, 180, 240]

        for _ in range(50):
            college_code = "C"
            clg_code = random.randint(0, 9999)
            clg_code = "0" * (4 - len(str(clg_code))) + str(clg_code)# putting value of coolege code in clg_code
            while college_code in colleges:
                clg_code = random.randint(0, 9999)
            college_code += "0" * (4 - len(str(clg_code))) + str(clg_code)
            colleges += [college_code]# appending college code in list colleges
            clg_branch = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            while clg_branch == [0, 0, 0, 0, 0, 0, 0, 0, 0]:
                clg_branch = []
                for _ in range(9):
                    clg_branch += [capacity[random.randint(0, 4)]] # randomaly selecting the seat capacity of student in each branch
            row = [college_code] + clg_branch
            college_detail += [row] # creating another coloum which contains name of branch
            writer.writerow(row)
        return college_detail   # returns filr which contain college code3 , branch name with capacity.

#generating studentdetais.csv for 5000 students ques-1 part-(b).

def student_details():
    students = []
    student_detail = []
    with open('student_details.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["EnrollmentNo", "sub1", "sub2", "sub3", "sub4", "sub5"])

        for _ in range(5000):
            enrollment_no = "E"              #code for generating enrolment number
            code = random.randint(0, 9999)    #code for generating enrolment number
            code = "0" * (4 - len(str(code))) + str(code)    #code for generating enrolment number
            while enrollment_no in students:    #code for generating enrolment number
                code = random.randint(0, 9999)    #code for generating enrolment number
            enrollment_no += "0" * (4 - len(str(code))) + str(code)     #code for generating enrolment number
            students += [enrollment_no]     #code for generating enrolment number

            subject_marks = []       #generating marks for 5 subject of student
            for _ in range(5):
                subject_marks += [random.randint(40, 100)]
            row = [enrollment_no] + subject_marks
            student_detail += [row]
            writer.writerow(row)
    return students, student_details
