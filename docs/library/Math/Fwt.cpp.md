# Fwt

```cpp
#include <bits/stdc++.h>
using namespace std;
#define DEBUG 1
#define endl '\n'
#define FUCK if (DEBUG) cout << "fuck" << endl;
using ll = long long;
using pii = pair<int,int>;
using i128 = __int128_t;
using pll = pair<ll,ll>;
const ll N = 2000000;
const ll INF = 1e18;
const ll MOD = 1e9 + 7;

// XOR Fast Walsh–Hadamard Transform (in-place).
// 功能：将向量 a 变换到 FWT 域并返回结果。
// 复杂度：O(n log n)，其中 n = a.size()，须为 2 的幂。
vector<ll> fwt(vector<ll>& a){
    int n = a.size();
    for(int len = 1; len < n; len <<= 1)
        for(int i = 0; i < n; i += len << 1)
            for(int j = 0; j < len; ++j){
                ll u = a[i + j];
                ll v = a[i + j + len];
                a[i + j] = u + v;
                a[i + j + len] = u - v;
            }
    return a;
}

vector<ll> FWT(vector<ll>& a) {
    vector<ll> b = a;
    fwt(b);
    for (int i = 0;i<b.size();i++) b[i]=b[i]*b[i];
    fwt(b);
    for (int i = 0;i<b.size();i++) b[i] /= b.size();
    return b;
}

void solve() {
    ll n, m, k; cin >> n >> m >> k;
    ll M = (1 << m);
    vector<ll> a(M, 0);
    for (int i = 1;i<n+1;i++) {
        string s; cin >> s;
        int x = 0;
        for (int j = 0;j<m;j++) {
            if (s[j] == 'A') {
                x += (1 << j);
            }
        }
        a[x] ++;
    }

    a = FWT(a);

    for (int i = 0;i<M;i++) {
        for (int j = 0;j<m;j++) {
            if (i & (1 << j)) {
                a[i] += a[i ^ (1 << j)];
            }
        }
    }

    for (int i = 0;i<m;i++) {
        for (int j = 0;j<M;j++) {
            if (j & (1 << i)) a[j] += a[j ^ (1 << i)];
        }
    }

    // for(int bit=0;bit<m;bit++)
    //     for(int mask=0;mask<M;mask++)
    //         if(mask&(1<<bit)) a[mask]+=a[mask^(1<<bit)];


    ll ans = 0;
    for (int i = 1;i<M;i++) {
        int S = ((M - 1) ^ i);
        ll z = 1ll * n * n - a[S];
        if (z >= 2 * k) ans ++;
    }

    cout << ans << endl;
    return;
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
    // cin >> t;

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
