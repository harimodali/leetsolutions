#Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

#A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

#Input: "23"
#Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

class Solution(object):
    digit_to_alpha = {'2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
            '0': ' '
    }
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        return_list = []
        if len(digits) == 0:
            return return_list
        cur = digits[0]
        post_string = self.letterCombinations(digits[1:])
        for i in self.digit_to_alpha.get(cur):
            if len(post_string) > 0:
                for string in post_string:
                    return_list.append(i + string)
            else:
                return_list.append(i)
        return return_list
