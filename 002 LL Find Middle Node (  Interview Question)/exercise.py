# 002 LL Find Middle Node (  Interview Question)

"""
Instructions:
# Implement the find_middle_node method for the LinkedList class. 
# 
# Note: this LinkedList implementation does not have a length member variable.
# 
# If the linked list has an even number of nodes, return the first node of the 
# second half of the list.
# 
# Keep in mind the following requirements:The method should use a two-pointer 
# approach, where one pointer (slow) moves one node at a time and the other 
# pointer (fast) moves two nodes at a time.When the fast pointer reaches the end 
# of the list or has no next node, the slow pointer should be at the middle node 
# of the list.The method should return the middle node when the number of nodes 
# is odd or the first node of the second half of the list if the list has an 
# even number of nodes.The method should only traverse the linked list 
# once.&nbsp; In other words, you can only use one loop.
"""

# Write your solution below (your code will be imported as module 'exercise')
# ------------------------
# [Your code goes here]
# ------------------------

if __name__ != 'exercise':
    import sys
    sys.modules['exercise'] = __import__(__name__)
