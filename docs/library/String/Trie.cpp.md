# Trie

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

namespace Trie {
    const int M = 31;
    struct Node {
        int ch[2];
        Node() {
            ch[0] = ch[1] = 0;
        }
    } nodes[N * 10]; // 注意节点数分析对

    int cntNode; // 初始化为 0
    int newNode() {
        ++ cntNode;
        nodes[cntNode] = Node();
        return cntNode;
    }

    void insert(int rt, int dep, int x) {
        if (dep == -1) return;
        if ((x >> dep) & 1) {
            if (!nodes[rt].ch[1]) {
                nodes[rt].ch[1] = newNode();
            }
            insert(nodes[rt].ch[1], dep - 1, x);
        } else {
            if (!nodes[rt].ch[0]) {
                nodes[rt].ch[0] = newNode();
            }
            insert(nodes[rt].ch[0], dep - 1, x);
        }
        return;
    }
};
using namespace Trie;

struct Trie {
    int cnt;
    struct Node {
        int ch[2];
        Node () {
            ch[0] = ch[1] = 0;
        }
    };
    vector<Node> nodes;

    int newNode() {
        nodes.push_back(Node());
        return ++cnt;
    }

    Trie() {
        nodes.resize(1);
        cnt = 0;
    };

    void insert(ll x) {
        int rt = 0;
        for (int i = 30;i>=0;i--) {
            int nxt;
            if ((x>>i)&1) {
                nxt = 1;
            } else {
                nxt = 0;
            }

            if (nodes[rt].ch[nxt] == -1) {
                nodes[rt].ch[nxt] = newNode();
            }

            rt = nodes[rt].ch[nxt];
        }
        return;
    }

    ll getMx(ll x) {
        int rt = 0;
        ll ans = 0;
        for (int i = 30;i>=0;i--) {
            int nxt;
            if ((x>>i)&1) {
                nxt = 0;
            } else {
                nxt = 1;
            }

            if (nodes[rt].ch[nxt] == -1) {
                if (nodes[rt].ch[nxt^1] == -1) {
                    return 0;
                } else {
                    rt = nodes[rt].ch[nxt^1];
                }
            } else {
                rt = nodes[rt].ch[nxt];
                ans = ans + (1<<i);
            }
        }
        return ans;
    }

    void init() {
        cnt = 0;
        nodes.clear();
        nodes.resize(1);
    }
};
```
