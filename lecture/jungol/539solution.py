sum = 0
cnt = 0
while True:
    listVal = list(input().split(" "))
    # print(listVal)
    check = False
    for n in listVal:
        n = int(n)
        cnt += 1
        sum += n
        if n >= 100:
            check = True
            break
    if check:
        break
print(sum)
avg = sum/cnt
print("%.1f"%avg)