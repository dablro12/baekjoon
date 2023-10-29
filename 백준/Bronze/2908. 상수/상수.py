a, b = map(str, input().split())
a, b = a[::-1], b[::-1]
print(max(list([int(a),int(b)])))