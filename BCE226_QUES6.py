import BCE226_QUES1 as gcs
import BCE226_QUES3 as gcf
import BCE226_QUES245 as ga

"""

enrollment_no    percentage     admission_college/branch_code      day
sort students percentage wise
extra files: no remaining choices left of a student in that case

"""

college_details = gcs.college_details()
gcs.student_details()
student_results = ga.rank_students()
student_choices = gcf.fill_choice_filling()
# print(student_results)
# print(student_choices)
# print(college_details)

ga.create_day_wise_admission(student_results, student_choices, college_details)


