# Mudule6 Problem Set
## __Jiapeng Pei S01435611__

### 1. $9$
To perform quickselect, find a pivot(the left one), move all the smaller elements to the left of it and bigger elements to the right of it. Check whether the new index is our target, then move to left/right side or return the element. Following is intermediate steps:
- before start : $3, 17, -5, 4, 13, 8, 7, 6, 9$  left = 0, right=8
- round 1 end: $-5, 3, 9, 4, 13, 8, 7, 6, 17$  pivot index = 1 < 7, so left = 2, right = 8
- round 2 end: $-5, 3, 4, 8, 7, 6, 9, 17, 13$  pivot index = 6, which means $9$ is the $7^{th}$ smallest element.

### 2. 6
The size of the array is 5, and our target index is 2.
- before start : $9, 8, 6, 4, -100$  left = 0, right=4
- round 1 end: $-100, 8, 6, 4, 9$  pivot index = 4 > 2, so left = 0, right = 3
- round 2 end: $-100, 8, 6, 4, 9$  pivot index = 0 < 2, so left = 1, right = 3
- round 3 end: $-100, 4, 6, 8, 9$  pivot index = 3 > 2, so left = 1, right = 2
- round 3 end: $-100, 4, 6, 8, 9$  pivot index = 1 < 2, so left = 2, right = 2
- round 4 end: We found the median since left >= right. return $6$


### 3. $4, 5, 7, 9$
The characteristic of quickSelect determines that the selected pivot value must be in its right sorted position. Compare following arrays:
$3, 1, 2, 4, 5, 8, 7, 6, 9$
$1, 2, 3, 4, 5, 6, 7, 8, 9$
We can find that $4, 5, 7, 9$ are on their right positions. So they are possible pivot elements.

### 4.  $0, 1, 1, 1, 3$ 
- i = 0, random0 = 0:  $1, 2, 3, 4, 5$  
- i = 1, random1 = 1:  $1, 2, 3, 4, 5$ 
- i = 2, random2 = 1:  $1, 3, 2, 4, 5$ 
- i = 3, random3 = 1:  $1, 4, 2, 3, 5$  
- i = 4, random4 = 3:  $1, 4, 2, 5, 3$

So $0, 1, 1, 1, 3$ is a possible sequence.

### 5. 
