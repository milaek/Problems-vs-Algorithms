# Problem 3
## Rearrange Array Elements
### Design Choices
I chose to use a Max Heap data structure to sort and then pull the highest values from the array due to the efficient runtime and focus on ease of accessing the largest value.

### Time Complexity
As requested, the time complexity is O(n log n). Since I chose to use a Max Heap, this means that the runtimes adhere to the standards of the structure.
The original full transition of the given array into a heap must call the "heapify" function n number of times.
Each call of this heapify runs at the standard O(log n), which makes the overall runtime for the build O(n log n)
From there we simply pull out the values one by one, each time needing to run another "heapify" to re balance the tree.
These will all add more O(log n)'s, which at this point are non dominant and can be simplified from the equation, as can all constant time pieces.
This leaves us with the O(n log n) time complexity 

### Space Complexity
The space complexity is O(n) due to the recursive nature of heapsort.