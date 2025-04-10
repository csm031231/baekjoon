a, b, c, m = map(int, input().split())

day = 0        # 시간 (0시부터 시작해서 24시까지 체크)
result = 0     # 일해서 번 돈 (또는 작업량)
counts = 0     # 현재 피로도


if a > m :
    print(0)
else:
    while day != 24 :
        day += 1
        if counts + a <= m:
            counts += a
            result += b
        else:
            if counts - c >= 0:
                counts -= c
            else:
                counts = 0  
    print(result)