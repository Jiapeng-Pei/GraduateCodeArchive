# Mudule4 Problem Set

## __Jiapeng Pei S01435611__


### For question 1-10, I will apply master Theorem to solve them.

### 1. $O(n^2)$
$T(n) = 3T(\frac{n}{2}) + n^2$, where $a=3, b=2, k=2, p=0$. We have $a<b^k, p>=0$ so that:
$T(n) = O(n^2\log^0(n)) = O(n^2)$ 

### 2. $O(n^2\log(n))$
$T(n) = 4T(\frac{n}{2}) + n^2$, where $a=4, b=2, k=2, p=0$. We have $a = b^k, p>-1$ so that:
$T(n) = O(n^{\log_2(4)}\log^1(n)) = O(n^2\log(n))$ 

### 3. $O(n^2)$
$T(n) = T(\frac{n}{2}) + n^2$, where $a=1, b=2, k=2, p=0$, We have $a<b^k, p>=0$ so that:
$T(n) = O(n^2\log^0(n)) = O(n^2)$ 

#### 4. $O(n^2)$
$T(n) = 16T(\frac{n}{4}) + n$, where $a=16, b=4, k=1, p=0$. We have $a>b^k$ so that:
$T(n) = O(n^{\log_4(16)}) = O(n^2)$

#### 5. $O(n\log^2(n))$
$T(n) = 2T(\frac{n}{2}) + n\log(n)$, where $a=2, b=2, k=1, p=1$. We have $a=b^k, p>-1$ so that:
$T(n) = O(n^{\log_2(2)}\log^{1+1}(n)) = O(n\log^2(n))$

#### 6. $O(n\log(\log(n)))$
$T(n) = 2T(\frac{n}{2}) + n\log^{-1}(n)$, where $a=2, b=2, k=1, p=-1$. We have $a=b^k, p=-1$ so that:
$T(n) = O(n^{\log_2(2)}\log(\log(n))) = O(n\log(\log(n)))$

#### 7. $O(n^{0.51})$
$T(n) = 2T(\frac{n}{4}) + n^{0.51}$, where $a=2, b=4, k=0.51, p=0$. We have $a<b^k, p>=0$ so that:
$T(n) = O(n^{0.51}\log^0(n)) = O(n^{0.51})$

#### 8. $O(n^2\log(n))$
$T(n) = 6T(\frac{n}{3}) + n^2\log(n)$, where $a=6, b=3, k=2, p=1$. We have $a<b^k, p>=0$ so that:
$T(n) = O(n^2\log^{1}(n)) = O(n^2\log(n))$ 

### 9. $O(n^2)$
$T(n) = 7T(\frac{n}{3}) + n^2$, where $a=7, b=3, k=2, p=0$. We have $a<b^k, p>=0$ so that:
$T(n) = O(n^2\log^0(n)) = O(n^2)$ 

### 10. $O(\sqrt n)$
$T(n) = \sqrt2 T(\frac{n}{2}) + n^2$, where $a=\sqrt2, b=2, k=0, p=1$. We have $a>b^k$ so that:
$T(n) = O(n\log_2(\sqrt2)) = O(\sqrt n)$

### 11. $O(n)$
I assume that the range of $n$ is $[1, \infty)$.
$T(n) = 3T(\frac{n}{3}) + 1 = 9T(\frac{n}{9})+3+1 = 27T(\frac{n}{27}) + 9 +3+1$
$T(n) = 3^kT(\frac{n}{3^k})+3^{k-1}+3^{k-2}+...+3^0=3^kT(\frac{n}{3^k})+\frac{3^k-1}{2}$
let $3^k=n, k=\log_3(n)$, we have:
$T(n)=nT(1)+\frac{n-1}{2}=\frac{5n-1}{2}$, where $n \in [1, \infty)$.
So, $T(n) = O(n)$

#### 12. $O(n!)$
Since this question neither provide any information about $T(1)$, nor the range of $n$, I assume that the range of n is $[2, \infty)$
$T(n)=nT(n-1)=n(n-1)T(n-2) = n(n-1)(n-2)T(n-3)$
$T(n)=n(n-1)(n-2)...(4)(3)T(2)$
$T(n)=\frac{n!}{2}*150 = 75n!$, where $n \in [2, \infty)$.
So, $T(n)=O(n!)$

#### 13. $O(n\log(n))$
By observing the equation $T(n) = T(\frac{9n}{10}) + T(\frac{n}{10})+n$, we could find that it is similar to equation $T(n)=2T(\frac{n}{2})+n$ whose complexity is $O(n\log(n))$. They both split $T(n)$ into 2 subproblems whose space sum up to $n$ and have a $n$ cost. So it is fair to guess that $T(n)=O(n\log(n))$. In the following step, we bring this complexity back to the the equation.

$T(n)=kn\log(n)$, where k should be a positive number. 
$T(\frac{9}{10}n)=k\frac{9}{10}n\log(\frac{9}{10}n)=k\frac{9}{10}n(\log(\frac{9}{10})+\log(n))=k\frac{9}{10}n\log(\frac{9}{10})+k\frac{9}{10}n\log(n)$
$T(\frac{1}{10}n)=k\frac{1}{10}n\log(\frac{1}{10}n)=k\frac{1}{10}n(\log(\frac{1}{10})+\log(n))=k\frac{1}{10}n\log(\frac{1}{10})+k\frac{1}{10}n\log(n)$
let $A=\frac{9}{10}\log(\frac{9}{10})+\frac{1}{10}\log(\frac{1}{10})$, we have:
$T(\frac{9}{10}n)+T(\frac{1}{10}n)=kn\log(n)+kAn$
Since $T(n)=T(\frac{9}{10}n)+T(\frac{1}{10}n)+n$, we also have:
$kn\log(n)=kn\log(n)+kAn+n$, so $kA+1=0,k=-\frac{1}{A}\approx7.08$.

We can conclude that $T(n)=O(7.08\log(n))=O(n\log(n))$

#### 14. $O(n\log(n))$
By observing the equation $T(n)=T(an)+T((1-a)n)+n$, we could find that it is similar to equation $T(n)=2T(\frac{n}{2})+n$ whose complexity is $O(n\log(n))$. They both split $T(n)$ into 2 subproblems whose space sum up to $n$ and have a $n$ cost. So it is fair to guess that $T(n)=O(n\log(n))$. In the following step, we bring this complexity back to the the equation.

$T(n)=kn\log(n)$, where k should be a positive number. 
$T(an)=kan\log(an)=kan(\log(a)+\log(n))=kan\log(a)+kan\log(n)$
$T((1-a)n)=k(1-a)n\log((1-a)n)=k(1-a)n\log(1-a)+k(1-a)n\log(n)$
let $A=a\log(a)+(1-a)\log(1-a)$, we have:
$T(an)+T((1-a)n)=kn\log(n)+kAn$
Since $T(n)=T(an)+T((1-a)n)+n$, we also have:
$kn\log(n)=kn\log(n)+kAn+n$, so $kA+1=0,k=-\frac{1}{A}$.

Since $0<a<1, 0<1-a<1$, so $\log(a) < 0$ and $\log(1-a) < 0$. We know that $A$ is a negative number, so $-\frac{1}{A}$ makes k a positive number which confirms our conjecture. 

We can conclude that $T(n)=O(n\log(n))$.
