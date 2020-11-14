for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)

    if n == 1:
        print(a[0])
    elif n == 2:
        print(max(a))
    elif n == 3:
        t = 0
        if a[0] == a[1]:
            t = t+a[0]+a[2]
        else:
            t = a[1]
            if a[0]-a[1] <= a[2]:
                t = t+a[2]
            else:
                t = a[0]

        print(t)
    elif n == 4:
        t = 0
        if a[0] == a[1]:
            t = a[0]
            if a[2] == a[3]:
                t = t+a[2]
            else:
                if a[3] > a[2]:
                    t += a[3]
                else:
                    t += a[2]

        else:
            t = a[1]
            if a[2] == a[0]-a[1]:
                t += a[2]+a[3]
            else:
                if a[2] < a[0]-a[1]:
                    t = t+a[2]
                    if a[3] > a[0]-a[1]-a[2]:
                        t = t+a[3]
                    else:
                        t = t+a[0]-a[1]-a[2]
                elif a[2] > a[0]-a[1]:
                    t = t+a[0]-a[1]
                    if a[3] > a[2]-a[0]+a[1]:
                        t = t+a[3]
                    else:
                        t = t+a[2]-a[0]+a[1]

        print(t)
