def filter_prime(nums): 
    cnt = 0 
    for i in range(2,nums-1): 
        if nums % i == 0: 
            cnt+=1 
    if cnt == 0: 
        print(nums, end = ' ') 
        
list1 = list(map(int, input().split()))         
for i in list1: 
    filter_prime(i)