# Wheel筛

```cpp
#include <bits/stdc++.h>
using namespace std;
#define DEBUG 1
using ll = long long;
using pii = pair<int,int>;
using i128 = __int128_t;
using pll = pair<ll,ll>;
const ll N = 2000000;
const ll INF = 5e18;
const ll MOD = 1e9 + 7;

/*
2025牛客多校期间从 wanna be free 处 cv 得到的板子
可以快速(1800ms)筛出 1e9 以内质数
调用时,需要指定 U 表示筛选的最大质数的大小,可以输入 1e9
然后 init ,之后从 1 开始, prime 数组会填充质数, 遍历到为 0 的位置就表示没有质数了
1e9 以内质数大概有 5e7 个!!
*/

namespace wheelSieve {
    using std::cin,std::cout;
    using std::max,std::memcpy;
    
    #define N 50847534
    #define block 510510
    #define block_size 15953
    #define M 7
    #define K 1959
    
    #define set(a, b) a[b >> 5] |= 1 << (b & 31)
    typedef unsigned int uint;
    typedef unsigned char uchar;
    
    uint prime[N + 7], pre_block[block_size + 7], cur_block[block_size + 7];
    uchar p[block + 7];
    int U;
    void init(){
        uint cnt = 0;
        p[0] = p[1] = true;
        set(pre_block, 0);
        set(pre_block, block);
        for ( uint i = 2; i <= block; ++i){
            if (!p[i]){
                prime[++cnt] = i;
                if (cnt <= M) set(pre_block, i);
            }
            for ( uint j = 1; j <= cnt && i * prime[j] <= block; ++j){
                uint t = i * prime[j];
                p[t] = true;
                if (j <= M) set(pre_block, t);
                if (i % prime[j] == 0) break;
            }
        }
        for ( uint i = 1, j = cnt; i < K; ++i){
            uint end = (i + 1) * block - 1, start = i * block;
            memcpy(cur_block, pre_block, sizeof(cur_block));
            for ( uint k = M + 1; prime[k] * prime[k] <= end; ++k){
                uint t1 = max((start - 1) / prime[k] + 1, prime[k]) * prime[k], t2 = prime[k] << 1;
                for ( uint l = (t1 & 1 ? t1 : t1 + prime[k]) - start; l < block; l += t2){
                    set(cur_block, l);
                }
            }
            for ( uint k = 0; k <= block_size; ++k){
                uint t1 = ~cur_block[k];
                while (t1){
                    uint t2 = __builtin_ctz(t1);
                    if ((k << 5) + t2 >= block) break;
                    prime[++j] = start + (k << 5) + t2;
                    if (j >= N||prime[j]>=U) return;
                    t1 -= t1 & ((~t1) + 1);
                }
            }
        }
    }
};
```
