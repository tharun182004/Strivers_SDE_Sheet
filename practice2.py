class Solution(object):
    def generate_rows(self, row_num):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans=1
        arr=[]
        arr.append(ans)
        for col in range(1,row_num):
            ans=ans*(row_num-col)
            ans=ans//col
            arr.append(ans)
        return arr

    def generate(self, numrow):
        temp=[]
        for i in range(1,numrow+1):
            ans=self.generate_rows(i)
            temp.append(ans)
        return temp


sol=Solution()
a=sol.generate(6)
print(a)