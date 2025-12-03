# Kmp

```cpp
#include <bits/stdc++.h>
using namespace std;
#define DEBUG 1
using ll = long long;
using pii = pair<ll,ll>;
const ll N = 2000000;
const ll INF = 5e18;
const ll MOD = 1e9 + 7;

// nxt[i] 表示长度为 i 的前缀的最长 board
void kmp(string& s) {
    int n = s.size();
    vector<int> nxt(n + 1, 0);
    for (int i = 1;i<n;i++) {
        int j = nxt[i];
        while (j > 0 && s[j] != s[i]) {
            j = nxt[j];
        }
        if (s[j] == s[i]) j ++;
        nxt[i + 1] = j;
    }
}

```
