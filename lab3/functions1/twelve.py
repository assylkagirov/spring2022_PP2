def histogram(nums):
    for i in range(len(nums)):
        abc = ""
        for f in range(int(nums[i])):
            abc = abc + "*"
        print(abc)

lst = input().split(' ')
histogram(lst)