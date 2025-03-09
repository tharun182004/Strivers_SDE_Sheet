'''class Solution(object):
    def setZeroes(self, matrix):

        row = [0] * len(matrix)
        col = [0] * len(matrix[0])

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row[i] = 1
                    col[j] = 1
        for i in range(len(row)):
            if row[i] == 1:
                for j in range(len(matrix[0])):
                    matrix[i][j] = 0  # Set the entire row to zero

        # Step 3: Zero out the identified columns
        for j in range(len(col)):
            if col[j] == 1:
                for i in range(len(matrix)):
                    matrix[i][j] = 0

        print(matrix)



'''
for i in range(2):
    row=[1]*(i+1)
    print(row)

