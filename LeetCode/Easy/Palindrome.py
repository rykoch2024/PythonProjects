class Solution:
    def isPalindrome(self, x: int) -> bool:
        conv_x = str(x)
        if len(conv_x) <= 1:
            return True
        if conv_x[0] == conv_x[-1]:
            return self.isPalindrome(conv_x[1:-1])
        else:
            return False

test = Solution()

print(test.isPalindrome(121))