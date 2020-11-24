## Sociable number

It's a number that belongs to a sociable secuence. A ***sociable secuence*** $A=\{a_0,\ a_1,\ a_2,..,a_n\}$ of period $n$ is one in which each element $a_i$ is such that $s(a_i)=a_{i+1}$ and the last one $s(a_n)$ is equals to $a_0$ (forming a cycle). The $s(a_i)$ denotes the sum of the proper divisors of $a_i$.

A number in a sociable secuence of period $n = 1$ (a unique number $a$ in which $s(a) = a$) it's called **perfect number**. The one in a sociable secuence of period $n = 2$ it's called **amicable number**.

### Social numbers identification pseudocode (not verified)

1. Toma el primer número $a_0$
2. Calcula los factores propios de $a_0$, $s(a_0)$.
4. Si $s(a_0) = a_0$, insértalo en la lista de números perfectos. Entonces, vuelve al `paso 1` con el número siguiente de la secuencia.
3. Si no, entonces, compara la suma de factores propios de cada elemento siguiente de la secuencia con $s(a_0)$.
5. Si $s(a_0) = a_{i+1}$ y $s(a_{i+1}) = a_0$, insértalo en la lista de **amicable numbers**.
6. Si no, y si $s(a_0) = a_{i+1}$ y $s(a_{i+1}) \ne a_0$, se puede presuponer que es de periodo $n=3$. Registra $a_0$ y $a_{i+1}$ en la lista de números sociables de ese periodo.
7. Tomar el último elemento que haya tomado en esa lista, vuelve al paso 5 usado $a_0 = b_n$, donde $b_n$ es el último elemento de esa nueva lista.