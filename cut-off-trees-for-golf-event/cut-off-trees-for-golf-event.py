class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        rows = len(forest)
        cols = len(forest[0])
        def is_valid_move(row, col, matrix, visited):
            nonlocal rows, cols
            if new_row >= rows or new_row < 0 or new_col >= cols or new_col < 0: return False
            if (new_row, new_col) in visited: return False
            if matrix[row][col] == 0: return False
            return True
        trees = []
        for r in range(rows):
            for c in range(cols):
                if forest[r][c] > 1: trees.append(forest[r][c])
        trees.sort()
        index = 0
        steps = 0
        start_node = (0,0)
        found_flag = True
        while index < len(trees):
            start_row, start_col = start_node
            if not found_flag: break
            found_flag = False
            queue = deque([(start_row, start_col, 0)])
            visited = set([(start_row, start_col)])
            while queue:
                # look for current_tree
                r,c,s = queue.popleft()
                if forest[r][c] == trees[index]:
                    forest[r][c] = 1
                    index += 1
                    steps += s
                    found_flag = True
                    start_node = (r,c)
                    break
                for direction_row, direction_col in [(-1,0), (1,0), (0,1), (0,-1)]:
                    new_row, new_col = direction_row + r, direction_col + c
                    if is_valid_move(new_row, new_col, forest, visited):
                        queue.append((new_row, new_col, s+1))
                        visited.add((new_row, new_col))
        return steps if index >= len(trees) else -1
