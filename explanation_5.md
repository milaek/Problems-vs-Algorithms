# Problem 5
## Autocomplete with Tries
### Design Choices
This was a walk through. No design choices to be made.

### Time Complexity
In the trie, the most time complex task we have is traversing a prefix and finding all suffixes. This depends on the number and length of available words in the dictionary.
Therefore I would say that it comes down to a simplified O(nw) where n is depth and w is number of available words. This can be further simplified to
O(n).

### Space Complexity
As more words are added to the Trie the space needed grows. The Space complexity is linear, O(n)