# Tarjan

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

// inde 数组存的是合并后的新点编号
// 记得补充 info 的合并函数 !!!
// 其实 info 的合并完全可以写在外部, 内部只实现一个缩点
// 默认建立正向边的啊
struct Tarjan {
    struct Info {
        Info() {

        }
    };
    int tot, idx;
    vector<int> dfn, low, s, inde;
    vector<vector<int>> e;
    vector<bool> vis;
    vector<Info> infos;
    void tarjan(int u, vector<vector<int>>& g) {
        dfn[u] = low[u] = ++idx;
        s.push_back(u);
        vis[u] = 1;
        for (auto v : g[u]) {
            if (!dfn[v]) {
                tarjan(v, g);
                low[u] = min(low[u], low[v]);
            } else if (vis[v]) {
                low[u] = min(low[u], dfn[v]);
            }
        }
        if (low[u] == dfn[u]) {
            tot ++;
            infos.push_back(Info());
            while (1) {
                inde[s.back()] = tot;
                // info merge

                if (s.back() == u) {
                    vis[s.back()] = 0;
                    s.pop_back();
                    break;
                }
                vis[s.back()] = 0;
                s.pop_back();
            }
        }
        return;
    }
    void init(vector<vector<int>>& g) {
        int n = g.size() - 1;
        idx = tot = 0;
        vector<int>().swap(dfn);
        dfn.resize(n + 1, 0);
        vector<int>().swap(low);
        low.resize(n + 1, 0);
        vector<int>().swap(inde);
        inde.resize(n + 1, 0);
        vector<bool>().swap(vis);
        vis.resize(n + 1, 0);
        vector<Info>().swap(infos);
        infos.resize(1, Info());
        vector<vector<int>>().swap(e);
        e.resize(n + 1);

        for (int i = 1;i<=n;i++) {
            if (!dfn[i]) {
                tarjan(i, g);
            }
        }
        
        for (int i = 1;i<=n;i++) {
            for (auto v : g[i]) {
                if (inde[v] == inde[i]) continue;
                e[inde[i]].push_back(inde[v]);
            }
        }
        return;
    }
} solver;
```
