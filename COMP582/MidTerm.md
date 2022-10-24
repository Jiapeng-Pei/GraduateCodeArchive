# Midterm Exam

## Jiapeng Pei S01435611

### Quick Answer

1. $\log(N)$
2. $\log(N)$
3. $O(N\log^*(N))$
4. $O(n^2)$
5. $O(n^2)$
6. $O(n^2)$
7. $O(n)$
8. $O(n^2)$
9. $O(n\log(n))$
10. $O(n\log(n))$
11. These 2 complexities are essentially the same in the Big Oh sense.
12. $O(n^2)$
13. $O(n)$
14. $O(n)$
15. $\lfloor \frac{N}{2} \rfloor - 1$
16. $-27, 4, 0, -4, 12, 17, -100, -8, 42, 6404, 9$
17. $O(\log(n))$
18. $O(\log(n))$
19. $O(\log(L))$
20. $O(T_A) <= O(T_B)$

### Not-so-Quick Answers

1. $Fn$ is not an algorithm. Initially $i=0, j=2, i < j$ is true. Inside the while loop, variable $i, j$ increase at the same rate. Since $i < j$ is always true, this piece of code won't terminate or halt. Thus $Fn$ is not an algorithm.

2. Since $O(n^3\log^3(n)) > O(n^2\log^2(n)) > n^2$, $T(n)$ could be write as:
   $$
   T(n) = 3T(\frac{n}{2}) + O(n^3\log^3(n))
   $$

   By applying the Master Theorem, we have:
   $a=3, b=2, k=3, p=3$, where $a<b^k, p>=0$.
   So the overall complexity is:
   $$
   O(n^3\log^3(n))
   $$

3. 1. 

      ```python
      def quickSort(arr, left, right):
          if left >= right:
              return
          pivotVal = d(arr)
          for i in range(left, right + 1):
              if arr[i] == pivotVal:
                  exchange(arr, left, i)
                  break
          
          # qspart is the COMP 582 partitioning algorithm
          pivotIndex = qspart(arr, left, right)
          quickSort(arr, left, pivotIndex - 1)
          quickSort(arr, pivotIndex + 1, right)
      ```

   2. In my quickSort algorithm, it takes $O(n)$ to find the pivot index, $O(1)$ to call $d(S)$, perform the swapping and splitting into subintervals.

      So, $T(n)=T(\frac{n}{5}) + T(\frac{4n}{5})+O(n)+O(1)$. 

      We could ignore the $O(1)$ part and its time consumption could be written as:

      $T(n) = T(\frac{n}{5}) + T(\frac{4n}{5})+ cn$, where $c$ is a positive constant. 

      It is fair to guess that $T(n) = O(n\log(n))$, since $T(n)$ resembles the form of merge sort complexity. They both split a bigger problems to 2 smaller parts whose scales sum up to $n$ and cost $O(n)$. Then we could write $T(n)$ as:

      $T(n) = O(n\log(n)) = kn\log(n)$, and we need to prove that $k$ is a positive constant. 

      We have:

      $T(\frac{n}{5})=\frac{kn}{5}\log(n)+\frac{kn}{5}\log(\frac{1}{5})$

      $T(\frac{4n}{5})=\frac{4kn}{5}\log(n)+\frac{4kn}{5}\log(\frac{4}{5})$

      Combine with $T(n) = T(\frac{n}{5}) + T(\frac{4n}{5})+ cn$, we have:

      $kn\log(n) = kn\log(n)+\frac{kn}{5}\log(\frac{1}{5})+\frac{4kn}{5}\log(\frac{4}{5})+cn$

      $\frac{k}{5}\log(\frac{1}{5})+\frac{4k}{5}\log(\frac{4}{5})=-c$

      $k=\frac{-c}{\frac{1}{5}\log(\frac{1}{5})+\frac{4}{5}\log(\frac{4}{5})}$ 

      Since $-c < 0$, $\frac{1}{5}\log(\frac{1}{5})+\frac{4}{5}\log(\frac{4}{5}) < 0$, we can conclude that $k$ is a positive constant. So we have
      $$
      T(n) = O(n\log(n))
      $$

   3. Similar to question 3.2, the time consumption is:

      $T(n) = T(\frac{n}{5}) + T(\frac{4n}{5})+O(n)+O(\log(n))+O(1)$, since the only difference is that complexity of $d(S)$ increases from $O(1)$ to $O(\log(n))$. Since $O(\log(n)) <= O(n)$, $T(n)$ could be written as $$T(n) = T(\frac{n}{5}) + T(\frac{4n}{5})+ cn$$, which is the same as previous one. So the time complexity is the same as previous one and it is 
      $$
      O(n\log(n))
      $$

      

