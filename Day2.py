# Control statements

'''
age = 16

# procedural way
if age >= 18:
    print("Person is elligible for voting")
elif  age == 17:
    print("Person is elligible for voting next year")
else:
    print("Person is not elligible for voting")


# functional way
def is_elligible_voting(age):
    if age >= 18:
        print("Person is elligible for voting")
    elif age == 17:
        print("Person is elligible for voting next year")
    else:
        print("Person is not elligible for voting")

is_elligible_voting(18)
is_elligible_voting(10)



# Looping statement
# print 1 to 5
print(" printing 1 to 5 using sequenctial way")
print(1)
print(2)
print(3)
print(4)
print(5)

# Using for loop
print(" printing 1 to 5 using for loop")
for num in range(1,6):
    print(num)

# Using for while
print(" printing 1 to 5 using while loop")
num = 1
while num <= 5:
    print(num)
    num = num + 1



# Primitve data types :
course_name = "ETL Testing Automation"
print(type(course_name))
course_duration = 3
print(type(course_duration))
course_fee  = 12.5
print(type(course_fee))
enrollment_available = True
print(type(enrollment_available))



# List : an ordered collection ( insertion order ) of items that is mutable( changed)
marks_list = [99,70,65,55,45]

print(marks_list)
# Fetch each marks and add 5 to it and print them
for mark in marks_list:
    print(mark+5)



marks_list = [99,70,65,55,45]
print(marks_list[0])
print(marks_list[4])

n = len(marks_list)
print(n)

for idx in range(n):
    print(marks_list[idx])




# List slicing
marks_list = [99,70,65,55,45]

print(marks_list[0])
print(marks_list[1])
print(marks_list[2])

print(marks_list[0:3:1])

print(marks_list[0:3:2])

marks_list = [99,70,65,55,45,85,79]
print(" elements are even index :",marks_list[::2])
print(" elements are odd index :",marks_list[1::2])
print(" elements are odd index in reverse :",marks_list[::-2])
print(" elements in reverse :",marks_list[::-1])



# key funtions in the list:

list1 = [99,70,65,"Rakesh",65.8]
print("type is ",type(list1))

print("  list is ",list1)
list1.append(100)
print(" new list is ",list1)

list1.insert(2,"Ankur")
print(" new list is ",list1)

list2 = [1,2]
list1.extend(list2)
print(" new list is ",list1)

list1.remove("Ankur")
print(" new list is ",list1)

list1.pop()
print(" new list is ",list1)

popped_item = list1.pop(1)
print(" new list is ",list1)
print(popped_item)
del list1[1]  # delete in sql
print(" new list is ",list1)

list1.clear() # ( trcuncate )
print(" new list is ",list1)

# del list1  ( drop in SQL )



list1 = ["Ankur","Mayank","Akash"]
print("Before sorting :",list1)
list1.sort()
print("After  sorting in ascending order  :",list1)



# problem 1 : Given a list of numbers , find the higest number
list_num = [10,45,23,99,12,67]
max_num = list_num[0]
for num in list_num:
    if num > max_num:
        max_num = num
print(max_num)


# Tuple
tuple_num = (10,45,23,99,12,10,12,12,67)
print(type(tuple_num))
print(tuple_num)
print(tuple_num.count(12))

# Convert the tuple to list
list_num = list(tuple_num)
print(list_num)
list_num.append(100)
print(list_num)
tuple2 = tuple(list_num)
print(tuple2)

list_num = [10,45,23,99,12,67]
print(max(list_num))

'''

# set

set_num = {10,45,23,99,12,67,10,10}
print(type(set_num))
print(set_num)

print(hash("ETL"))
print(hash(2))

# List to set
list_num = [10,45,23,99,12,67,10,10]
print(list_num)

print(set(list_num))