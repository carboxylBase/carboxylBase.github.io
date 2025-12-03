# ACAM

```cpp
#include "all.hpp"
using namespace std;
#define DEBUG 1
using ll = long long;
using pii = pair<ll,ll>;
const ll N = 2000000;
const ll INF = 5e18;
const ll MOD = 1e9 + 7;

/*
先插入所有模式串
然后 init 构建 fail 数组
*/
namespace ACAM {
    struct Node {
        int ch[26], fail, cnt, f;
        char c;
        Node() {
            fail = cnt = f = 0;
            memset(ch, 0, sizeof ch);
        }
    } nodes[N]; // 注意节点数分析对

    int cntNode; // 初始化为 0
    int newNode() {
        ++ cntNode;
        nodes[cntNode] = Node();
        return cntNode;
    }

    void insert(int rt, int dep, string& s) {
        if (dep == s.size()) {
            nodes[rt].cnt ++;
            return;
        }
        if (!nodes[rt].ch[s[dep] - 'a']) {
            nodes[rt].ch[s[dep] - 'a'] = newNode();
            nodes[cntNode].c = s[dep];
            nodes[cntNode].f = rt;
        }
        insert(nodes[rt].ch[s[dep] - 'a'], dep + 1, s);
        return;
    }

    void init() {
        queue<int> q;
        for (int i = 0;i<26;i++) {
            if (nodes[1].ch[i]) {
                nodes[nodes[1].ch[i]].fail = 1;
                q.push(nodes[1].ch[i]);
            } else {
                nodes[1].ch[i] = 1;
            }
        }
        while (!q.empty()) {
            int u = q.front(); q.pop();
            for (int i = 0;i<26;i++) {
                if (nodes[u].ch[i]) {
                    nodes[nodes[u].ch[i]].fail = nodes[nodes[u].fail].ch[i];
                    q.push(nodes[u].ch[i]);
                } else {
                    nodes[u].ch[i] = nodes[nodes[u].fail].ch[i];
                }
            }
        }
        return;
    }
};
using namespace ACAM;
```
