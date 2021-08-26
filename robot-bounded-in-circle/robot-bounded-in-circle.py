class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
            current_coords = start_coords = (0,0)
            directions = [0,1,2,3]  
                         # N,E,S,W
            direction = 0
            for char in instructions:
                if char == "G":
                    if direction == 0:  # go north
                        tmp_coords = current_coords
                        current_coords = tmp_coords[0], tmp_coords[1] + 1
                    elif direction == 1:  # go east
                        tmp_coords = current_coords
                        current_coords = tmp_coords[0]+1, tmp_coords[1]
                    elif direction == 2:  # go south
                        tmp_coords = current_coords
                        current_coords = tmp_coords[0], tmp_coords[1] - 1
                    elif direction == 3:  # go west
                        tmp_coords = current_coords
                        current_coords = tmp_coords[0]-1, tmp_coords[1]
                elif char == "L":
                    direction = directions[direction-1]
                elif char == "R":
                    direction = directions[direction-3]
            return current_coords == start_coords or direction != 0
