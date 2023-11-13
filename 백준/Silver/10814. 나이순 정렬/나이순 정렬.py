import sys
input = sys.stdin.readline
n = int(input())
# db = [['21', 'Junkyu'], ['21', 'Dohyun'], ['20', 'Sunyoung']]
db = []

for i in range(n):
    db.append(input().split())
db.sort(key = lambda db: (int(db[0])))
for age, member in db:
    print(f"{age} {member}")