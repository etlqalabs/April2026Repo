name1 = {"Ram","Shyam","Ghanshyam","Vijay"}
name2 = {"Ram","Shyam","Ajay","Vijay"}

emp_dict = {"name":"Mayanak","city":"Bangalore","age":30}
email = "etlqalabs@gmail.com"
list_num = [1,20,30,5,6,90]

'''
name = {"Ram","Shyam","Ghanshyam"}

name.add("ajay")
name.add(30)
print("Original list : " ,name)

removed1 = name.remove("Ram")
print(name)
print(removed1)


removed2 = name.pop()
print(name)
print(removed2)





# Union
ans1 = name1.union(name2)
print(ans1)

ans2 = name1 |name2
print(ans2)

# Intersection
ans1 = name1.intersection(name2)
print(ans1)

ans2 = name1 & name2
print(ans2)


# minus/ difference

ans1 = name1.difference(name2)
print(ans1)

ans2 = name1 - name2
print(ans2)

ans1 = name2.difference(name1)
print(ans1)



# symmteric difference
ans =  name1.symmetric_difference(name2)
print(ans)

ans2 = name1.difference(name2).union(name2.difference(name1))
print(ans2)



# discard vs remove
print("before :",name1)
name1.discard("Ram")
print("After discard 1 :",name1)
name1.discard("Ramesh")
print("after 2 :",name1)
name1.remove("Ramesh")
print("after :",name1)



# Iterate each elements in the list snad set

name_list = ["Ram","Shyam","Ghanshyam","Vijay"]
n = len(name_list)  # 4

for idx in range(0,n,1):
    print("Hello !",name_list[idx])

for name in name_list:
    print("Hello !",name)


name_set = {"Ram","Shyam","Ghanshyam","Vijay"}

for name in name_set:
    print("Hello !",name,"printing from set")

# Q1 . Given 2 list of numbers , can you find all the unique elements from both?



# Dictionary ( unordered and mutable )

emp_dict = {"name":"Mayanak","age":30,"city":"Bangalore"}

print(emp_dict["name"])
print(emp_dict["city"])

keys = emp_dict.keys()
print(keys)

values = emp_dict.values()
print(values)

items = emp_dict.items()
print(items)

# Get all the keys and corresponding values


for key,val in emp_dict.items():
    print(key,"=>",val)


popped_val = emp_dict.pop("name")
print("opoped value : ",popped_val)
print("dict after pop: ",emp_dict)


popped_item = emp_dict.popitem()
print(popped_item)

# Access value of a key
print(emp_dict["name"])
print(emp_dict.get("name"))



# Strings

print(ord('A')) # 65
print(ord('Z'))

print(ord('a')) # 97
print(ord('z'))

print(ord("@"))


#print(email.upper())
n = len(email)
print(n) # 19 => index range (o to 18)
#print(email[18])

# Traversal in the string

# range(0,n,1) => range(n)

print(" indexed based for loop")
for idx in range(0,n,1):
    print(email[idx])

print(" extended for loop")
for ch in email:
    print(ch)



print(email)
# String slicing

# print first 5 characteres  - index : 0,1,2,3,4
print(email[0:5:1])

print(email[0:5:2])

print(email[0::2])

# print from 5th character onward to the end of the string

print(email[4::1])

# Reverse the string

print(email[::-1])

# print last 5 chatrcters in the reverse order the string

print(email[-1:-5:-1])

print(email[18:14:-1])


# Split

name = "etl-qa-labs"
name_list = name.split("-")
print(name_list)

# Print the words in the list in reverse order
name = "etl-qa-labs"
# expected = "labs-qa-etl"

name = "etl-qa-labs"
name_list = name.split("-")
print(name_list[::-1])
reverse_list = name_list[::-1]
ans_str = ""
for word in reverse_list:
    ans_str = ans_str+word+"-"
print("Answer is :",ans_str)



# Q1 . Give a list of numbers , can you get me the code for finding the highest number.



# Way 1
n = len(list_num) # 5
max_num = list_num[0] # 1
for idx in range(1,n,1):
    next_num = list_num[idx]
    if next_num > max_num:
        max_num = next_num
print(max_num)

# Way 2
max_num = list_num[0] # 1
for next_num in list_num:
    if next_num > max_num:
        max_num = next_num
print(max_num)



list_num = [1,20,30,5,6,90]

def get_max_void(list_num):
    n = len(list_num)
    max_num = list_num[0]
    for idx in range(1, n, 1):
        next_num = list_num[idx]
        if next_num > max_num:
            max_num = next_num
    print(max_num)

ans  = get_max_void(list_num)
print(ans)

def get_max_return(list_num):
    n = len(list_num)
    max_num = list_num[0]
    for idx in range(1, n, 1):
        next_num = list_num[idx]
        if next_num > max_num:
            max_num = next_num
    print(max_num)
    return max_num

ans  = get_max_return(list_num)
print(ans)


# Class Assignment : Find prime numbers between 1 to 20
# prime numbers - factors should be extactly 2 ( 1 & another the number itself)
# 2 => (1,2)
# 5 => (1,5)
# 6 => (1,2,3,6) = 4 factors , not a prime number
 # Hint: nested for loop

'''

list_num = [[1,2],[3,4]]
min_list = list_num[0]
print(min_list[1])



