class Solution(object):
    def countAndSay(self, n):
        if n == 1:
            return "1"

        say = ""
        for i in range(n, 0, -1):
            say = self.countAndSay(n-1)
            ret = ""
            i = 0
            while i < len(say):
                num = say[i]
                count = 1
                while i + count + 1 <= len(say) and say[i] == say[i+count]:
                    count += 1
                i += count
                ret += str(count) + num
            return ret
        return ret