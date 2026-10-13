class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        minimum = -1
        maximum = -1


        def search_in_array(left, right,find_first):
            nonlocal maximum
            nonlocal minimum
            #print(left, right)
            if left > right:
                return

            mid =  left + (right - left) // 2

            
            if nums[mid] == target:
                if find_first:
                    minimum = mid
                    search_in_array(left, mid - 1, True)
                else:
                    maximum = mid
                    search_in_array(mid + 1, right, False)

            elif nums[mid] > target:
                search_in_array(left, mid - 1, find_first)

            else:
                search_in_array(mid + 1, right, find_first)



        search_in_array(0,len(nums)-1, False)
        search_in_array(0,len(nums)-1, True)

        return [minimum, maximum]

        