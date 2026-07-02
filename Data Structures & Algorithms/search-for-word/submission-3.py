class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def initialize(board):
            check_board = []
            for i in range(len(board)):
                board_i = []
                for j in range(len(board[i])):
                    board_i.append(False)
                check_board.append(board_i)
            return check_board

        def find(board, visited, i, j, word):
            if visited[i][j]:
                return False

            if board[i][j] != word[0]:
                return False

            if len(word) == 1:
                return True

            visited[i][j] = True

            if i + 1 < len(board) and find(board, visited, i+1, j, word[1:]):
                return True
            if i > 0 and find(board, visited, i-1, j, word[1:]):
                return True
            if j + 1 < len(board[0]) and find(board, visited, i, j+1, word[1:]):
                return True
            if j > 0 and find(board, visited, i, j-1, word[1:]):
                return True

            visited[i][j] = False
            return False
                    
        for i in range(len(board)):
            for j in range(len(board[i])):
                board_matrix = initialize(board)
                if find(board, board_matrix, i, j, word):
                    return True
        return False



        
        