# coding=utf-8

from typing import List

# @solution-sync:begin
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index01 in range(len(nums)):
            for index02 in range(index01+1, len(nums)):
                if nums[index01] + nums[index02] == target:
                    return [index01, index02]
# 双循环+双指针
# 枚举所有的数据，双层循环实现，双指针移动指向数据
# @solution-sync:end


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9

    result = Solution().twoSum(nums, target)
    print(result)
