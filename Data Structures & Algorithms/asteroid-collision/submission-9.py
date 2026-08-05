class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        

        for i in range(len(asteroids)):
            # print(st)
            if(len(st)==0):
                st.append(asteroids[i])
            else:
                if(st[-1]*asteroids[i]>0):
                    st.append(asteroids[i])
                    continue
                elif(abs(asteroids[i])==abs(st[-1]) and asteroids[i]<0 and st[-1]>0):
                    st.pop()
                    continue
                elif(asteroids[i]>0 and st[-1]<0):
                    st.append(asteroids[i])
                    continue

                while(len(st)!=0 and st[-1]>0 and asteroids[i]<0 and abs(asteroids[i])>abs(st[-1])):
                    st.pop()
                if(len(st)==0):
                    st.append(asteroids[i])
                    continue
                elif(abs(asteroids[i])==abs(st[-1]) and asteroids[i]<0 and st[-1]>0):
                    st.pop()
                    continue
                elif(asteroids[i]*st[-1]>0):
                    st.append(asteroids[i])
                elif(abs(asteroids[i])<=abs(st[-1])):
                    continue
                
                # if(abs(asteroids[i])<abs(st[-1])):
                #     continue
                # elif(abs(asteroids[i])==abs(st[-1])):
                #     st.pop()
                
        return st
