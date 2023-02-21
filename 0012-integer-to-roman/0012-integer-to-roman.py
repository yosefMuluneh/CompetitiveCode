class Solution(object):
    def intToRoman(self, x):
        ourRome = {
            1:"I",
            5:"V",
            10:"X",
            50:"L",
            100:"C",
            500:"D",
            1000:"M"
        }
        y = x
        num = []
        power = 0
        while y:
            num.append((y%10)*10**power )
            y = y // 10
            power += 1

        theRoma = ""
        for i in range(len(num)-1,-1,-1):
            if num[i] >= 900:
                if num[i] == 900:
                    theRoma += ourRome[100] + ourRome[1000]
                elif num[i] == 1000:
                    theRoma += ourRome[1000]
                else:
                    theRoma += (num[i]//1000)*ourRome[1000]
            elif num[i] >= 400:
                if num[i] == 400:
                    theRoma += ourRome[100]+ ourRome[500]
                elif num[i] == 500:
                    theRoma += ourRome[500]
                else:
                    theRoma += ourRome[500]+ (((num[i]-500)//100)*ourRome[100])
            elif num[i] >= 90:
                if num[i] == 90:
                    theRoma += ourRome[10]+ourRome[100]
                elif num[i] == 100:
                    theRoma += ourRome[100]
                else:
                    theRoma += (num[i]//100)*ourRome[100]
            elif num[i] >= 40:
                if num[i] == 40:
                    theRoma += ourRome[10]+ourRome[50]
                elif num[i] == 50:
                    theRoma += ourRome[50]
                else:
                    theRoma += ourRome[50] +(((num[i]-50)//10)*ourRome[10])
            elif num[i] >= 9:
                if num[i]== 9:
                    theRoma += ourRome[1]+ourRome[10]
                elif num[i] == 10:
                    theRoma += ourRome[10]
                else:
                    theRoma += (num[i]//10)*ourRome[10]
            else:

                if num[i] == 5:
                    theRoma += ourRome[5]
                elif num[i] >5:
                    theRoma += ourRome[5] +((num[i]-5)*ourRome[1])
                elif num[i] == 4:
                    theRoma += ourRome[1]+ourRome[5]
                else:
                    theRoma += num[i]*ourRome[1]
        return theRoma