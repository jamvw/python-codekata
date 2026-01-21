# 자연수 뒤집어 배열로 만들기
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12932
# 알고리즘: 문자열, 배열
# 작성자: 표주하
# 작성일: 2026. 01. 21. 10:53:37

def solution(n):
    answer = []
    
    r_str = str(n)[::-1]
    for i in r_str:
        answer.append(int(i))
        
    return answer