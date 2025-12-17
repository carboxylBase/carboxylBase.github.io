# PAM

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

const ll N = 2000000;
const ll INF = 5e18;
const ll MOD = 1e9 + 7;


namespace PAM {
    string s;
    int n, fail[N], len[N], sum[N], ch[N][26], tot;

    int getFail(int x, int i) {
        while (i - len[x] - 1 < 0 || s[i - len[x] - 1] != s[i]) {
            x = fail[x];
        }
        return x;
    }

    // 先给 s 赋值
    void init() {
        tot = 1;
        n = s.size();
        fail[0] = 1, len[1] = -1;
        int cur = 0;
        for (int i = 0;i<n;i++) {
            int pos = getFail(cur, i);
            if (!ch[pos][s[i] - 'a']) {
                fail[++tot] = ch[getFail(fail[pos], i)][s[i]-'a'];
                ch[pos][s[i] - 'a'] = tot;
                len[tot] = len[pos] + 2;
                sum[tot] = sum[fail[tot]] + 1;
            }            
            cur = ch[pos][s[i] - 'a'];
        }
        
        return;
    }
};
using namespace PAM;
```
