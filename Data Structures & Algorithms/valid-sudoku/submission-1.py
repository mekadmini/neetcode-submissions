class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows 
        for row in board:
            seen_numbers = set()
            for num in row:
                if num in ["1","2","3","4","5","6","7","8","9"]:
                    if num in seen_numbers:
                        print("rows")
                        return False
                    seen_numbers.add(num)
        
        # check columns
        for i in range(len(board[0])):
            seen_numbers = set()
            for row in board:
                num = row[i]
                if num in ["1","2","3","4","5","6","7","8","9"]:
                    if num in seen_numbers:
                        print("columns")
                        return False
                    seen_numbers.add(num)

        # check squares
        starting_points = [(i,j) for i in [0,3,6] for j in [0,3,6]]
        for i,j in starting_points:
            seen_numbers = set()
            for k in range(3):
                for l in range(3):
                    print(f"staring: {i}, {j}")
                    print(f"{i+k}, {j+l}")
                    if board[k+i][l+j] in seen_numbers and board[k+i][l+j] in  ["1","2","3","4","5","6","7","8","9"]:
                        print("squares")
                        return False
                    seen_numbers.add(board[k+i][l+j])
                    
        return True
        