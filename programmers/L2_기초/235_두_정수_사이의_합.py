# 두 정수 사이의 합
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12912
# 알고리즘: 수학
# 작성자: 표주하
# 작성일: 2026. 01. 17. 18:47:50

def solution(a, b):
    return sum(range(min(a, b), max(a, b) + 1))