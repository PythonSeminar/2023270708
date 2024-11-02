# 1. 학과 정보 입력 받기
# 학과명, 학생 수, 담당 교수 이름, 설립 연도를 입력 받아 변수에 저장
department_name = input("학과명을 입력하세요:")
student_count = int(input("학생 수를 입력하세요:"))
professor_name = input("담당 교수 이름을 입력하세요:")
established_year = int(input("학과 설립 연도를 입력하세요:"))

# 2. 학과 정보를 딕셔너리로 저장
department_info = {
    '학과명' : department_name,
    '학생 수' : student_count,
    '교수명' : professor_name,
    '설립 연도' : established_year
}

# 3. 학생 정보를 저장할 빈 리스트 생성
students = []

# 4. 5명의 학생 정보 입력 받기 
# 이름, 학번, 평균 학점, 수강 과목을 입력 받아 딕셔너리로 저장 후 리스트에 추가
# 수강 과목은 콤마로 구분된 입력을 받아 튜플로 변환
for i in range(5):
    student_name = input(f"학생 {i+1} 이름을 입력하세요:")
    student_id = input(f"학생 {i+1} 학번을 입력하세요:")
    student_average_grade = float(input(f"학생 {i+1} 평균 학점을 입력하세요:"))
    subjects = tuple(input(f"학생 {i+1} 수강 과목:").split(','))

    student_info = {
        '이름' : student_name,
        '학번' : student_id,
        '평균 학점' : student_average_grade,
        '수강 과목' : subjects
    }

    students.append(student_info)

# 5. 학과 정보 처리
# 학과명과 설립 연도 연결, 학과명 반복, 학과명 길이 계산
combined_department_name_and_established_year = department_info['학과명'] + " " + str(department_info['설립 연도'])
repeated_department_name = department_info['학과명'] * 3
department_name_length = len(department_info['학과명'])

print(f"학과명과 설립 연도: {combined_department_name_and_established_year}")
print(f"학과명 3번 반복: {repeated_department_name}")
print(f"학과명 길이: {department_name_length}")

# 6. 학생 정보 처리
# 첫 번째와 마지막 학생 정보 출력
# 2~4번째 학생 정보 출력
# 새로운 학생 추가 및 첫 번째 학생 삭제
first_student = students[0]
last_student = students[-1]
middle_students = students[1:4]
print(f"첫 번째 학생: {first_student}")
print(f"마지막 학생: {last_student}")
print(f"2~4번째 학생: {middle_students}")
students.append({'이름' : '전재희', '학번' : '2023270708', '평균 학점' : 4.5, '수강 과목' : ('과학',)})
students.pop(0)
print("새로운 학생이 추가 및 첫 번째 학생 삭제:", students)

# 7. 학과 통계 계산
# 평균 학점의 평균 계산
# 3.5 이상 학점 학생 수 계산
# 최고 및 최저 평균 학점 찾기
average_grade = sum([student['평균 학점'] for student in students]) / len(students)
high_grade_students = sum([student['평균 학점'] >= 3.5 for student in students])
max_grade = max([student['평균 학점'] for student in students])
min_grade = min([student['평균 학점'] for student in students])

print(f"평균 학점: {average_grade}")
print(f"평균 학점 3.5 이상인 학생 수: {high_grade_students}")
print(f"최고 학점: {max_grade}")
print(f"최저 학점: {min_grade}")

# 8. 추가 기능 구현
# 학과 정보에 인증 여부 추가
# 특정 학생 정보 검색 기능 구현e
department_info["certified"] = input("학과가 인증되었습니까? (Yes/No): ").lower() == 'yes'

search_name = input("정보를 검색할 학생 이름을 입력하세요: ")
searched_student = next((student for student in students if student['이름'] == search_name), None)
if searched_student:
    print(f"\n{search_name} 학생의 정보:", searched_student)
else:
    print(f"\n{search_name} 학생의 정보가 없습니다.")

# 9. 모든 정보 출력
# 처리된 학과 정보, 학생 정보, 통계 결과 출력
