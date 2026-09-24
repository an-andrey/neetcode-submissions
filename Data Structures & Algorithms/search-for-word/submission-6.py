class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def helper(i, j, pos_word, seen):
            if (i,j) in seen: 
                return False
            else: 
                seen.add((i,j))
            if board[i][j] == word[pos_word]: 
                if pos_word == len(word)-1: 
                    return True

                if j < len(board[0]) - 1: 
                    if helper(i, j+1, pos_word+1, seen): 
                        return True

                if i < len(board) - 1:
                    if helper(i+1, j, pos_word+1, seen): 
                        return True
                
                if i > 0: 
                    if helper(i-1, j, pos_word+1, seen): 
                        return True
                
                if j > 0: 
                    if helper(i, j-1, pos_word+1, seen): 
                        return True
            seen.remove((i,j))
            return False

        for i in range(len(board)): 
            for j in range(len(board[0])): 
                if helper(i, j, 0, set()): 
                    return True

        return False