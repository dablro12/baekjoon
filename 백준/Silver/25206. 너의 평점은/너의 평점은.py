score_of_grade = {
    'A+' : 4.5,
    'A0' : 4.0,
    'B+' : 3.5,
    'B0' : 3.0,
    'C+' : 2.5,
    'C0' : 2.0,
    'D+' : 1.5,
    'D0' : 1.0,
    'F' : 0.0,    
}
total = 0.0
hak_total = 0.0
for _ in range(20):
    subject, score, grade = map(str, input().split())
    score = float(score)
    if grade != 'P':
        total += (score * score_of_grade[grade])
        hak_total += score
print(total/hak_total)