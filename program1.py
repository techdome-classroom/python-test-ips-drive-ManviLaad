from typing import List 
def smallest_missing_positive_integer(nums: List[int]) -> int:
    nums_set = set(nums)
    for i in range (1 , len(nums) +2):
                    if i not in nums_set:
                            return i
   
nums = [3,4,-1,1]
print (smallest_missing_positive_integer(nums))








    



  

