num = {
    "V": 10,
    "VI": 10,
    "VII": 40,
    "VIII": 20,
    "IX": 70,
    "X": 80,
    "XI": 40,
    "XII": 20
}

numTrack = []

print("Counter:{(", end="")
for x in num.keys():
    counter = 0
    if(num[x] not in numTrack):
        print(num[x], end=": ")
        numTrack.append(num[x])
        counter += 1
    else:
        continue
    for y in num.keys():
        if x == y:
            pass
        else:
            if(num[x] == num[y]):
                counter += 1
    print(counter, end=" ")
print(")}")