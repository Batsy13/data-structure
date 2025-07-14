class Solution:
    def maximumLengthSubstring(self, s:str) -> int:
        L, R = 0,0
        _max = 1

        counter = {}

        counter[s[0]] = 1

        while R < len(s) - 1:
            R += 1
            if counter.get(s[R]):
                counter[s[R]] += 1
            else:
                counter[s[R]] = 1

            while counter[s[R]] == 3:
                counter[s[L]] -= 1
                L += 1
            _max = max(_max, R-L+1)
        return _max

string1 = "bcbbbcba"
string2 = "aaaa"

sol = Solution()

res1 = sol.maximumLengthSubstring(string1)
res2 = sol.maximumLengthSubstring(string2)

print(f"String: {string1} | max: {res1}")
print(f"String: {string2} | max: {res2}")