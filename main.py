l = [1, 12, 5, -33, 9, 10, -100, -5]

maxx = max(l)  # 12
minn = min(l)  # -100

for index in range(0, len(l)):
    if l[index] == maxx:
        l[index] = minn
    if l[index] == minn:
        l[index] = maxx

print(l)