import sys
input = sys.stdin.readline
n, m = map(int, input().strip().split()) #n,m 은 (1,100,000) 
poketmon_dict = {}
converted_poketmon_dict = {}
for idx in range(n): #첫글자만 대문자, 나머지 문자는 소문자 *예외 : 일부 포켓몬은 마지막 문자만 대문자일수도 있다.
    name = input().strip()
    poketmon_dict[idx] = name
    converted_poketmon_dict[name] = idx
    
for _ in range(m):
    quiz = input().strip()
    if quiz.isdigit() == True:# quiz가 숫자로 들어오면 
        print(poketmon_dict[int(quiz)-1]) #사전영어를 출력
    else : #quiz가 영어로 들어오면
        print(converted_poketmon_dict[quiz]+1) #숫자를 출력