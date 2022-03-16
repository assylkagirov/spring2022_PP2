def spy_game(nums):
    mark = []
    for i in range(len(nums)):
        if nums[i] == 0 or nums[i] == 7:
            mark.append(nums[i])
    far = ""
    for i in range(len(mark)):
        far = far + str(mark[i])
        if far == '007':
            print('True')
            return
    print('False')

spy_game([1,2,4,0,0,7,5])
spy_game([1,0,2,4,0,5,7])
spy_game([1,7,2,0,4,5,0])
