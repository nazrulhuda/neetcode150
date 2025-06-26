#
class Solution:
     def hasDuplicate(self, nums):
          return len(nums)!=len(set(nums))
     
sol=Solution()
nums=[1,2,3,4]
print(sol.hasDuplicate(nums))
        
