class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        y = str(x)
        while len(y)>=2 and y[len(y)-1] == "0":
            y=y[:len(y)-1]
        if len(y)>1:
            if y[0]=="-":
                y=y[1:]
                if 0-int(y[::-1]) > -1*(2**31):
                    return 0-int(y[::-1])
                else:
                    return 0
            else:
                if int(y[::-1]) < (2**31) - 1:
                    return int(y[::-1])
                else:
                    return 0
        else:
            return int(y)
        