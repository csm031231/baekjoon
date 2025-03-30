start_num = int(input())
last_num = int(input())

s_list = []
for num in range(start_num, last_num+1):
    error = 0
    if num > 1 :
        for i in range(2, num): 
            if num % i == 0:
                error += 1
                break  
        if error == 0:
            s_list.append(num) 
            
if len(s_list) > 0 :
    print(sum(s_list))
    print(min(s_list))
else:
    print(-1)