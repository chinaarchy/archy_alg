from typing import List


def bsearch_left(nums: List[int], target: int) -> int:
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return low if nums[low] == target else -1


def bsearch_right(nums: List[int], target: int) -> int:
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] > target:
            high = mid - 1
        elif nums[mid] < target:
            low = mid + 1
        else:
            if (mid == len(nums) - 1) or (nums[mid + 1] != target):
                return mid
            else:
                low = mid + 1
    return -1


def bsearch_left_not_less(nums: List[int], target: int) -> int:
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] >= target:
            if mid == 0 or nums[mid - 1] < target:
                return mid
            else:
                high = mid - 1
        else:
            low = mid + 1
    return -1


def bsearch_right_not_greater(nums: List[int], target: int) -> int:
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] <= target:
            low = mid + 1
        else:
            high = mid - 1
    return high if high > 0 else -1


if __name__ == "__main__":
    import bisect

    a = [0, 1, 1, 2, 3, 4, 5, 6, 6, 7, 8, 8, 10, 10, 10]
    b = [11, 12, 12, 13, 14, 14, 15, 15]
    print(bisect.bisect_left(a, 10) == bsearch_left(a, 10))
    print(bisect.bisect_right(a, 10))
    print(bsearch_right(a, 10))
    print(bisect.bisect_right(a, 6) - 1 == bsearch_right(a, 6))
    print(bisect.bisect_right(b, 14) - 1 == bsearch_right(b, 14))

    print(bsearch_left_not_less(a, 11))
    print(bsearch_left_not_less(a, 9))
    print(bsearch_right_not_greater(b, 12))
    print(bsearch_right_not_greater(b, 10))
    print(bsearch_right_not_greater(b, 17))
