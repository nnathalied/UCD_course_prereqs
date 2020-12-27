from get_courses import get_courses


# prereqs = []
# course_subject = "ABI"
# course_number = "50A"
# search_subject = "ABI"


# get_courses(course_subject, course_number, search_subject, prereqs)

# print("Prereqs: \n")
# for i in prereqs:
#     print(i, "\n")

prereqs = []
course_subject = "BIS"
course_number = "002A"
search_subject = "BIS"

get_courses(course_subject, course_number, search_subject, prereqs)

print("-- Courses with {} {} as a prerequisite: --\n".format(course_subject, course_number))
for i in range(len(prereqs)):
    print("-- {} --\n".format(i + 1))
    print("{}\n".format(prereqs[i]))
    
# prereqs = []
# course_subject = "ECS"
# course_number = "36B"
# search_subject = "ECS"

# get_courses(course_subject, course_number, search_subject, prereqs)

# print("-- Courses with {} {} as a prerequisite: --\n".format(course_subject, course_number))
# for i in range(len(prereqs)):
#     print("-- {} --\n".format(i + 1))
#     print("{}\n".format(prereqs[i]))

