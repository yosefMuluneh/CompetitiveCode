class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        letterComb = {
            2:["a","b","c"],
            3:["d","e","f"],
            4:["g","h","i"],
            5:["j","k","l"],
            6:["m","n","o"],
            7:["p","q","r","s"],
            8:["t","u","v"],
            9:["w","x","y","z"]
        }
        if len(digits)==0:
            return []
        elif "1" not in digits:
            if len(digits)==1:
                return letterComb[int(digits)]
            else:
                thetwo = self.calcu(letterComb[int(digits[0])],letterComb[int(digits[1])])
                if len(digits)==2:
                    return thetwo 
                else:
                    for i in range(2,len(digits)):
                        thetwo = self.calcu(thetwo,letterComb[int(digits[i])])
                    return thetwo
    def calcu(self, array,secArr):
        output=[]
        for j in range(len(array)):
            for i in range(len(secArr)):
                output.append(array[j]+secArr[i])
        return output
        