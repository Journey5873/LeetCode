class Solution(object):
    def intToRoman(self, num):
        ones = {1:"I", 2:"II", 3:"III", 4:"IV", 5:"V",
                6:"VI", 7:"VII", 8:"VIII", 9:"IX"}
        tens = {10:"X", 20:"XX", 30:"XXX", 40:"XL", 50:"L", 
                60:"LX", 70:"LXX", 80:"LXXX", 90:"XC"}
        hundreds = {100:"C", 200:"CC", 300:"CCC", 400:"CD",
                   500:"D", 600:"DC", 700:"DCC", 800:"DCCC",
                   900:"CM"}
        thousands = {1000: "M", 2000:"MM", 3000:"MMM"}
        
        roman = ""
        if (num//1000)*1000 != 0:
            roman += thousands[(num//1000)*1000]
        if (num//100)%10 * 100 != 0:
            roman += hundreds[(num//100)%10 * 100]
        if (num//10)%10 * 10 != 0:
            roman += tens[(num//10)%10 * 10]
        if num%10 != 0:
            roman += ones[num%10]
        return roman