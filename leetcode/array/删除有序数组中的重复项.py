# coding=utf-8

from typing import List

# @solution-sync:begin
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        a_i = 1
        b_i = 0
        while b_i < len(nums)-1:
            if nums[b_i] != nums[b_i + 1]:
                nums[a_i] = nums[b_i + 1]
                a_i = a_i+1
            b_i = b_i+1
        return a_i
# 双指针
# 指针一为判断数组内相邻数据是否相同，此为是否移动指针二的必要判断条件 while 循环实现，单层循环实现
# 指针二为变更数组内容的指针，该指针主要在满足条件的时候进行数据变更
# @solution-sync:end


if __name__ == '__main__':
    nums = [1, 1, 2]

    result = Solution().removeDuplicates(nums)
    print(result)
