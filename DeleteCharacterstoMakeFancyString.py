class Solution:
    def makeFancyString(self, s: str) -> str:
        flag = 1
        prev = s[0]
        newString=""
        newString+=prev
        for i in range(1, len(s)): #aaba, last index 3
            if s[i] == prev:
                flag +=1
            else:
                prev = s[i]
                flag = 1
            if flag < 3:
                newString+=s[i]
        return newString



            

