# 하샤드 수
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12947
# 알고리즘: 수학, 문자열
# 작성자: 표주하
# 작성일: 2026. 01. 17. 18:47:33

def solution(x):
    digit_sum = 0
    for i in str(x):
        digit_sum += int(i)
        
    if x % digit_sum == 0:
        return True
    else:
        return False