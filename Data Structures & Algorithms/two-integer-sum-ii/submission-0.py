class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        res = numbers[right]+numbers[left]
        while(res!=target):
            if(res>target):
                right-=1
            else:
                left+=1
            res = numbers[right]+numbers[left]
            print(res)
            print("left ", left)
            print("right ", right)

            
        return [left+1, right+1]