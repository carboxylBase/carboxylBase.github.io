# Lucas

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

ll qpow(ll base,ll k,ll mod) {
    ll res = 1;
    if (k < 0) {
        return qpow(qpow(base,-k,mod),mod-2,mod);
    }
    while (k) {
        if (k & 1) {
            res *= base; res %= mod;
        }
        k >>= 1;
        base *= base; base %= mod;
    }
    return res;
}

// cal 函数是用于调用的接口, C 函数是内部使用的!!!
struct Lucas {
    int p;
    vector<int> fact;
    vector<int> inv;
    void init(int P_) {
        p = P_;
        fact.resize(p);
        inv.resize(p);
        fact[0] = 1;
        for (int i = 1;i<p;i++) {
            fact[i] = 1ll * fact[i - 1] * i % p;
        }
        vector<ll> pre(p, 1), suf(p, 1);
        for (int i = 1;i<p;i++) {
            pre[i] = pre[i - 1] * fact[i] % p;
        }
        suf[p - 1] = p - 1;
        for (int i = p - 2;i>=1;i--) {
            suf[i] = suf[i + 1] * fact[i] % p;
        }
        ll base = qpow(pre.back(), p - 2, p);
        inv[0] = 1;
        for (int i = 1;i<p;i++) {
            if (i + 1 < p) {
                inv[i] = pre[i - 1] * suf[i + 1] % p;
            } else {
                inv[i] = pre[i - 1];
            }
            inv[i] = inv[i] * base % p;
        }
    }
    int C(int n, int m) {
        if (m > n) return 0;
        return 1ll * fact[n] * inv[n - m] % p * inv[m] % p;
    }
    int cal(int n, int m) {
        if (m > n) return 0;
        if (n < p && m < p) {
            return C(n, m);
        }
        return 1ll * cal(n / p, m / p) * C(n % p, m % p) % p;
    }
} solver;

// 这个 C 真的是接口了
struct ExLucas {
    ll mod = 1;
    vector<ll> p, e, pk, prod;
    void init(ll M) {
        mod = M;
        ll x = M;
        for (ll i = 2; i * i <= x; i++) if (x % i == 0) {
            ll cnt = 0, pw = 1;
            while (x % i == 0) { x /= i; cnt++; pw *= i; }
            p.push_back(i); e.push_back(cnt); pk.push_back(pw);
        }
        if (x > 1) { p.push_back(x); e.push_back(1); pk.push_back(x); }
        prod.resize(pk.size());
        for (size_t idx = 0; idx < pk.size(); ++idx) {
            ll P = p[idx], PK = pk[idx], pr = 1;
            for (ll i = 1; i <= PK; i++) if (i % P) pr = (i128)pr * i % PK;
            prod[idx] = pr;
        }
    }
    ll modpow(ll a, ll b, ll m) {
        ll r = 1 % m; 
        a %= m; 
        while (b) { 
            if (b & 1) r = (i128)r * a % m; 
            a = (i128)a * a % m; 
            b >>= 1; 
        } 
        return r;
    }
    ll exgcd(ll a, ll b, ll &x, ll &y) {
        if (b == 0) { x = 1; y = 0; return a; }
        ll x1, y1; ll g = exgcd(b, a % b, x1, y1);
        x = y1; y = x1 - (a / b) * y1; return g;
    }
    ll invmod(ll a, ll m) { ll x, y; ll g = exgcd((a % m + m) % m, m, x, y); return g == 1 ? (x % m + m) % m : -1; }
    ll vp(ll n, ll P) { ll cnt = 0; while (n) { n /= P; cnt += n; } return cnt; }
    ll fac_mod(ll n, ll idx) {
        ll P = p[idx], PK = pk[idx], PR = prod[idx];
        if (n == 0) return 1 % PK;
        ll res = modpow(PR, n / PK, PK);
        for (ll i = 1; i <= n % PK; i++) if (i % P) res = (i128)res * i % PK;
        return (i128)res * fac_mod(n / P, idx) % PK;
    }
    ll C_mod_pk(ll n, ll m, ll idx) {
        if (m < 0 || m > n) return 0;
        ll P = p[idx], PK = pk[idx], K = e[idx];
        ll cnt = vp(n, P) - vp(m, P) - vp(n - m, P);
        if (cnt >= K) return 0;
        ll a = fac_mod(n, idx);
        ll b = fac_mod(m, idx) * fac_mod(n - m, idx) % PK;
        ll ib = invmod(b, PK);
        ll res = (i128)a * ib % PK;
        res = (i128)res * modpow(P, cnt, PK) % PK;
        return res;
    }
    ll C(ll n, ll m) {
        if (m < 0 || m > n) return 0;
        int sz = pk.size();
        if (sz == 0) return 1 % mod;
        vector<ll> r(sz);
        for (int i = 0; i < sz; i++) r[i] = C_mod_pk(n, m, i);
        ll M = mod, x = 0;
        for (int i = 0; i < sz; i++) {
            ll mi = pk[i], ai = r[i];
            ll Mi = M / mi;
            ll ti = invmod(Mi % mi, mi);
            x = (x + (i128)ai * Mi % M * ti) % M;
        }
        return (x % M + M) % M;
    }
};
```
