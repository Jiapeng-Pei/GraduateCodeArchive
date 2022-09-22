# Mudule5 Problem Set
## __Jiapeng Pei S01435611__

### 1. $O(N\log(N))$
Suppose the size of input array is $N$. $T(1)=1$, since a single element is always sorted. 
$T(N)=3T(\frac{N}{3}) + F(N)$, where $F(N)$ denotes the time to perform a 3-way merge. 
The best compleity of $F(N)$ is $O(N)$, we could use a similar way to 2-way merge by adding an additional pointer. 
So, $T(N)=3T(\frac{N}{3}) + cN$, where c is a positive constant. Apply the Master Theorem, we have $a=3, b=3, k=1, p=0$, where $a=b^k, p>-1$. 
$$T(N)=O(N^{\log_3(3)}\log^1(N))=O(N\log(N))$$

### 2. $O(n^2)$
Suppose the size of input array is $n$. $T(1)=1$, since a single element is always sorted. In this case, $T(n)=T(n-1) + n$. $T(n-1)$ denotes the next subproblem to solve, and $n$ denotes the cost of partition. 
$$T(n)=T(n-2)+n+n-1=n+n-1+n-2+...+2+1=\frac{n*(n+1)}{2}$$
So the time complexity is $O(n^2)$.

### 3. Insertion Sort.
From the question, it is fair to assume that the input array in almost sorted with respect to transaction date. In this case, applying quick sort may result in worst case time-complexity. Since the leftmost element will be chosen as the pivot, the instance is partitioned into $1, k-1$ and the time complexity of quick sorting at this point is close to $O(n^2)$.

However, an almost-sorted array is the best case for insertion sort. In this case, each element only needs to move several positions and the complexity is close to $O(n)$. 

In conclusion, insertion sort is better than quick sort when it comes to an almost sorted array,

### 4. $O(k^2n)$
Let us merge this array step by step. 
	- Merge the $1^{st}$ and $2^{nd}$ array and takes $2n$ units time, since we need to traverse every elements in both array. Let's call the new longer array $L$.
	- Merge $L$ with the $3^{rd}$ array and takes $2n+n$ units time.
	- Merge $L$ with the $4^{th}$ array and takes $3n+n$ units time.
	- ....
	- Merge $L$ with $k^{th}$ array and takes $(k-1)n+n$ units time.
So, $$T(k)=n(2+3+4+...+k)=\frac{(k+2)(k-1)}{2}n=O(k^2n)$$

### 5. $O(nk\log(k))$
$T(k)$ denotes the time to merge $k$ arrays, and $k$ denotes the number of array. It takes the sum of both arrays' size to merge them. We have: 
$T(2)=2n$
$T(k)=2T(\frac{k}{2})+kn$
$T(k)=4T(\frac{k}{4})+2kn=2^mT(2)+mkn$, where $k=2^{m+1}, m=\log_2(k)-1$.
Substitude m back, we have:

$$T(k)=\frac{k}{2}*2n+\log_2(k)kn-kn=nk\log_2(k)$$
So the time complexity is $O(nk\log(k))$