def checkList(num):
    unique = []
    for i in num:
        if i in unique:
            continue
        else:
            unique.append(i)
            print(i ,"=>", end=" ")
            count = 0
            for j in num:
                if j==i:
                    count += 1
            print(count, end=" ")

num = [10,20,30,30,30,30,20,40]
checkList(num)
            
