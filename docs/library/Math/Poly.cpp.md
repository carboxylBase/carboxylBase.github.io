# Poly

```cpp
/* 死亡回放
你的输入, 真的写对了吗?? (2025 ICPC 沈阳 M)
*/
#define DEBUG 1
#define FUCK cout << "fuck" << endl;
#if DEBUG
    #include "all.hpp"
#else
    #include <bits/stdc++.h>
#endif

using namespace std;
using ll = long long;
using pii = pair<int,int>;
using pll = pair<ll,ll>;
using db = long double;
using pdd = pair<db, db>;
using i128 = __int128_t;

const ll N = 2000000;
const ll INF = 5e18;
const ll MOD = 998244353;

/*
此模版来自 https://hourai.nanani-fan.club/poly-family/
感谢 哈尔滨工业大学-蓬莱人形 的分享
*/

namespace poly {
    ll qpow(ll base,ll k) {
        if (base == 0) return 0;
        ll res = 1;
        base %= MOD; base = (base + MOD) % MOD;
        k %= (MOD - 1); k = (k + MOD - 1) % (MOD - 1);
        while (k) {
            if (k & 1) {
                res *= base; res %= MOD;
            }
            k >>= 1;
            base *= base; base %= MOD;
        }
        return res;
    }
    ll inv(ll x) {
        return qpow(x, MOD - 2);
    }
    mt19937 MT;
    using Poly = vector<ll>;
    #define lg(x) ((x) == 0 ? -1 : __lg(x))
    #define Size(x) int(x.size())
    namespace NTT_ns {
    const long long G = 3, invG = inv(G);
    vector<int> rev;
    void NTT(ll* F, int len, int sgn) {
        rev.resize(len);
        for (int i = 1; i < len; ++i) {
        rev[i] = (rev[i >> 1] >> 1) | ((i & 1) * (len >> 1));
        if (i < rev[i]) swap(F[i], F[rev[i]]);
        }
        for (int tmp = 1; tmp < len; tmp <<= 1) {
        ll w1 = qpow(sgn ? G : invG,
            (MOD - 1) / (tmp << 1));
        for (int i = 0; i < len; i += tmp << 1){
            for(ll j = 0, w = 1; j < tmp; ++j,
                w = w * w1 % MOD) {
            ll x = F[i + j];
            ll y = F[i + j + tmp] * w % MOD;
            F[i + j] = (x + y) % MOD;
            F[i + j + tmp] = (x - y + MOD) % MOD;
            }
        }
        }
        if (sgn == 0) {
        ll inv_len = inv(len);
        for (int i = 0; i < len; ++i)
            F[i] = F[i] * inv_len % MOD;
        }
    }
    }
    using NTT_ns::NTT;
    Poly operator * (Poly F, Poly G) {
    int siz = Size(F) + Size(G) - 1;
    int len = 1 << (lg(siz - 1) + 1);
    if (siz <= 300) {
        Poly H(siz);
        for (int i = Size(F) - 1; ~i; --i)
        for (int j = Size(G) - 1; ~j; --j)
            H[i + j] =(H[i + j] + F[i] * G[j])%MOD;
        return H;
    }
    F.resize(len), G.resize(len);
    NTT(F.data(), len, 1),NTT(G.data(), len, 1);
    for (int i = 0; i < len; ++i)
        F[i] = F[i] * G[i] % MOD;
    NTT(F.data(), len, 0), F.resize(siz);
    return F;
    }
    Poly operator + (Poly F, Poly G) {
    int siz = max(Size(F), Size(G));
    F.resize(siz), G.resize(siz);
    for (int i = 0; i < siz; ++i)
        F[i] = (F[i] + G[i]) % MOD;
    return F;
    }
    Poly operator - (Poly F, Poly G) {
    int siz = max(Size(F), Size(G));
    F.resize(siz), G.resize(siz);
    for (int i = 0; i < siz; ++i)
        F[i] = (F[i] - G[i] + MOD) % MOD;
    return F;
    }
    Poly lsh(Poly F, int k) {
    F.resize(Size(F) + k);
    for (int i = Size(F) - 1; i >= k; --i)
        F[i] = F[i - k];
    for (int i = 0; i < k; ++i) F[i] = 0;
    return F;
    }
    Poly rsh(Poly F, int k) {
    int siz = Size(F) - k;
    for (int i = 0; i < siz;++i)F[i] = F[i + k];
    return F.resize(siz), F;
    }
    Poly cut(Poly F, int len) {
    return F.resize(len), F;
    }
    Poly der(Poly F) {
    int siz = Size(F) - 1;
    for (int i = 0; i < siz; ++i)
        F[i] = F[i + 1] * (i + 1) % MOD;
    return F.pop_back(), F;
    }
    Poly inte(Poly F) {
    F.emplace_back(0);
    for (int i = Size(F) - 1; ~i; --i)
        F[i] = F[i - 1] * inv(i) % MOD;
    return F[0] = 0, F;
    }
    Poly inv(Poly F) {
    int siz = Size(F); Poly G{inv(F[0])};
    for (int i = 2; (i >> 1) < siz; i <<= 1) {
        G= G + G - G * G * cut(F, i), G.resize(i);
    }
    return G.resize(siz), G;
    }
    Poly ln(Poly F) {
    return cut(inte(cut(der(F) * inv(F), Size(F))), Size(F));
    }
    Poly exp(Poly F) {
    int siz = Size(F); Poly G{1};
    for (int i = 2; (i >> 1) < siz; i <<= 1) {
        G = G * (Poly{1} - ln(cut(G, i)) + cut(F, i)), G.resize(i);
    }
    return G.resize(siz), G;
    }
};
using namespace poly;
```
