
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        count = Counter()
        ans = 0

        for r in range(len(s)):
            count[s[r]] += 1

            while (r - l + 1) - count.most_common(1)[0][1] > k:
                count[s[l]] -= 1
                l += 1

            ans = max(ans, r - l + 1)

        return ans