4. By applying the Master Theorem, the complexity of 

   $T_0(n)=2T_0(\frac{n}{2})+O(n^2)$ is $O(n^2)$. It is fair to guess that $T(n)$ has complexity of $O(n^2)$, since $T(n)$ and $T_0(n)$ share similar forms. 

   We could write $T(n)$ as $T(n)=T(\frac{3n}{4})+T(\frac{n}{4})+cn^2$, where c is a positive constant.

   From our guess,

   $T(n)=kn^2$, and we need to prove $k$ is a positive constant. We have:

   $T(\frac{3n}{4})=\frac{9}{16}kn^2$

   $T(\frac{n}{4})=\frac{1}{16}kn^2$

   Combine with $T(n)=T(\frac{3n}{4})+T(\frac{n}{4})+cn^2$, we have:

   $kn^2=\frac{9}{16}kn^2+\frac{1}{16}kn^2+cn^2$, 

   $k=\frac{8}{3}c$. 

   We can conclude that k is a positive constant and complexity is:
   $$
   T(n) = O(n^2)
   $$

5. $O(L\log(M))$

   ```python
   import heapq
   
   def largetsStreamElements(stream, m):
       minHeap = []
       for i in stream:
           heappq.heappush(minHeap, i)
           if len(minHeap) > m:
               heappq.heappop(minHeap)
   ```

   My algorithm perform $L$ heap push operations, and 

   $max(L - M, 0)$ (when $L<=M$, there is no need to pop) heap pop operations. 

   The worst case complexity of push and pop are both $\log(M)$, so the overall complexity is:
   $$
   L\log(M)+max(L-M,0)*\log(M) = O(L\log(M))
   $$

6. 

   1. $S_3, S_2, S_1, S_0$. In this case the number of operation is:

      $7+4+11+3+14+3=42$

   2. $S_0, S_1, S_2, S_3$. In this case the number of operation is:

      $3+3+6+4+10+7=33$

   3. $O(N\log(N))$

      ```python
      import heappq
      
      def findSmallestSequence(sets):
          index = len(sets)
          minHeap = []
          for i, s in enumerate(sets):
              heappq.heappush(minHeap, (s, i))
          while len(minHeap) > 1:
              s1, i1 = heappq.heappop(minHeap)
              s2, i2 = heappq.heappop(minHeap)
              print(f"{index} = bmerge({i1},{i2})")
              heappq.heappush(minHeap, (s1+s2, index))
              index += 1
      ```

      Suppose the size of input is $N$. It takes $O(N\log(N))$ to build the min heap. In each iteration of the while loop, the size of minheap reduces by $1$. So the while loop runs $N$ times. Each time we perform several 2 pop & 1 push operations which take $O(\log(N))$ in the worst case. So the overall complexity is: 
      $$
      O(N\log(N)) + N *3\log(N) = O(N\log(N))
      $$

7. $O(n), O(1)$

   ```python
   import math
   
   def findLargestTwo(arr):
       largest = -math.inf
       larger = -math.inf
       for i in arr:
           if i <= larger:
               continue
           larger = i
           if larger > largest:
               largest, larger = larger, largest
      	
       return (largest, larger)
   ```

   It is fair to assume that $L >= 2$. My implementation iterates all elements of array of size $N$. In each iteration, it takes $O(1)$ to find the 1st largest and 2nd largest elements up to current element. So the overall complexity is $O(n)$ to find the maximum, and $O(1)$ to get the 2nd largest from the returned tuple. 

   Obviously, $O(n), O(1) < O(n), O(n)$ in in lexicographic order. 



#### Pledge

**On my honor, I have neither given nor received any unauthorized aid on this exam.**

start time: 1:02 pm 10/17

end time: 3.59 pm 10/17

Jiapeng Pei