class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        minimum = -1
        maximum = -1


        def search_minimum(left, right):
            nonlocal minimum
            if left > right:
                return

            mid =  left + (right - left) // 2

            
            if nums[mid] == target:
                minimum = mid
                search_minimum(left, mid - 1)
                
            elif nums[mid] > target:
                search_minimum(left, mid - 1)

            else:
                search_minimum(mid + 1, right)

        
        def search_maximum(left, right):
            nonlocal maximum
            #print(left, right)
            if left > right:
                return

            mid =  left + (right - left) // 2

            
            if nums[mid] == target:

                maximum = mid
                search_maximum(mid + 1, right)

            elif nums[mid] > target:
                search_maximum(left, mid - 1)

            else:
                search_maximum(mid + 1, right)


        search_minimum(0,len(nums)-1)
        search_maximum(0,len(nums)-1)

        return [minimum, maximum]

        