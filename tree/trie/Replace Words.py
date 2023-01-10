class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.end_char = False

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()
    def insert(self,word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end_char = True

    def search(self,word):
        curr = self.root
        root_word = ""
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c] 
            root_word+=c
            if curr.end_char:
                return root_word
        return False                         

class Solution:    

    def replaceWords(self, dictionary: List[str], sentence: str) -> str:

        t = Trie()
        for word in dictionary:
            t.insert(word)
        new_sentence = ""
        for word in sentence.split(" "):
            root_word = t.search(word)
            if root_word == False:
                new_sentence= new_sentence + " "+ word
            else:
                new_sentence = new_sentence + " " + root_word

        return new_sentence.strip()
