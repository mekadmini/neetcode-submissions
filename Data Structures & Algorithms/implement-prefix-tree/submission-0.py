class PrefixTree:

    def __init__(self):
        self.letters_list = {}
        self.end = False
        

    def insert(self, word: str) -> None:
        first_letter = word[0]
        if first_letter not in self.letters_list.keys():
            self.letters_list[first_letter] = PrefixTree()

        if not word[1:]:
            self.letters_list[first_letter].end = True
            return
        self.letters_list[first_letter].insert(word[1:])
        

    def search(self, word: str) -> bool:
        if not word:
            return self.end

        first_letter = word[0]

        if first_letter not in self.letters_list:
            return False

        return self.letters_list[first_letter].search(word[1:])
        

    def startsWith(self, prefix: str) -> bool:
        if not prefix:
            return True

        first_letter = prefix[0]

        if first_letter not in self.letters_list:
            return False

        return self.letters_list[first_letter].startsWith(prefix[1:])
        
        