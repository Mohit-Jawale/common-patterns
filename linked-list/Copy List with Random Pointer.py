"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        old_to_new_table = {}
        future_table = collections.defaultdict(list)

        def set_random_tail(curr_old,curr_new):
            random_prev_new = old_to_new_table[curr_old]
            curr_new.random = random_prev_new
            return

        def set_random_head(curr_old,curr_new):
            old_to_new_table[curr_old] = curr_new
            return

        def set_future_node(curr_old,curr_new):
            future_table[curr_old].append(curr_new)  

        def set_random_past_tail(curr_old,curr_new):
            
            for i in future_table[curr_old]:
                past_new_node = i
                past_new_node.random = curr_new
            return
            
        def create_node(value):
            return Node(value)

        old_node = head
        prev = None
        new_head= None

        while old_node:
            curr_node = create_node(old_node.val)
            if not new_head:
                new_head = curr_node
            if prev:
                prev.next = curr_node

            set_random_head(old_node, curr_node)

            if old_node.random == None:
                curr_node.random = None
            elif old_node.random in  old_to_new_table:
                set_random_tail(old_node.random,curr_node)
            else:
                set_future_node(old_node.random,curr_node)    

            if old_node in future_table:
                set_random_past_tail(old_node,curr_node)    
                
            prev = curr_node
            old_node = old_node.next
           
        return new_head

            
                
                


            






           

        
           

           

