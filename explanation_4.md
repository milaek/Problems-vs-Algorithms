# Problem 4
## Dutch National Flag Problem
### Design Choices
I chose use two markers and a "mover" to allow for a sort in place with a single traversal.

### Time Complexity
This runs in a single traversal O(n) as requested. Only one iteration of the array is done, and the average case is actually less than a single traversal, due to the auto sorting of all ones as the sort continues.

### Space Complexity
This sorts in place. The space complexity is constant.