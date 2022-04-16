"""
int[] nums = {2,7,11,15};
int target = 9;
nums[1,2]
"""


def two_sum(nums, target):
    for x in range(len(nums)):
        for y in range(x+1, len(nums)):
            if nums[x] + nums[y] == target:
                return x, y


if __name__ == '__main__':
    # nums = (2, 7, 11, 15)
    nums = (3, 3)
    target = 6
    print(two_sum(nums, target))

