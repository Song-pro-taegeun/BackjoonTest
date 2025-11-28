
wordInfos = [input() for _ in range(20)]
subjectScoreSum = 0 # 과목평점 * 학점 총합
subjectCount = 0 # P를 제외한 과목의 학점의 합
result = 0

for inputWord in wordInfos:
    info = inputWord.split()
    credit = float(info[1])
    grade = info[2]

    # P 과목은 계산 제외
    if grade == "P":
        continue

    subjectCount += credit

    if grade == "A+":
        subjectScoreSum += credit * 4.5
    elif grade == "A0":
        subjectScoreSum += credit * 4
    elif grade == "B+":
        subjectScoreSum += credit * 3.5
    elif grade == "B0":
        subjectScoreSum += credit * 3
    elif grade == "C+":
        subjectScoreSum += credit * 2.5
    elif grade == "C0":
        subjectScoreSum += credit * 2
    elif grade == "D+":
        subjectScoreSum += credit * 1.5
    elif grade == "D0":
        subjectScoreSum += credit * 1
    elif grade == "F":
        subjectScoreSum += credit * 0

result = subjectScoreSum / subjectCount
print("{:.6f}".format(result))