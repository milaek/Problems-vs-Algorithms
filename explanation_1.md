# Problem 1
## Square Root of an Integer
### Design Choices
The main design choice here was in using the while loop to handle the equation for reducing the guess number.
I handled this much like a binary search, roughly halving the search number in each time I didn't have the correct square root.
The main difference was in my choice to not build an array of all of the possible numbers, and instead use math to calculate and hold the totals.
This choice saved space and processing time overall

### Time complexity
As requested, the time complexity falls within O(log n).
Since the while loop acts as a modified binary search of all numbers between zero and the passed number,
it will similarly run in O(log n) time. All other time factors are constant, which means they can be simplified from the equation.

### Space complexity
The space complexity is constant.  