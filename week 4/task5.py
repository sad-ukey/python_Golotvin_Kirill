def search_range(nums, target):
    def find_start(nums, target):
        left, right = 0, len(nums) - 1
        start_index = -1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                start_index = mid
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return start_index

    def find_end(nums, target):
        left, right = 0, len(nums) - 1
        end_index = -1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                end_index = mid
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return end_index

    start = find_start(nums, target)
    end = find_end(nums, target)

    return [start, end]


# Примеры

print(search_range([5, 7, 7, 8, 8, 10], 8))
print(search_range([5, 7, 7, 8, 8, 10], 6))
print(search_range([], 0))
