class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        left =0
        max_freq=0
        right =0
        ans =0
        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right],0)+1

            if freq[s[right]]>max_freq:
                max_freq=freq[s[right]]
            while (right-left)+1 - max_freq > k:
                freq[s[left]]-=1
                left+=1
            ans = max(ans,right-left+1)

        return ans
        

        


            
            


        