class Solution:
    def romanToInt(self, s: str) -> int:
        
##ej IV = 4, bc I < V then ans = I - V = 4
# i ii iii iv v vi vii viii ix xx xxi xxii xxiii xxiiv the only real check we have to make is if our current numeral is
# a 1, ie I, if the next digit is greater than it the the sum is s[i+1]-s[i]
        numerals = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        sum=0
        i = 0
        while i < len(s): 
            if i+1 < len(s):
                if numerals[s[i]] < numerals[s[i + 1]]: 
                    sum+= numerals[s[i+1]] - numerals[s[i]]
                    i = i  + 2 
                else:
                    sum+=numerals[s[i]] 
                    i= i + 1 
            else:
                sum+=numerals[s[i]] 
                i = i + 1
        return sum
    #1000 + 900 + 90 + 4

def main():
     sl1 = Solution()
     print(sl1.romanToInt("III"))
main()