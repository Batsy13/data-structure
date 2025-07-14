class Solution:
    def reverseWords(self, s: str) -> str:
        result = ""
        l = 0
        r = 0 

        while r < len(s):
            if s[r] != " ":
                r += 1
            else:
                result += s[l:r+1][::-1]
                r += 1
                l = r
        
        result += " "
        result += s[l:r + 2][::-1]
        return result[1:]
    
sol = Solution()

string1 = "Let's take LeetCode contest"
string2 = "Mr Ding"

new_string1 = sol.reverseWords(string1)
new_string2 = sol.reverseWords(string2)

print(f"Original: '{string1}' -> Inverted: '{new_string1}' ")
print(f"Original: '{string2}' -> Inverted: '{new_string2}' ")