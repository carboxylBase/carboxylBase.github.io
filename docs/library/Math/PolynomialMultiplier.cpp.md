# PolynomialMultiplier

```cpp
#include <bits/stdc++.h>
using namespace std;
#define DEBUG 1
using ll = long long;
using pii = pair<int,int>;
using pll = pair<ll,ll>;
const ll N = 2000000;
const ll INF = 5e18;
const ll MOD = 1e9 + 7;

const int MAXN = 3 * 1e6 + 10, P = 998244353, G = 3, Gi = 332748118;
class PolynomialMultiplier {
public:
    char buf[1 << 21], *p1 = buf, *p2 = buf;
    int N, M, limit = 1, L;
    int r[MAXN];
    long long a[MAXN], b[MAXN];

    inline long long fastPow(long long a, long long k) {
        long long base = 1;
        while(k) {
            if(k & 1) base = (base * a) % P;
            a = (a * a) % P;
            k >>= 1;
        }
        return base % P;
    }

    inline void NTT(long long *A, int type) {
        for(int i = 0; i < limit; i++)
            if(i < r[i]) swap(A[i], A[r[i]]);
        for(int mid = 1; mid < limit; mid <<= 1) {
            long long Wn = fastPow(type == 1 ? G : Gi, (P - 1) / (mid << 1));
            for(int j = 0; j < limit; j += (mid << 1)) {
                long long w = 1;
                for(int k = 0; k < mid; k++, w = (w * Wn) % P) {
                    int x = A[j + k], y = w * A[j + k + mid] % P;
                    A[j + k] = (x + y) % P,
                    A[j + k + mid] = (x - y + P) % P;
                }
            }
        }
        if(type == -1) {
            long long inv = fastPow(limit, P - 2);
            for(int i = 0; i < limit; i++) A[i] = A[i] * inv % P;
        }
    }

public:
    PolynomialMultiplier() {
        // 初始化一些必要的变量
        for(int i = 0; i < MAXN; i++) r[i] = 0;
        for(int i = 0; i < MAXN; i++) a[i] = 0;
        for(int i = 0; i < MAXN; i++) b[i] = 0;
    }

    vector<int> multiply(vector<int> &A, vector<int> &B) {
        N = A.size() - 1;
        M = B.size() - 1;
        copy(A.begin(), A.end(), a);
        copy(B.begin(), B.end(), b);

        while(limit <= N + M) limit <<= 1, L++;
        for(int i = 0; i < limit; i++) r[i] = (r[i >> 1] >> 1) | ((i & 1) << (L - 1));

        NTT(a, 1);
        NTT(b, 1);
        for(int i = 0; i < limit; i++) a[i] = (a[i] * b[i]) % P;
        NTT(a, -1);

        vector<int> result(N + M + 1);
        for(int i = 0; i <= N + M; i++) result[i] = a[i] % P;

        return result;
    }
};


// 任意模数 NTT
ll mod_pow(ll a, ll e, ll mod) {
    ll r = 1;
    while (e) {
        if (e & 1) r = (__int128)r * a % mod;
        a = (__int128)a * a % mod;
        e >>= 1;
    }
    return r;
}
struct NTT {
    ll mod;
    ll root;
    NTT() {}
    NTT(ll m, ll g): mod(m), root(g) {}
    void ntt(vector<ll>& a, bool invert) {
        int n = a.size();
        int j = 0;
        for (int i = 1; i < n; i++) {
            int bit = n >> 1;
            for (; j & bit; bit >>= 1) j ^= bit;
            j ^= bit;
            if (i < j) swap(a[i], a[j]);
        }
        for (int len = 2; len <= n; len <<= 1) {
            ll wlen = mod_pow(root, (mod - 1) / len, mod);
            if (invert) wlen = mod_pow(wlen, mod - 2, mod);
            for (int i = 0; i < n; i += len) {
                ll w = 1;
                for (int j = 0; j < len/2; j++) {
                    ll u = a[i+j];
                    ll v = (ll)((__int128)a[i+j+len/2] * w % mod);
                    a[i+j] = u + v;
                    if (a[i+j] >= mod) a[i+j] -= mod;
                    a[i+j+len/2] = u - v;
                    if (a[i+j+len/2] < 0) a[i+j+len/2] += mod;
                    w = (ll)((__int128)w * wlen % mod);
                }
            }
        }
        if (invert) {
            ll inv_n = mod_pow(n, mod - 2, mod);
            for (int i = 0; i < n; i++) a[i] = (ll)((__int128)a[i] * inv_n % mod);
        }
    }
    vector<ll> multiply(const vector<ll>& a, const vector<ll>& b) {
        if (a.empty() || b.empty()) return {};
        int rlen = (int)a.size() + (int)b.size() - 1;
        int n = 1;
        while (n < rlen) n <<= 1;
        vector<ll> fa(n), fb(n);
        for (size_t i = 0; i < a.size(); i++) fa[i] = a[i] % mod;
        for (size_t i = 0; i < b.size(); i++) fb[i] = b[i] % mod;
        ntt(fa, false);
        ntt(fb, false);
        for (int i = 0; i < n; i++) fa[i] = (ll)((__int128)fa[i] * fb[i] % mod);
        ntt(fa, true);
        fa.resize(rlen);
        return fa;
    }
};

ll inv_mod(ll a, ll m) {
    ll b = m, x = 1, y = 0;
    while (b) {
        ll q = a / b;
        ll t = a - q * b; a = b; b = t;
        t = x - q * y; x = y; y = t;
    }
    x %= m;
    if (x < 0) x += m;
    return x;
}

vector<ll> convolution_mod(const vector<ll>& a, const vector<ll>& b, ll mod) {
    const ll m1 = 167772161; // 5 * 2^25 + 1, root = 3
    const ll m2 = 469762049; // 7 * 2^26 + 1, root = 3
    const ll m3 = 1224736769; // 73 * 2^24 + 1, root = 3
    static NTT ntt1(m1, 3), ntt2(m2, 3), ntt3(m3, 3);
    auto c1 = ntt1.multiply(a, b);
    auto c2 = ntt2.multiply(a, b);
    auto c3 = ntt3.multiply(a, b);
    int rlen = c1.size();
    vector<ll> res(rlen);
    ll m1_mod_m2 = m1 % m2;
    ll m1m2_mod_m3 = ( (__int128)m1 % m3) * (m2 % m3) % m3;
    ll inv_m1_mod_m2 = inv_mod(m1_mod_m2, m2);
    ll inv_m12_mod_m3 = inv_mod(m1m2_mod_m3, m3);
    for (int i = 0; i < rlen; i++) {
        ll x1 = c1[i];
        ll x2 = c2[i];
        ll x3 = c3[i];
        ll t1 = x1;
        ll t2 = ( (__int128)(x2 - t1) % m2 + m2 ) % m2;
        t2 = ( (__int128)t2 * inv_m1_mod_m2 ) % m2;
        ll t3 = ( (__int128)(x3 - (t1 + (__int128)t2 * m1) % m3) % m3 + m3 ) % m3;
        t3 = ( (__int128)t3 * inv_m12_mod_m3 ) % m3;
        __int128 value = (__int128)t1 + (__int128)t2 * m1 + (__int128)t3 * m1 * m2;
        ll finalv = (ll)(value % mod);
        if (finalv < 0) finalv += mod;
        res[i] = finalv;
    }
    return res;
}

void solve() {
    int n, m;
    ll p;
    cin >> n >> m >> p;
    vector<ll> A(n+1), B(m+1);
    for (int i = 0; i <= n; i++) cin >> A[i];
    for (int i = 0; i <= m; i++) cin >> B[i];
    auto C = convolution_mod(A, B, p);
    for (int i = 0; i <= n + m; i++) {
        if (i) cout << " ";
        cout << (C[i] % p + p) % p;
    }
    cout << "\n";
}

signed main() {
#if DEBUG
    freopen("input.txt", "r", stdin);
    auto start_time = chrono::steady_clock::now();
#else
    ios::sync_with_stdio(false);
#endif
    cin.tie(nullptr);

    int t = 1;

    while (t--) {
        solve();
    }

#if DEBUG
    auto end_time = chrono::steady_clock::now();
    auto diff = chrono::duration_cast<chrono::milliseconds>(end_time - start_time);
    cerr << "Time: " << diff.count() << " ms" << endl;
#endif

    return 0;
}

```
