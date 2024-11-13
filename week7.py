"""
199. Binary Tree Right Side View
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
"""
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []
        
        right_view = []
        queue = [root]  # Initialize queue with root node
        
        while queue:
            level_length = len(queue)
            
            for i in range(level_length):
                # Pop the first node from the queue
                node = queue.pop(0)
                
                # If it's the last node in this level, add it to the result
                if i == level_length - 1:
                    right_view.append(node.val)
                
                # Add left and right children if they exist
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return right_view


"""
994. Rotting Oranges
"""
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # Get the grid dimensions
        m, n = len(grid), len(grid[0])
        
        # Initialize a queue and count fresh oranges
        queue = []
        fresh_count = 0
        
        # Populate the initial state of the queue with all rotten oranges
        # and count the fresh oranges.
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))  # Add rotten orange positions
                elif grid[i][j] == 1:
                    fresh_count += 1  # Count fresh oranges

        # If there are no fresh oranges, return 0 as there's nothing to rot
        if fresh_count == 0:
            return 0
        
        # Directions for 4-directional movement
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        minutes_passed = 0
        
        # Perform BFS from initially rotten oranges
        while queue:
            # Process all oranges that are rotten at the current minute
            new_rotten = []
            for i, j in queue:
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    # Check if adjacent cell has a fresh orange
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                        # Rotten the fresh orange
                        grid[ni][nj] = 2
                        fresh_count -= 1  # Decrease fresh orange count
                        new_rotten.append((ni, nj))  # Add to the queue for the next minute
            
            # If no new oranges rotted this round, break the loop
            if not new_rotten:
                break
            
            # Move to the next minute
            queue = new_rotten
            minutes_passed += 1
        
        # If there are still fresh oranges left, return -1
        return minutes_passed if fresh_count == 0 else -1

"""
210. Course Schedule II
"""
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # Create an adjacency list to represent the graph
        adj_list = [[] for _ in range(numCourses)]
        for dest, src in prerequisites:
            adj_list[src].append(dest)
        
        # State of each node: 0 = unvisited, 1 = visiting, 2 = visited
        state = [0] * numCourses
        order = []
        
        def dfs(course):
            if state[course] == 1:  # Cycle detected
                return False
            if state[course] == 2:  # Already processed
                return True
            
            # Mark this course as being visited
            state[course] = 1
            
            # Visit all the neighbors
            for neighbor in adj_list[course]:
                if not dfs(neighbor):
                    return False
            
            # Mark this course as processed and add to the order
            state[course] = 2
            order.append(course)
            return True
        
        # Perform DFS on each course
        for course in range(numCourses):
            if state[course] == 0:
                if not dfs(course):
                    return []  # Return empty if a cycle is detected
        
        # The order should be reversed to get the correct topological order
        return order[::-1]
