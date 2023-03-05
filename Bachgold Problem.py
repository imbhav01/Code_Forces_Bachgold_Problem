x = int(input())
y = []
if (x > 1):
    for i in range(2, int(x/2)+1):
        if (x % i) == 0:
            break
        else:
            y.append(i)
else:
    y.append(i)


print(y)