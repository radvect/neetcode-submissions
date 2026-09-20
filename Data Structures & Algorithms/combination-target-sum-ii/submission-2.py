class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = sorted(candidates)
        # used = [False]*len(nums)
        path = []
        res = []

        def backtracking(start, remaining):
            nonlocal path
            if(remaining<0):
                return 
            if(remaining == 0):
                res.append(path.copy())
                return

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                # if(used[i] == True):
                #     continue
                # nums[i] = True
                path.append(nums[i])
                backtracking(i+1,remaining-nums[i])
                path.pop()
                # nums[i] = False

        backtracking(0, target)
        return res