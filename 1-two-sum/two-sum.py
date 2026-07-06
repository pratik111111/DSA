class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1,len(nums)):
                if nums[i] + nums[j] == target:
                    print(f"Indicies",i,j)
                    print(f"Numbers",nums[i],nums[j])
                    return[i,j]

nums = [2,7,11,15]
target = 9
soul = Solution()

soul.twoSum(nums,target)


