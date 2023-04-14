from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        n_len = len(nums)
        def find_pivot():
            end = n_len - 1
            if nums[0] < nums[end]:
                return 0, False
            else:
                start = 1
                while start <= end:
                    mid = (start + end) // 2
                    if nums[mid] == target:
                        return mid, True
                    elif nums[mid - 1] > nums[mid]:
                        return mid, False
                    elif nums[0] <= nums[mid - 1]:
                        start = mid + 1
                    else:
                        end = mid - 1
                    
        start, found = find_pivot()
        if found:
            return start
        end = start + n_len - 1
        while start <= end:
            mid = (start + end) // 2
            actual = mid % n_len
            if nums[actual] == target:
                return actual
            elif nums[actual] < target:
                start = mid + 1
            else:
                end = mid - 1
        return -1
                     
                
                
arr = [3,5,1]
target = 6
print(Solution().search(arr, target))
print(Solution().search(arr, 3))