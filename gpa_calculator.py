class RangeError(Exception):
    pass


while True:
    min_range = 0
    max_range = 100
    try:
        bangla = float(input("Enter the marks of Bangla: "))
        if bangla < min_range or bangla > max_range:
            raise RangeError
        english = float(input("Enter the marks of English: "))
        if english < min_range or english > max_range:
            raise RangeError
        math = float(input("Enter the marks of Mathematics: "))
        if math < min_range or math > max_range:
            raise RangeError
        science = float(input("Enter the marks of Science: "))
        if science < min_range or science > max_range:
            raise RangeError
        break

    except ValueError:
        print("Please Enter a valid input. \nTry Again")
    except RangeError:
        print("Please Enter a value from 0 -100. \nTry Again")

avg_total_marks = (bangla + english + math + science) / 4
print(avg_total_marks)

if avg_total_marks > 90:
    print("The grade : A+")
elif avg_total_marks >= 81 and avg_total_marks <= 90:
    print("The grade : A")
elif avg_total_marks >= 71 and avg_total_marks <= 80:
    print("The grade : B")
elif avg_total_marks >= 61 and avg_total_marks <= 70:
    print("The grade : C")
elif avg_total_marks >= 41 and avg_total_marks <= 60:
    print("The grade : D")
else:
    print("The grade : F")
