# ST

```cpp
#include <bits/stdc++.h>
using namespace std;
#define DEBUG 1
#define FUCK if (DEBUG) cout << "fuck" << endl;
using ll = long long;
using pii = pair<int,int>;
using i128 = __int128_t;
using pll = pair<ll,ll>;
const ll N = 2000000;
const ll INF = 1e18;
const ll MOD = 1e9 + 7;

/*
使用前记得 init
*/
namespace ST {
    int lg[N];
    void init(int n) {
        lg[0] = 0, lg[1] = 0;
        for (int i = 2;i<=n;i++) {
            lg[i] = lg[i / 2] + 1;
        }
    }
    struct ST {
        struct Info {
            ll val;
            Info() {
                val = INF;
            }
            Info operator+(const Info& A) const {
                Info z;
                z.val = min(val, A.val);
                return z;
            }
        };
        vector<vector<Info>> f;
        void init(const vector<ll>& a) {
            int n = (int)a.size();
            if (n == 0) return;
            for (int i = 2; i <= n; ++i) lg[i] = lg[i >> 1] + 1;
            int K = lg[n];
            f.assign(K + 1, vector<Info>(n));
            for (int i = 0; i < n; ++i) f[0][i].val = a[i];
            for (int k = 1; k <= K; ++k)
                for (int i = 0; i + (1 << k) <= n; ++i)
                    f[k][i] = f[k - 1][i] + f[k - 1][i + (1 << (k - 1))];
        }
        Info query(int l, int r) {
            if (l > r) return Info();
            int len = r - l + 1;
            int k = lg[len];
            return f[k][l] + f[k][r - (1 << k) + 1];
        }
    };
}
```
