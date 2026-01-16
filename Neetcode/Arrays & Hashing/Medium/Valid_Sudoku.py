# Completed: 01/13/2026

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        square_centers = [
            (1, 1),     (4, 1),     (7, 1),
            (1, 4),     (4, 4),     (7, 4),
            (1, 7),     (4, 7),     (7, 7)]
        square_edges = [
            (-1, -1),   (-1, 0),    (-1, +1),
            (0, -1),    (0,  0),    (0,  +1),
            (+1, -1),   (+1, 0),    (+1, +1),]
        
        for center in square_centers:
            current_square = []
            for edge in square_edges:
                item = board[center[0] + edge[0]][center[1] + edge[1]]
                if item == ".":
                    continue
                current_square.append(item)
                if current_square.count(item) > 1:
                    return False

        for column in [[board[x][i] for x in range(9)] for i in range(9)]:
            for item in column:
                if item == ".":
                    continue
                if column.count(item) > 1:
                    return False

        for row in board:
            for item in row:
                if item == ".":
                    continue
                if row.count(item) > 1:
                    return False

        return True