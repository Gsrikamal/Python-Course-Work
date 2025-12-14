# Student Grade Calculator

def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"

def main():
    print("===== Student Grade Calculator =====")

    # Input marks for five subjects
    marks = []
    for i in range(1, 6):
        score = float(input(f"Enter marks for Subject {i}: "))
        marks.append(score)

    # Total and Percentage
    total = sum(marks)
    percentage = (total / 500) * 100
    grade = calculate_grade(percentage)

    # Output
    print("\n===== RESULT =====")
    print(f"Total Marks: {total}/500")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")

if __name__ == "__main__":
    main()
    