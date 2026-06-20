
list_num = [1,2,5,8,10,20]
num_to_find = 10
s = "ETLQALABS"
list_num = [1,2,3,4,5,1,2,5,5]

'''
# Linear Search
def is_number_exist_linear(list_num,num_to_find):
    for ele in list_num:
        if ele == num_to_find:
            return True
    return False

ans = is_number_exist_linear(list_num,num_to_find)
print(ans)


# Binary Search
def is_number_exist_binary(list_num,num_to_find):
    left = 0
    right = len(list_num) -1
    while left <= right:
        mid = int((left + right)/2)
        if list_num[mid] == num_to_find:
            return True
        elif list_num[mid] < num_to_find:
            left = mid + 1
        else:
            right = mid -1
    return False

ans  = is_number_exist_binary(list_num,num_to_find)
print(ans)




# String slicing

s ="bangalorecity"
# first 4 charcter
print(s[0:4:1])
print(s[:4:1])
print(s[:4:])
print(s[:4])

# first 4 charcter in reverse order
print(s[3::-1])
print(s[-10::-1])
print(s[-10:-14:-1])
print(s[::-1])

print(s[::1])




# Split

s = "etl.qa.labs"
list = s.split(".")
print(list)



# Given a string check if it contains any lower case character and retun True if it does otherwise False.



# A (65 ) => Z(90)
# a(97) => z(122)
def is_lower_case_char_present(str):
    for ch in str:
        if (ord(ch)>=97 and ord(ch)<=122):
            return True
    return False

ans = is_lower_case_char_present(s)
print(ans)



# Q . Find and return a substring which starts from Q and ends with B
# s = "ETLQALABS
# o/p : QALAB

def get_substring(str):
    start_index= str.find('Q')
    end_index = str.find('B') +1
    ans = str[start_index:end_index:1]
    return ans
print(get_substring(s))

# Class Assignment : Solve this using for loop.




s = "ETL QA Labs"
 # Replace L(uppercase) with l(lowecase)
def replace_charcter(s):
    ans = ""
    for ch in s:
        if ch == "L":
            ans = ans+"l"
        else:
            ans = ans + ch
    return ans

ans = replace_charcter(s)
print(ans)



# Q. Given a list of numbers, count the occurence of each numbers and return them
# I/P : list_num = [1,2,3,4,5,1,2,5,5]
# O/P : {1:2,2:2,3:1,4:1,5:3}

def count_list_occurence(list):
    count_element = {}
    for ele in list:
        if ele in count_element:
            count_element[ele] = count_element[ele]+1
        else:
            count_element[ele] = 1
    return count_element

ans_dic = count_list_occurence(list_num)
print(ans_dic)

def get_duplicate_number(dictionary):
    duplicate_list  = []
    for key in dictionary.keys():
        if dictionary[key] > 1:
            duplicate_list.append(key)

    return duplicate_list

dups_list = get_duplicate_number(ans_dic)
print(dups_list)

def get_unique_number(dictionary):
    unique_list  = []
    for key in dictionary.keys():
        if dictionary[key] == 1:
            unique_list.append(key)

    return unique_list

unique_list = get_unique_number(ans_dic)
print(unique_list)


# Q . Given a list of numbers . get me all the duplicate numbers
# I/P : list_num = [1,2,3,4,5,1,2,5,5]

def get_duplicates_using_set(list):
    dupes_set = set()
    for ele in list:
        if list.count(ele) > 1:
            dupes_set.add(ele)
    return dupes_set

ans = get_duplicates_using_set(list_num)
print(ans)

def get_duplicates_using_list(list):
    dupes_list = []
    for ele in list:
        if list.count(ele) > 1 and ele not in dupes_list:
            dupes_list.append(ele)
    return dupes_list

ans = get_duplicates_using_list(list_num)
print(ans)


'''

import pandas as pd
df = pd.read_csv("emp.csv")
type(df)
print(df)


