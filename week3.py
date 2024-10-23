"""
1. Given the head of a singly linked list, return true if it is a palindrome or false otherwise.
"""
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        if not head:
            return True

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node

        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        
        return True
    
"""
2. Given the head of a linked list, remove the nth node from the end of the list and return its head.
"""
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        # Create a dummy node to handle edge cases like removing the first node
        dummy = ListNode(0)
        dummy.next = head
        
        # Initialize two pointers
        fast = slow = dummy
        
        # Move fast pointer n steps ahead
        for _ in range(n):
            fast = fast.next
        
        # Move both fast and slow pointers until fast reaches the end
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        # Skip the nth node
        slow.next = slow.next.next
        
        # Return the head of the modified list
        return dummy.next

"""
3. Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.
"""
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None (modify matrix in place)
        """
        m, n = len(matrix), len(matrix[0])
        first_row_zero = False
        first_col_zero = False
        
        # Check if the first row needs to be zeroed
        for j in range(n):
            if matrix[0][j] == 0:
                first_row_zero = True
                break
        
        # Check if the first column needs to be zeroed
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_zero = True
                break
        
        # Use first row and first column as markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        # Zero out cells based on markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        # Zero out the first row if necessary
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0
        
        # Zero out the first column if necessary
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0
