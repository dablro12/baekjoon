n = int(input())

word_li = []
for i in range(n):
    word_li.append(input())

word_li  = list(set(word_li))

word_len_li = []
for word in word_li:
    word_len_li.append([word, len(word)])
word_len_li.sort(key = lambda word_len_li : (word_len_li[1], word_len_li[0])) #첫번쨰로 숫자 정렬 두번쨰로 문자열정렬

for word, len_word in word_len_li:
    print(word)
    