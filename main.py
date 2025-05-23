# grade_calculator.py

def get_marks():
    marks = []
    for i in range(1, 6):
        while True:
            try:
                mark = int(input(f"Enter marks for subject {i} (0-100): "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Marks should be between 0 and 100.")
            except ValueError:
                print("Please enter a valid number.")
    return marks

def calculate_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "Fail"

def main():
    marks = get_marks()
    total = sum(marks)
    percentage = (total / 500) * 100
    grade = calculate_grade(percentage)

    print("\n--- Result ---")
    print(f"Total Marks: {total}/500")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")

if __name__ == "__main__":
    main()
