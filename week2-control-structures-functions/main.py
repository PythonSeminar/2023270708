def input_student_info():
    name = input("학생 이름을 입력하세요: ")
    while True:
        try:
            score = int(input("학생의 점수를 입력하세요 (0-100): "))
            if 0 <= score <= 100:
                return {"name": name, "score": score}
            else:
                print("점수는 0에서 100 사이여야 합니다.")
        except ValueError:
            print("유효한 숫자를 입력해주세요.")

def calculate_grade(score):
    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score < 90:
        return 'B'
    elif 70 <= score < 80:
        return 'C'
    elif 60 <= score < 70:
        return 'D'
    else:
        return 'F'

def print_results(students):
    print("\n학생 성적 결과:")
    for student in students:
        name = student['name']
        score = student['score']
        grade = calculate_grade(score)
        print(f"이름: {name}, 점수: {score}, 등급: {grade}")

def calculate_stats(students):
    scores = [student['score'] for student in students]
    avg_score = sum(scores) / len(scores)
    max_score = max(scores)
    min_score = min(scores)
    return avg_score, max_score, min_score

def main():
    students = []
    print("학생 성적 관리 프로그램")
    
    while True:
        student = input_student_info()
        students.append(student)
        
        cont = input("계속해서 학생 정보를 입력하시겠습니까? (계속: Enter, 종료: q): ")
        if cont.lower() == 'q':
            break
    
    print_results(students)
    
    avg, max_score, min_score = calculate_stats(students)
    print(f"\n통계:")
    print(f"평균 점수: {avg:.2f}")
    print(f"최고 점수: {max_score}")
    print(f"최저 점수: {min_score}")

if __name__ == "__main__":
    main()
