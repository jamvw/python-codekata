# 정수 내림차순으로 배치하기
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12933
# 알고리즘: 문자열, 정렬
# 작성자: 표주하
# 작성일: 2026. 01. 17. 02:21:47

def solution(n):
    x = list(str(n))
    x.sort(reverse=True)
    return int("".join(x))
