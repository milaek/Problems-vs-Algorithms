# Problem 2
## Search in a Rotated Sorted Array
### Design Choices
The main choice I had to make here was how to search through the array most efficiently.
The main roadblock was the Rotation and how to account for it.
Pretty quickly I realized that the Rotation didn't actually change much. A simple binary search would still work, it just needed a few more checkpoints.
Instead of simply checking if the number was lower or higher than the center, you had to check the beginning or the end as well, depending on how it related to the center point.
Though this is slightly less ideal than your standard binary search, it solved the problem the most cleanly.

### Time Complexity
As requested, this runs in O(log n) time. As stated, I chose to use a modified binary search, which has an O(log n) time complexity.
The added checks all run in constant time as they are simple comparisons, and as such can be simplified out of the equation.

### Space Complexity
The binary search happens in place. The space complexity is constant.