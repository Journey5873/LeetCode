class Solution(object):
    def letterCombinations(self, digits):
        digitsList = list(digits)
        dic = {"":"", "2":"abc", "3":"def", "4":"ghi", "5": "jkl", 
               "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        
        if not digitsList:
            return []
        
        result = []

        def dfs(currentCombination, nextDigit):
            if not nextDigit:
                result.append(currentCombination)
                return 
            
            currentDigit = nextDigit[0]
            letters = dic[currentDigit]

            for letter in letters:
                dfs(currentCombination + letter, nextDigit[1:])

        dfs("", digitsList)
        
        return result