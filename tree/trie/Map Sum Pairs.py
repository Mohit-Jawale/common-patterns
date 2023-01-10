class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.sum = {}
        self.end_char = False
class MapSum:

    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, key: str, val: int) -> None:
        curr = self.root
        for c in key:
            if c not in curr.children:
                curr.children[c] = TrieNode()

            curr = curr.children[c]
            if key not in curr.sum : 
                curr.sum[key] = val
            else:
                curr.sum[key]=val   
    
        curr.end_char =True      
        

    def sum(self, prefix: str) -> int:
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return 0
            curr = curr.children[c]
        return sum(curr.sum.values())     

        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
