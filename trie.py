
class Trie(object):
    def __init__(self):
        """Initialize the data structure here"""
        self.root = {}
        self.end = -1

    def insert(self, word):
        """
        Insert a word into the trie
        :param word: str
        """
        curNode = self.root
        for c in word:
            if c not in curNode:
                curNode[c] = {}
            curNode = curNode[c]
        curNode[self.end] = True

    def search(self, word):
        """
        search if the word is in the trie
        :param word:  str
        :return: bool
        """
        curNode = self.root
        for c in word:
            if c not in curNode:
                return False
            curNode = curNode[c]
        # not end
        if self.end not in curNode:
            return False
        return True

    def starts_with(self, prefix):
        """
        return if there is any word in the trie that starts with the given prefix
        :param prefix: str
        :return:bool
        """
        curNode = self.root
        for c in prefix:
            if c not in curNode:
                return False
            curNode = curNode[c]
        return True


if __name__ == '__main__':

    trie = Trie()

    trie.insert("something")
    trie.insert("somebody")
    trie.insert("somebody123")

    param_1 = trie.search("somebody")
    param_2 = trie.search("some")
    param_3 = trie.starts_with("some")

    print(param_1)
    print(param_2)
    print(param_3)