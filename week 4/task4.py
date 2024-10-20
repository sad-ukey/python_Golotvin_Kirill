def next_permutation(nums):
    n = len(nums)
    i = n - 2

    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1
    if i >= 0:
        j = n - 1
        while nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
    nums[i + 1 :] = reversed(nums[i + 1 :])


# Примеры

nums1 = [1, 2, 3]
next_permutation(nums1)
print(nums1)

nums2 = [3, 2, 1]
next_permutation(nums2)
print(nums2)

nums3 = [1, 1, 5]
next_permutation(nums3)
print(nums3)
