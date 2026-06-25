d1 = {
    'a': 100, 
    'b': 200,
    'c': 300
}
d2 = {
    'a': 300,
    'b': 200,
    'd': 400
}
track = []

print("Counter:({", end="")
for x in d2.keys():
    print("'"+x+"':", end=" ")
    printed = False
    for y in d1.keys():
        if(x == y):
            d2[x] += d1[y]
            track.append(x)
    print(d2[x], end=" ")

for a in d1.keys():
    if a in track:
        pass
    else:
        print("'"+a+"':",d1[a], end=" ")
print("})")  
    
        