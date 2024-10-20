def three_sum_closest(nums, target):
    nums.sort()  # Сортируем массив
    closest_sum = float("inf")

    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            if current_sum == target:
                return current_sum
            if abs(current_sum - target) < abs(closest_sum - target):
                closest_sum = current_sum
            if current_sum < target:
                left += 1
            else:
                right -= 1
    return closest_sum


# Примеры

print(three_sum_closest([-1, 2, 1, -4], 1))
print(three_sum_closest([0, 0, 0], 1))
