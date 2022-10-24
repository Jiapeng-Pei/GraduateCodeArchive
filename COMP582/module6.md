# Mudule6 Problem Set
## __Jiapeng Pei S01435611__

### 1. $9$

#### **Lomuto partition scheme**
For the partition part in quickSelect algorithm, I used the following scheme that is different from lecture's way:
```python
def partition(list, left, right, pivotIndex)
    pivotValue = list[pivotIndex]
    swap list[pivotIndex] and list[right] // Move pivot to end
    storeIndex = left
    for i from left to right − 1 do
        if list[i] < pivotValue then
            swap list[storeIndex] and list[i]
            increment storeI  ndex
    swap list[right] and list[storeIndex]  // Move pivot to its final place
    return storeIndex
```
This scheme is known as **Lomuto partition scheme** [Hoare's vs Lomuto partition scheme in QuickSort - GeeksforGeeks](https://www.geeksforgeeks.org/hoares-vs-lomuto-partition-scheme-quicksort/). So in question 1 and 2, it is possible that my intermediate steps are not the same as professor's intermediate steps, but I can ganrantee that the intermediate steps and result are right.

To perform quickselect, find a pivot(the left one), move all the smaller elements to the left of it and bigger elements to the right of it. Check whether the new index is our target, then move to left/right side or return the element. Following is intermediate steps:
- before start : $3, 17, -5, 4, 13, 8, 7, 6, 9$  left = 0, right=8
- round 1 end: $-5, 3, 9, 4, 13, 8, 7, 6, 17$  pivot index = 1 < 7, so left = 2, right = 8
- round 2 end: $-5, 3, 4, 8, 7, 6, 9, 17, 13$  pivot index = 6, which means $9$ is the $7^{th}$ smallest element.

#### **Professor's Algorithm**

Following is the process:
- start: $3, 17, -5, 4, 13, 8, 7, 6, 9$  ==>
- 1     : $3, -5, 17, 4, 13, 8, 7, 6, 9$  ==>
- 2     : $-5, 3, 17, 4, 13, 8, 7, 6, 9$  ==> 
- 3     : $-5, 3, 9, 4, 13, 8, 7, 6, 17$  ==>
- 4     : $-5, 3, 9, 4, 6, 8, 7, 13, 17$  ==> 
- 5     : $-5, 3, 7, 4, 6, 8, 9, 13, 17$, then we have pivot index = 6, which means 9 is the $7^{th}$ smallest element.

### 2. $6$

The size of the array is 5, and our target index is 2.
- before start : $9, 8, 6, 4, -100$  left = 0, right=4
- round 1 end: $-100, 8, 6, 4, 9$  pivot index = 4 > 2, so left = 0, right = 3
- round 2 end: $-100, 8, 6, 4, 9$  pivot index = 0 < 2, so left = 1, right = 3
- round 3 end: $-100, 4, 6, 8, 9$  pivot index = 3 > 2, so left = 1, right = 2
- round 3 end: $-100, 4, 6, 8, 9$  pivot index = 1 < 2, so left = 2, right = 2
- round 4 end: We found the median since left >= right. return $6$


### 3. $4, 5, 9$

The characteristic of quickSelect determines:
- The selected pivot value must be in its right sorted position. 
- The elements on the left of pivot element must be smaller than itself, and the elements on the right of pivot element must be bigger. 

Compare following arrays:
$3, 1, 2, 4, 5, 8, 7, 6, 9$
$1, 2, 3, 4, 5, 6, 7, 8, 9$
We can find that $4, 5, 7, 9$ are on their right positions. And for each element in $4, 5, 9$, all the elements on the left are smaller and all the elements on the right are bigger. 
So $4, 5, 9$ are possible pivot elements.


### 4.  $0, 1, 1, 1, 3$ 

- i = 0, random0 = 0:  $1, 2, 3, 4, 5$ 
- i = 1, random1 = 1:  $1, 2, 3, 4, 5$ 
- i = 2, random2 = 1:  $1, 3, 2, 4, 5$ 
- i = 3, random3 = 1:  $1, 4, 2, 3, 5$  
- i = 4, random4 = 3:  $1, 4, 2, 5, 3$

So $0, 1, 1, 1, 3$ is a possible sequence.


### 5. 
#### a. $27$
For the shuffle algorithm in this situation, the outer loop runs $N$ times. In each iteration, the inner loop choose an elemnt from all $N$ elements. So the total number of permutation is:
$$N*N*...*N=N^N=27$$

#### b. $6$
Here's how KFY shuffling algorithm works: traverse from the first element to the Nth element, and choose a random element from previously choosed elements ($i$ elements) and place it at the current position. So the number of permutations is:
$$1*2*3*...*N=N!=6$$

#### c. 
The difference between 2 permutations is $27-6=21$. 
Let suppose that there is no bias if we select a random number between $0$ to $N-1$.
Then, there must be a way to split these $21$ more permutations from a. evenly to $6$ permutations from b. such that the chances of each permutation are the same.
But $21/6=3{...}3$, which denotes that there is no such spliting way. And there exists at least 1 permutation which owns larger chance.
This contradicts with our assuption. 
So there is a bias for the fault algorithm.
