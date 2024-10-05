def nextPermutation(nums):

    n = len(nums)

    i = n - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1
    if i < 0:
        nums.reverse()
        return
    j = n - 1
    while j > i and nums[j] <= nums[i]:
        j -= 1
    nums[i], nums[j] = nums[j], nums[i]

    left, right = i + 1, n - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1


nums = [1, 2, 3]
nextPermutation(nums)
print(nums)

nums = [3, 2, 1]
nextPermutation(nums)
print(nums)

nums = [1, 1, 5]
nextPermutation(nums)
print(nums)

nums = [5, 4, 7, 5, 3, 2]
nextPermutation(nums)
print(nums)