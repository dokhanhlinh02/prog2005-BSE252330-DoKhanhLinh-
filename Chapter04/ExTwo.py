# Bài 2:
students = {
    "Yến": 10,
    "Nhi": 8.9,
    "Trà": 8.4
}
def average_score(student_dict):
    total = sum(student_dict.values())
    count = len(student_dict)
    return total/count
print("Điểm trung bình:",average_score(students))
