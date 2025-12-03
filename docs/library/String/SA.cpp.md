# SA

```cpp
#include <bits/stdc++.h>
using namespace std;
#define DEBUG 1
using ll = long long;
using pii = pair<ll,ll>;
const ll N = 2000000;
const ll INF = 5e18;
const ll MOD = 1e9 + 7;

struct SA {
    string s;
    int n;
    int sa[N],rk[N<<1],oldrk[N<<1];

    // 先输入 s 再 init
    void init() {
        n = s.size();
        for (int i = 1;i<=n;i++) {
            sa[i] = i; rk[i] = s[i-1];
        }

        for (int w = 1;w<n;w<<=1) {
            sort(sa + 1,sa + 1 + n,[this,w](int x,int y){
                return rk[x] == rk[y] ? rk[x + w] < rk[y + w] : rk[x] < rk[y];
            });
            memcpy(oldrk,rk,sizeof rk);

            for (int p = 0,i = 1;i<=n;i++) {
                if (oldrk[sa[i]] == oldrk[sa[i-1]] && 
                        oldrk[sa[i]+w] == oldrk[sa[i-1]+w]) {
                    rk[sa[i]] = p;
                } else {
                    rk[sa[i]] = ++p;
                }
            }
        }

        return;
    }
};
SA solver;
void solve() {
    cin >> solver.s;
    solver.init();

    for (int i = 0;i<solver.s.length();i++) {
        cout << solver.sa[i + 1] << ' ';
    }
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
