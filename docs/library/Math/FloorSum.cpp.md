# FloorSum

```cpp
#include <bits/stdc++.h>
using namespace std;
using i128 = __int128_t;
using ll = long long;

// floor((a * i + b) / m)
// i 从 0 到 n - 1
i128 floor_sum_i128(i128 n, i128 m, i128 a, i128 b){
    if(n<=0) return 0;
    i128 ans=0;
    if(a<0){ b += a*(n-1); a = -a; }
    if(b<0){ i128 k = (-b + m - 1) / m; b += k*m; ans -= k*n; }
    while(true){
        if(a>=m){ ans += (a/m) * (n*(n-1)/2); a %= m; }
        if(b>=m){ ans += (b/m) * n; b %= m; }
        i128 y = a*n + b;
        if(y < m) break;
        n = y / m;
        b = y % m;
        i128 tmp = m; m = a; a = tmp;
    }
    return ans;
}

i128 floor_sum_mod(i128 n, i128 m, i128 a, i128 b, i128 mod){
    if(n<=0) return 0;
    a%=m; b%=m;
    i128 ans=0;
    if(a<0){ b += a*(n-1); a = -a; }
    if(b<0){ i128 k = (-b + m - 1) / m; b += k*m; ans -= k*n; }
    while(true){
        if(a>=m){ ans += (a/m) * (n*(n-1)/2); a %= m; }
        if(b>=m){ ans += (b/m) * n; b %= m; }
        i128 y = a*n + b;
        if(y < m) break;
        n = y / m;
        b = y % m;
        i128 tmp = m; m = a; a = tmp;
    }
    ans %= mod;
    if(ans<0) ans += mod;
    return ans;
}
```
