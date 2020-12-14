# Problem 7
## HTTP Router Using a Trie
### Design Choices
This was a build along. No major design choices were made.

### Time Complexity
The time complexity of each action will be at average O(n) where n is the number of paths deep the item passed is working with,
be it an insert or find action within the Trie.

### Space Complexity
As the Trie gets items added to it, it will grow in size. Therefore the Space complexity is linear, O(n).