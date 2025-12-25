# Complex3

```cpp
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

ll qpow(ll base,ll k,ll mod) {
    if (base == 0) return 0;
    ll res = 1;
    base %= mod; base = (base + mod) % mod;
    k %= (mod - 1); k = (k + mod - 1) % (mod - 1);
    while (k) {
        if (k & 1) {
            res *= base; res %= mod;
        }
        k >>= 1;
        base *= base; base %= mod;
    }
    return res;
}

#define MMOD(x) ((x % MOD + MOD) % MOD)
struct Complex3 {
    ll x, y;
    Complex3(ll X_ = 0, ll Y_ = 0) {
        x = X_, y = Y_;
    }
    Complex3 operator+(const Complex3& z) const {
        return {MMOD(x + z.x), MMOD(y + z.y)};
    }
    Complex3 operator-(const Complex3& z) const {
        return {MMOD(x - z.x), MMOD(y - z.y)};
    }
    Complex3 operator*(const Complex3& z) const {
        ll a = x, b = y, c = z.x, d = z.y;
        return {MMOD(a*c%MOD - b*d%MOD), MMOD(a*d%MOD + b*c%MOD - b*d%MOD)};
    }
    Complex3 inv() const {
        ll a = x, b = y;
        ll n = a*a - a*b + b*b;
        n = MMOD(n);
        n = qpow(n, MOD - 2, MOD);
        return {MMOD((a - b) * n), MMOD((-b) * n)};
    }
    Complex3 operator/(const Complex3& z) const {
        return (*this) * z.inv();
    }
    bool operator==(const Complex3& z) const {
        return x == z.x && y == z.y;
    }
    Complex3 operator*(const ll& z) const {
        return Complex3(MMOD(x * z), MMOD(y * z));
    }
};
using Z = Complex3;
```
