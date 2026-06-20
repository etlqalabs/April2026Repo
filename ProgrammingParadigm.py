channel_name = "ETL QA Labs"
course_name = "Automation Testing"
course_duration = 3

'''
# procedural way
print(channel_name)
print(course_name)
print(course_duration)

print(channel_name)
print(course_name)
print(course_duration)

print(channel_name)
print(course_name)
print(course_duration)


# Functional way
def print_details():
    print(channel_name)
    print(course_name)
    print(course_duration)
print_details()
print_details()
print_details()

'''



# OOP ( Object Oriented Programming )
class CourseDetails:
    def print_detail(self):
        print(channel_name)
        print(course_name)
        print(course_duration)

ref = CourseDetails()
ref.print_detail()






