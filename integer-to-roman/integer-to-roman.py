class Solution:
    def intToRoman(self, num: int) -> str:
        dic = {
            0:'',
            1:'I',
            4:'IV',
            5:'V',
            9:'IX',
            10:'X',
            40:'XL',
            50:"L",
            90:"XC",
            100:"C",
            400:"CD",
            500:"D",
            900:"CM",
            1000:"M"
        }
        vals = [k for k in dic.keys()]
        vals = vals[::-1]
        print(vals)
        i = 0
        ans = ''
        while num != 0 and i!=13:

            toAdd = int(num/vals[i])
            num = num % vals[i]
            for k in range(toAdd):
                ans += dic[vals[i]]
            i+=1
        
        return ans