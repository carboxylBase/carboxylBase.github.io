# Manacher

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

struct Manacher {
    int cal(string& s) {
        string t;
        char z = '#';
        t.push_back(z); // 注意,一定填写一个 没出现过的字符
        for (auto v : s) {
            t.push_back(v); t.push_back(z);
        }
        int mid = 0, mr = 0;
        vector<int> p(t.size(), 0);
        for (int i = 1;i<t.size();i++) {
            if (mid <= i && i <= mr) {
                int j = 2 * mid - i;
                if (p[j] + i < mr) {
                    p[i] = p[j];
                    continue;
                }
                p[i] = mr - i;
                for (int j = p[i] + 1;;j++) {
                    if (i+j<t.size() && i-j>=0 && t[i+j] == t[i-j]) {

                    } else {
                        p[i] = j - 1;
                        mr = i + j - 1;
                        mid = i;
                        break;
                    }
                }
            } else {
                for (int j = 1;;j++) {
                    if (i+j<t.size() && i-j>=0 && t[i+j] == t[i-j]) {

                    } else {
                        p[i] = j - 1;
                        mr = i + j - 1;
                        mid = i;
                        break;
                    }
                }
            }
        }
        int ans = 0;
        for (int i = 0;i<t.size();i++) {
            if (i & 1) {
                ans = max(ans, p[i] / 2 * 2 + 1);
            } else {
                ans = max(ans, (p[i] + 1) / 2 * 2);
            }
        }
        return ans;
    }
};
```
