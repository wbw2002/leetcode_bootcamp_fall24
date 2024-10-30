"""
Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:

void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and returns it.
int peek() Returns the element at the front of the queue.
boolean empty() Returns true if the queue is empty, false otherwise.
"""
class MyQueue(object):

    def __init__(self):
        self.stack1 = []
        self.stack2 = []


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack1.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        if self.empty():
            return None
        
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
        

    def peek(self):
        """
        :rtype: int
        """
        if self.empty():
            return None
        
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        return not self.stack1 and not self.stack2
        

"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 10^5.
"""
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        count_stack = []
        string_stack = []
        current_string = ""
        k = 0
        
        for char in s:
            if char.isdigit():
                k = k * 10 + int(char)  # Handles multi-digit numbers for k
            elif char == '[':
                count_stack.append(k)
                string_stack.append(current_string)
                current_string = ""
                k = 0  # Reset k for the next encoded segment
            elif char == ']':
                repeat_count = count_stack.pop()
                decoded_part = current_string * repeat_count
                current_string = string_stack.pop() + decoded_part  # Append to previous segment
            else:
                current_string += char  # Accumulate characters for current segment
        
        return current_string


"""
On day 1, one person discovers a secret.

You are given an integer delay, which means that each person will share the secret with a new person every day, starting from delay days after discovering the secret. You are also given an integer forget, which means that each person will forget the secret forget days after discovering it. A person cannot share the secret on the same day they forgot it, or on any day afterwards.

Given an integer n, return the number of people who know the secret at the end of day n. Since the answer may be very large, return it modulo 10^9 + 7.
"""
class Solution(object):
    def peopleAwareOfSecret(self, n, delay, forget):
        """
        :type n: int
        :type delay: int
        :type forget: int
        :rtype: int
        """
        MOD = 10**9 + 7
        dp = [0] * (n + 1)
        dp[1] = 1
        
        for i in range(1, n + 1):
            if dp[i] > 0:
                start = i + delay
                end = i + forget
                for j in range(start, min(end, n + 1)):
                    dp[j] = (dp[j] + dp[i]) % MOD
        
        return sum(dp[n - forget + 1: n + 1]) % MOD