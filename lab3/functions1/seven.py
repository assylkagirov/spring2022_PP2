def has_33(nums):
     print(any(nums[i+1] == nums[i] == 3 for i in range(len(nums) - 1)))

has_33([1, 3, 3]) 
has_33([1, 3, 1, 3]) 
has_33([3, 1, 3]) 