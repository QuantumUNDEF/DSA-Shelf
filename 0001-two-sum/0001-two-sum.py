class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mymap = {}
        for i in range(len(nums)):
            need = target - nums[i]
            if need in mymap:
                return [mymap[need], i]
            mymap[nums[i]] = mymap.get(nums[i],i)
