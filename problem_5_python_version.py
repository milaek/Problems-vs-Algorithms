# Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        # Initialize this node in the Trie
        self.is_word = False
        self.children = {}

    def insert(self, char):
        # Add a child node in this Trie
        self.children[char] = TrieNode()

    def suffixes(self, suffix=''):
        suffix_list = []
        for char in self.children:
            if self.children[char].is_word:
                suffix_list.append(char)
            recursive_suffixes = self.children[char].suffixes(suffix + char)
            for item in recursive_suffixes:
                suffix_list.append(char + item)
        return suffix_list


class Trie:
    def __init__(self):
        # Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        # Add a word to the Trie
        current_node = self.root
        for char in word:
            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                current_node.insert(char)
                current_node = current_node.children[char]
        current_node.is_word = True

    def find(self, prefix):
        # Find the Trie node that represents this prefix
        current_node = self.root
        for char in prefix:
            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                return None
        return current_node


#    TESTS    #
MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for new_word in wordList:
    MyTrie.insert(new_word)


def test_cases(prefix):
    print("For " + str(prefix))
    if prefix != "":
        prefix_node = MyTrie.find(prefix)
        if prefix_node:
            print(", ".join(prefix_node.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print("")
    print("That is all\n")


test_case_1 = "a"
test_cases(test_case_1)
# expected: nt, nthology, ntagonist, ntonym

test_case_2 = "b"
test_cases(test_case_2)
# expected: b not found

test_case_3 = "fun"
test_cases(test_case_3)
# expected: ction

test_case_4 = ""
test_cases(test_case_4)
# expected:

