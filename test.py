answers = []
for i in range(1000, 9999):
    dBy12 = i % 12 == 0
    dBy20 = i % 20 == 0
    dBy16 = i % 16 == 0
    if dBy12 and dBy20 and not dBy16:
        answers.append(i)

print(len(answers))
