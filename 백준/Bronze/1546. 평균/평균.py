import sys
input = sys.stdin.readline
n = int(input())
pre_scores = list(map(int, input().split()))
tmp_scores = pre_scores.sort()
max_score = pre_scores[-1]
total = 0
for pre_score in pre_scores:
    if pre_score <= max_score:
        total += (pre_score/max_score*100)
    else:
        total += max_score

print(total/n)