class PrefixTree:

    def __init__(self):
        self.root = TrieNode(None)

    def insert(self, word: str) -> None:
        current = self.root
        for symb in word: 
        
            if(symb in current.children):
                current = current.children[symb]
            else:
                new = TrieNode(symb)
                current.children[symb] = new
                current = current.children[symb]
        current.isEnd=True
                    



    def search(self, word: str) -> bool:
        current = self.root
        for symb in word: 
            
            if(symb in current.children):
                current = current.children[symb]
            else:
                return False
        
        return True and current.isEnd

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for symb in prefix: 
            
            if(symb in current.children):
                current = current.children[symb]
            else:
                return False
        return True
        
class TrieNode:
    def __init__(self, symbol):
        self.children = dict()
        self.isEnd = False
        self.symbol = symbol