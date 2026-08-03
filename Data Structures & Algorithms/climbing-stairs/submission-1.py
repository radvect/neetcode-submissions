class Solution:
    def climbStairs(self, n: int) -> int:
        stairs_distance = [0]*n
        if(n == 1):
            return 1
        elif(n==2):
            return 2
        stairs_distance[0]=1

        stairs_distance[1] = 1

        for i in range(2, len(stairs_distance)):
            stairs_distance[i] = stairs_distance[i-1]+stairs_distance[i-2]
        
        print(stairs_distance)
        
        return (stairs_distance[-1]+stairs_distance[-2])
