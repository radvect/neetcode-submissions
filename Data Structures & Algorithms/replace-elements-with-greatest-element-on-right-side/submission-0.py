class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]: 
        if(len(arr)==1):
            return [-1]
        curr_max = arr[-1]
        arr[-1] = -1
        for i in range(len(arr)-2, -1,-1):
            if(arr[i]>curr_max):
                buf = curr_max
                curr_max = arr[i]
                arr[i]=buf
            else:
                arr[i]=curr_max
        
        return arr


            

        