class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        for i in range((n + 1) // 2):
            for j in range(n // 2):

                temp = matrix[i][j]
                row, col = i, j

                # Every value returns to its starting position after 4 moves
                for _ in range(4):
                    new_row = col
                    new_col = n - 1 - row

                    # Put temp in the new position, and save
                    # the displaced value in temp
                    matrix[new_row][new_col], temp = (
                        temp,
                        matrix[new_row][new_col]
                    )

                    row, col = new_row, new_col