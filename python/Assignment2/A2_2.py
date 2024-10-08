def get_student_data():
    student_data = []
    while True:
        student_name = input("Enter student name (or type 'done' to finish): ")
        if student_name.lower() == 'done':
            break
        
        grades = {}
        while True:
            course_name = input(f"Enter course name for {student_name} (or type 'done' to finish courses): ")
            if course_name.lower() == 'done':
                break
            grade = float(input(f"Enter grade for {course_name}: "))
            grades[course_name] = grade
        
        student_data.append({"student_name": student_name, "grades": grades})
    
    return student_data

def calculate_average_grade_per_student(student_data):
    student_averages = {}
    for student in student_data:
        grades = student["grades"].values()
        average_grade = sum(grades) / len(grades)
        student_averages[student["student_name"]] = average_grade
    return student_averages

def find_top_performers(student_averages, threshold=90):
    top_students = {name: avg for name, avg in student_averages.items() if avg >= threshold}
    return top_students

def grade_distribution(student_data):
    distribution = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    for student in student_data:
        for grade in student["grades"].values():
            if grade >= 90:
                distribution["A"] += 1
            elif grade >= 80:
                distribution["B"] += 1
            elif grade >= 70:
                distribution["C"] += 1
            elif grade >= 60:
                distribution["D"] += 1
            else:
                distribution["F"] += 1
    return distribution

def main():
    print("Enter student names and their grades. Type 'done' when you are finished.")
    student_data = get_student_data()
    
    if student_data:
        student_averages = calculate_average_grade_per_student(student_data)
        top_students = find_top_performers(student_averages)
        distribution = grade_distribution(student_data)

        print("\nAverage Grade per Student:")
        for student, avg in student_averages.items():
            print(f"{student}: {avg:.2f}")

        print("\nTop-Performing Students:")
        if top_students:
            for student, avg in top_students.items():
                print(f"{student}: {avg:.2f}")
        else:
            print("No students with an average grade above the threshold.")

        print("\nGrade Distribution:")
        for grade, count in distribution.items():
            print(f"{grade}: {count}")
    else:
        print("No student data was entered.")

if __name__ == "__main__":
    main()
