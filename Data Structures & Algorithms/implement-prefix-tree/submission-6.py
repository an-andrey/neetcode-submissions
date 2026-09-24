class PrefixTreeNode: 
    def __init__(self, char: str, isTerminal: bool = False, children: dict[PrefixTreeNode] | None = None):
        self.char = char
        self.isTerminal = isTerminal
        self.children = children

class PrefixTree:
    def __init__(self):
        self.root = PrefixTreeNode("")

    def insert(self, word: str) -> None:
        ptr = self.root
        for i in range(len(word)):
            char = word[i]
            
            if ptr.children and ptr.children.get(char, 0): 
                ptr = ptr.children[char]
            
            else: 
                if ptr.children:
                    ptr.children[char] = PrefixTreeNode(char=char)
                else: 
                    ptr.children = {char: PrefixTreeNode(char=char)}
                ptr = ptr.children[char]    

        ptr.isTerminal = True

    def search(self, word: str) -> bool:
        ptr = self.root

        for i in range(len(word)):
            char = word[i]
            
            if ptr.children and ptr.children.get(char, 0): 
                ptr = ptr.children[char]
            
            else: 
                return False
        
        return ptr.isTerminal
        

    def startsWith(self, prefix: str) -> bool:
        ptr = self.root 

        for i in range(len(prefix)):
            char = prefix[i]
            
            if ptr.children and ptr.children.get(char, 0): 
                ptr = ptr.children[char]
            
            else: 
                return False

        return (ptr.isTerminal or ptr.children is not None)