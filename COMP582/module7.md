# Mudule4 Problem Set

## __Jiapeng Pei S01435611__

### 1. 
For each heap_insert operation, the complexity is $O(\log(N))$, where $N$ is the size of priority queue. In worst case, the time comsuption is:
$$T(N) = \log(1)+\log(2)+\log(3)+...+log(N-1)=\log((N-1)!) $$
Since for $N >= 1$, $(N-1)! <= N! <= N^N$, we have: $$T(N)<=\log(N^N)=O(N\log(N))$$
### 2. $12, 11, 4, 9, 10, 1, 3, 0, 2, 7$ 
To build a tree using build_heap algorithm, we keep inserting elements to the back of priority queue and swim them up.
- Input      : $4, 2, 7, 9, 12, 1, 3, 0, 10, 11$
- Round1   : $4$
- Round2   : $4, 2$ 
- Round3   : $7, 2, 4$
- Round4   : $9, 7, 4, 2$
- Round5   : $12, 9, 4, 2, 7$
- Round6   : $12, 9, 4, 2, 7, 1$
- Round7   : $12, 9, 4, 2, 7, 1, 3$
- Round8   : $12, 9, 4, 2, 7, 1, 3, 0$ 
- Round9   : $12, 10, 4, 9, 7, 1, 3, 0, 2$ 
- Round10: $12, 11, 4, 9, 10, 1, 3, 0, 2, 7$ 

### 3. $12, 11, 7, 10, 4, 1, 3, 0, 9, 2$ 
To build a priority queue using Floyd heapify algorithm, we start from the back of the array and keep calling sink function. In this way, we build valid subtree first and then the whole tree.
- Start        : $4, 2, 7, 9, 12, 1, 3, 0, 10, 11$
- Round1   : $4, 2, 7, 9, 12, 1, 3, 0, 10, 11$
- Round2   : $4, 2, 7, 9, 12, 1, 3, 0, 10, 11$
- Round3   : $4, 2, 7, 9, 12, 1, 3, 0, 10, 11$ 
- Round4   : $4, 2, 7, 9, 12, 1, 3, 0, 10, 11$ 
- Round5   : $4, 2, 7, 9, 12, 1, 3, 0, 10, 11$ 
- Round6   : $4, 2, 7, 9, 12, 1, 3, 0, 10, 11$ 
- Round7   : $4, 2, 7, 10, 12, 1, 3, 0, 9, 11$ 
- Round8   : $4, 2, 7, 10, 12, 1, 3, 0, 9, 11$ 
- Round9   : $4, 12, 7, 10, 11, 1, 3, 0, 9, 2$ 
- Round10: $12, 11, 7, 10, 4, 1, 3, 0, 9, 2$ 

#### 4. $11, 10, 4, 9, 7, 1, 3, 0, 2$
To delete the max element, we need to (1) Move the back of array to the front and reduce the size of array by 1. (2) Sink the front element.
- Start       : $12, 11, 4, 9, 10, 1, 3, 0, 2, 7$
- Step 1    : $7, 11, 4, 9, 10, 1, 3, 0, 2$
- Step 2    : $11, 10, 4, 9, 7, 1, 3, 0, 2$

#### 5. 
The **heapSort** fucntion is the answer.
```python
def sink(arr, n, i):
    largest = i  
 
    l = 2*i + 1
    r = 2*i + 2    
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]
        sink(arr, n, largest)

def heapSort(arr):
    n = len(arr)
    
    # 1. Build a maxheap.
    for i in range(n, -1, -1):
        sink(arr, n, i)

    for i in range(n-1, 0, -1):
        # 2. swap the largest element with the tail element
	    # 3. maintain the remaining heap a max heap.
        arr[i], arr[0] = arr[0], arr[i]  
        sink(arr, i, 0)
```

#### 6. $O(N\log(N)$
Suppose the input array has size $N$. It takes $O(N)$ in **Step 1.** to build a max heap. **Step 2** is a swap operation that takes $N*O(1)$ which is $O(N)$ in total. **Step 3** is a sink operation that takes (in worst case)$$T = \log(N-1)+\log(N-2)+...+log(2)+\log(1)=\log((N-1)!)$$
Same as question 1, the complexity for **Step 3** is $O(N\log(N))$.
So the overall complexity is $$O(N)+O(N)+O(N\log(N)) = O(N\log(N))$$

#### 7. 
Following is pseudocode:
```python
minPQ<int> right
maxPQ<int> left

def insert(val):
	if len(left) == 0:
		left.push(val)
		return
		
	if len(left) == len(right):
		if val <= right.top:
			left.push(val)
		else:
			left.push(right.top)
			right.pop()
			right.push(val)
	else:
		if val >= left.top:
			right.push(val)
		else:
			right.push(left.top)
			left.pop()
			left.push(val)

def show_lmedian(): 
	return left.top
```

Following is python implementation: 
```python
class intR(object):
    def __init__(self, val) -> None:
        self.val = val
        
    def __lt__(self, other):
        return self.val > other.val

right = PriorityQueue()
left = PriorityQueue()

def insert(self, val):
    if left.empty():
        left.put(intR(val))
        return

    rightTop = right.get()
    leftTop = left.get()

    if left.qsize() == right.qsize():
        if val <= rightTop:
            left.put(intR(val))
            left.put(leftTop)
            right.put(rightTop)
        else:
            left.put(intR(rightTop))
            left.put(leftTop)
            right.put(val)

    else:
        if val >= leftTop.val:
            right.put(val)
            right.put(rightTop)
            left.put(leftTop)

        else:
            right.put(leftTop.val)
            right.put(rightTop)
            left.put(intR(val))

def show_lmedian():
    ret = left.get()
    left.put(ret)
    return ret.val
```

