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

    def search(self, word: str, root: PrefixTreeNode | None = None) -> bool:
        ptr = root if root else self.root

        for i in range(len(word)):
            char = word[i]
            if ptr.children:
                if char == ".":
                    for child in ptr.children.values(): 
                        if self.search(word=word[i+1:], root=child) == True: 
                            return True
                    return False
                else: 
                    if ptr.children.get(char, 0):
                        ptr = ptr.children[char]
                    else: 
                        return False
            
            else: 
                return False
        
        return ptr.isTerminal
        
class WordDictionary:

    def __init__(self):
        self.tree = PrefixTree()

    def addWord(self, word: str) -> None:
        self.tree.insert(word)

    def search(self, word: str) -> bool:
        return self.tree.search(word)
