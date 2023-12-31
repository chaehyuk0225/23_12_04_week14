#<오픈소스프로그래밍 기말 프로젝트>
#
# ● 아래의 코드를 수정 혹은 프로그래밍하여 문제를 해결하시오.
# ● 문제의 점수는 각각 표시되며, 부분점수가 존재합니다.
#
# 학번 : 20201870 이름 : 방채혁

import os
import time

# Q.1 10점
#
# 문자열 my_string과 target이 매개변수로 주어질 때,
# target이 문자열 my_string의 부분 문자열이라면 1을,
# 아니라면 0을 return 하는 solution 함수를 작성하시오.
#
# 제한사항
# 1 ≤ my_string 의 길이 ≤ 100
# my_string 은 영소문자로만 이루어져 있습니다.
# 1 ≤ target 의 길이 ≤ 100
# target 은 영소문자로만 이루어져 있습니다.

def solution(my_string, target): #my_stuing 오타수정
    if my_string.find(target) == -1: #if문으로 경우를 나눔 부분 문자열일 때, 부분 문자열이 아닐 때 find 함수를 사용하여 부분 문자열을 판단 
        answer = 0
    else: 
        answer = 1
    return answer

# Q.2 10점
#
# 모스부호 해독 프로그램 만들기
# 문자열 letter 가 매개변수로 주어질 때,
# letter 영어 소문자로 바꾼 문자열을 return 하는
# solution 함수를 완성하시오.
#
# 제한사항
# 1 ≤ letter 의 길이 ≤ 1,000
# letter 의 모스부호는 공백으로 나누어져 있습니다.
# letter 에 공백은 연속으로 두 개 이상 존재하지 않습니다.
#
# letter = 여러분의 좌우명 또는 인상 깊었던 말을 쓰시오.
# letter = ('Life is unfair get used to it')
# letter = ('.-.. .. ..-. . .. ... ..- -. ..-. .- .. .-. --. . - ..- ... . -.. - --- .. -')

def solution(letter):
    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'}
    answer = ''
    decode = letter.split()    #split 함수를 사용하여 letter를 공백단위로 나눔
    for i in decode:           #for문을 사용하여 공백단위로 나눠진 letter의 갯수만큼 반복
        answer += (morse[i])   #해석 된 값이 answer에 추가됨
    return answer

# Q.3 10점
#
# 행성의 나이를 알파벳으로 표현할 때,
# a는 0, b는 1, ..., j는 9
# 예를 들어 cd는 23살, fb는 51살입니다.
# age가 매개변수로 주어질 때
# PROGEAMMER-857식 나이를 return 하도록
# solution 함수를 완성하시오.
#
# 제한사항
# age는 자연수입니다.
# age ≤ 1,000
# PROGRAMMERS-857 행성은 알파벳 소문자만 사용합니다.

def solution(age):
    morse = { 
    '0':'a','1':'b','2':'c','3':'d','4':'e','5':'f',  #위 모스부호 morse표와 같이 딕셔너리로 'a는 0, b는 1, ..., j는 9' 이 조건을 나타냄
    '6':'g','7':'h','8':'i','9':'j'}
    answer = ''
    for i in age:             #for문을 사용하여 age의 갯수만큼 반복(자릿수만큼)
        answer += (morse[i])  #변경 된 값이 answer에 추가됨
    return answer

# Q.4 10점
#
# x축과 y축으로 이루어진 2차원 직교 좌표계에 중심이 원점인
# 서로 다른 크기의 원이 두 개 주어집니다.
# 반지름을 나타내는 두 정수 r1, r2가 매개변수로 주어질 때,
# 두 원 사이의 공간에 x좌표와 y좌표가 모두 정수인 점의 개수를
# return하도록 solution 함수를 완성해주세요.
# ※ 각 원 위의 점도 포함하여 셉니다.
#
# 제한사항
# 1 ≤ r1 < r2 ≤ 1,000,000

def solution(r1, r2):
    answer = 0
    return answer

# Q.5 10점
#
# 0 또는 양의 정수가 주어졌을 때,
# 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.
#
# 예를 들어, 주어진 정수가 [6, 10, 2]라면
# [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고,
# 이중 가장 큰 수는 6210입니다.
#
# 0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때,
# 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어
# return 하도록 solution 함수를 작성해주세요.
#
# 제한사항
# numbers의 길이는 1 이상 100,000 이하입니다.
# numbers의 원소는 0 이상 1,000 이하입니다.
# 정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.
#
# numbers = [8, 30, 17, 2, 23]
import random
def solution(numbers):
    answer = ''
    for i in numbers                           #for문으로 numbers에 갯수만큼 반복
    rnum1 = random.shuffle(numbers)            #shuffle함수로 numbers에 요소들을 무작위로 배열하여 rnum1에 저장
    rnum2 = random.shuffle(numbers)            #shuffle함수로 numbers에 요소들을 무작위로 배열하여 rnum2에 저장                   
        if ''.join(rnum1) > ''.join(rnum2):    #rnum1과 rnum2를 이어 정수로 크기를 비교 rnum1이 크다면 rnum1를 정수로 answer에 저장
            answer = ''.join(rnum1)           
        elif ''.join(rnum1) < ''.join(rnum2):  #rnum2가 크다면 rnum2를 정수로 answer에 저장
            answer = ''.join(rnum2)
        elif ''.join(rnum1) = ''.join(rnum2):  #rnum1 rnum2가 서로 같다면 0을 저장
            answer = 0
    return str(answer)                         #answer값을 문자열로 반환
