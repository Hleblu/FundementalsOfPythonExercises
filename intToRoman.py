class Solution(object):
    values = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}

    def intToRoman(self, num):
        result = []
        while num > 0:
            for key, value in self.values.items():
                while num >= value:
                    num -= value
                    result.append(key)
        return ''.join(result)


sol = Solution()
print(sol.intToRoman(3759))