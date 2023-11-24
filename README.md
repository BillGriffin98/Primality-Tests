## General info
This is a collection of a few primality tests I created as a part of my final year dissertation on number theory. The programs are derived from theorems in pure mathematics that determine (either deterministically and probabilistically) if a given natural number is prime or composite. All programs were created in Python. 
	
## Definitions
1. $(a,n)$ notates the *greatest common divisor* between $a$ and $n$. 

2. For an integer $a$ and a prime number $p$ such that $(a, p) = 1$, the *Lagrange symbol*, denoted as $\left(\frac{a}{p}\right)$, is defined as follows:

$$\left(\frac{a}{p}\right) = 
\begin{cases}
    0 & \text{if } a \equiv 0 \pmod{p} \\
    1 & \text{if } a \text{ is a quadratic residue modulo } p \\
    -1 & \text{if } a \text{ is a quadratic non-residue modulo } p
\end{cases}$$


3. For an integer $a$ and an odd positive integer $n$, the *Jacobi symbol*, denoted as $\left(\frac{a}{n}\right)$, can be expressed in terms of the Legendre symbol as follows:
$$\left(\frac{a}{n}\right) =
\prod_{i} \left(\frac{a}{p_i}\right)^{e_i}$$
where the product is taken over the prime factors $p_i$ of $n$, and $e_i$ is the exponent of the prime factor $p_i$ in the prime factorization of $n$.

## Trial Division
For a given $n$:
1. Generate a list of primes up to $\sqrt{n}$ via the Sieve of Eratosthenes.
2. Divide $n$ by each of the list's elements.
3. If none of these divisions result in an integer, then $n$ must be prime.
	
## Fermat's Test
For a given $n$:
1. Pick a random base $1 < a < n$ and test if $(a,n) = 1$. If it fails, chose another random value for $a$.
2. Test if Fermat's Little Theorem holds: $$a^{n-1} \equiv 1 \pmod{n}$$
3. If not, then $n$ is composite.


## Miller-Rabin Test
For a given odd $n$:
1. Express $n$ in the form $n-1 = 2^{e}k$, where $e$ is an integer, $k$ is odd, and $a$ is a random such that $1 < a < n$.

2. Generate a Miller-Rabin sequence $\{a^k, a^{2k},...,a^{2^ek} \} \pmod{n}$

3. If the resulting sequence doesn't takes the form $$\{ 1,...\}\text{ and }\{...,-1,...\}$$ then $n$ is composite.


## Lucas Sequence Test
For a given odd $n$:
1. Find a parameter $D$ such as $(\frac{D}{n}) = -1$ from the sequence $\{5, -7, 9, -11,...\}$.

2. Set $P = 1$ and $Q = (1 - D)/4$, and check $(P,n) = (Q,n) = 1$ 

3. Generate the Lucas sequences defined as follows:

$$U_{n}(P,Q) = PU_{n-1}(P,Q) - Q_{n-2}(P,Q)\\
V_{n}(P,Q) = PV_{n-1}(P,Q) - V_{n-2}(P,Q)$$
with starting values $U_0 = 0, U_1 = 1, V_0 = 2, V_1 = P$.

4. Check the congruence relation $U_{n+1} \equiv 0 \pmod{n}$. If this fails, then $n$ is certainly composite.

## Euler-Jacobi Test
For a given $n$ and number of trials $t$:
1. Generate a random $a$ such that $(a,n) = 1$ 

2. Test if the following relation holds

$$\left(\frac{a}{n}\right) \equiv a^{\frac{n-1}{2}} \pmod{n}$$

3. If not, then $n$ is certainly composite

## Ballie-PSW Test
For a given $n$
1. Perform the Miller-Rabin test with 2 as the base. If $n$ fails, then it is composite 

2. Perform a Lucas test on $n$. If $n$ fails, then it is composite

3. If $n$ passes, it is most certainly prime.

It has been shown through exhasutive search that there exists no composite $n<25 \times 10^{9}$ that pass this test. 

## Lucas-Lehmer Test
For a given $n$
1. Generate $S_p$ from the following sequence 

$$S_p = S_{p-1}^2 - 2$$ 
where $S_1 = 4$

2. Test if $S_p \equiv 0\pmod{2^p - 1}$

3. If so, $2^p - 1$ is certainly prime.

This test has been responsible for detecting the 8 largest primes.
