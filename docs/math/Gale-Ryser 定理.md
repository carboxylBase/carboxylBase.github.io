Gale-Ryser 定理用于解决这类问题:

假设我们有两个非负整数序列：行和向量：$R = (r_1, r_2, \dots, r_m)$ 列和向量：$C = (c_1, c_2, \dots, r_n)$ 我们想知道，是否存在一个 $m \times n$ 的 (0,1)-矩阵 $A$，使得第 $i$ 行的和恰好等于 $r_i$，第 $j$ 列的和恰好等于 $c_j$。

Gale-Ryser 定理指出：存在这样一个 (0,1)-矩阵的充要条件是：
+ $\sum_{i=1}^m r_i = \sum_{j=1}^n c_j$（总和相等）
+ 行和向量 $R$ 被列和向量 $C$ 的共轭序列（Conjugate sequence）$C^*$ 控制（Majorized）。即：$R \preceq C^*$
 
关键概念：共轭序列 $C^*$对于一个下降序列 $C$，其共轭序列 $C^*$ 的第 $i$ 个元素 $c^*_i$ 定义为：$C$ 中大于或等于 $i$ 的元素个数。

什么是“控制”关系 ($R \preceq C^*$)？对于两个长度均为 $k$ 的降序序列 $x$ 和 $y$，如果满足以下条件，则称 $x$ 被 $y$ 控制：

+ 对于所有 $1 \leq k < m$，有 $\sum_{i=1}^k r_i \leq \sum_{i=1}^k c^*_i$
+ 当 $k=m$ 时，有 $\sum_{i=1}^m r_i = \sum_{i=1}^m c^*_i$

相关例题:
[F - Conditional Mix](https://codeforces.com/contest/1740/problem/F)