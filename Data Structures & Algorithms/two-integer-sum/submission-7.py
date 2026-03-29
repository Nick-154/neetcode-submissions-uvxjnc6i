class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mappy = {}

        for i,n in enumerate(nums):
            differ = target - n

            if differ in mappy:
                return [mappy[differ], i]
            mappy[n] = i 
        return