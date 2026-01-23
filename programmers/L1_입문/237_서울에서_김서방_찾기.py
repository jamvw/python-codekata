# 서울에서 김서방 찾기
# 프로그래머스 L1 (입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12919
# 알고리즘: 배열, 탐색
# 작성자: 표주하
# 작성일: 2026. 01. 23. 09:56:39

def solution(seoul):
    kim_position = seoul.index("Kim")
    answer = f"김서방은 {kim_position}에 있다"
    return answer