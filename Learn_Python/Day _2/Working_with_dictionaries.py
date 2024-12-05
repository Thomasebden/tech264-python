#1
student_1 = {
    "name": "susan",
    "stream": "tech",
    "completed_lessons": 4,
    "completed_lesson_names": ["variables", "data_types", "set up"],
    "Age": 44
}

#toms
student_2 = {
    "name": "Thomas",
    "stream": "Law",
    "completed_lessons": 8,
    "completed_lesson_names": ["criminal", "contract", "tort"],
    "Age": 21
}

# 3
print("Dictionary:", student_1)

#toms
print("Dictionary:", student_2)

# 4
print("Data type:", type(student_1))

#toms
print("Data type:", type(student_2))

# 5
print("Value for 'stream':", student_1["stream"])

# 6
print("Value for 'completed_lesson_names':", student_1["completed_lesson_names"])

# 7
print("Data type of 'completed_lesson_names':", type(student_1["completed_lesson_names"]))

# 8
print("First element in 'completed_lesson_names':", student_1["completed_lesson_names"][0])

# 9
student_1["completed_lessons"] = 3
print("Updated dictionary:", student_1)

# 10
#student_1["completed_lesson_names"].remove("data_types")
#print("Updated dictionary after removing 'data_types':", student_1)

del student_1['completed_lesson_names'][1]
print(student_1['completed_lesson_names'])
#kevin's path -- uses the remove the index,

# 11
print("Keys in the dictionary:", student_1.keys())

