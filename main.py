'''*** 
extract.py
uses get_courses(course_subject, course_number, search_subject, prereqs)
from get_courses.py

started: 2020-10-12

fetches and prints courses in the department <search_subject>
you gain access to by taking <course_subject course_number>

uses code from https://matix.io/extract-text-from-webpage-using-beautifulsoup-and-python/
to extract text from UC Davis General Catalog 

***'''

from get_courses import get_courses

course_subject = input("course subject (ex: MAT): ")
course_number = input("3 digit, optional 1 letter course number (ex: 012, 022A): ")
subject = input("department to search (ex: ECS): ")

#attempt to check all subjects
#did not work, will need database
# subjects_list = []
# f = open("subjects.txt", "r")
# for line in f:
#     subject = line[0:3]
#     subjects_list.append(subject)

# prereqs = []
# for subject in subjects_list:
#     get_courses(course_subject, course_number, subject, prereqs)

prereqs = []
get_courses(course_subject, course_number, subject, prereqs)

print("-- Courses with {} {} as a prerequisite: --\n".format(course_subject, course_number))
for i in range(len(prereqs)):
    print("-- {} --\n".format(i + 1))
    print("{}\n".format(prereqs[i]))