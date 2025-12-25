# Lca

```cpp
#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
const ll N = 2000000;

/*
O(1) LCA
先把 Graph 边练好,然后调用 Lca 类的 init 函数
然后就可以使用 lca(查祖先) 和 query(查距离) 了

注意边权不要爆 ll !
*/

struct Lca {
    vector<vector<int>> *g;
    vector<int> depth, first, euler;
    vector<ll> dist;
    vector<vector<int>> st;
    vector<int> lg;

    void init(vector<vector<int>>* graph, int root) {
        g = graph;
        euler.clear();
        depth.clear();
        dist.assign(g->size(), 0);
        first.assign(g->size(), -1);
        dfs(root, -1, 0, 0);
        build_st();
    }

    void dfs(int u, int p, int d, ll s) {
        first[u] = euler.size();
        euler.push_back(u);
        depth.push_back(d);
        dist[u] = s;
        for (int v : (*g)[u]) if (v != p) {
            dfs(v, u, d + 1, s + 1);
            euler.push_back(u);
            depth.push_back(d);
        }
    }

    void build_st() {
        int m = euler.size();
        lg.assign(m + 1, 0);
        for (int i = 2; i <= m; ++i) lg[i] = lg[i >> 1] + 1;
        int K = lg[m] + 1;
        st.assign(K, vector<int>(m));
        for (int i = 0; i < m; ++i) st[0][i] = i;
        for (int j = 1; (1 << j) <= m; ++j)
            for (int i = 0; i + (1 << j) <= m; ++i) {
                int a = st[j - 1][i], b = st[j - 1][i + (1 << (j - 1))];
                st[j][i] = depth[a] < depth[b] ? a : b;
            }
    }

    int lca(int u, int v) {
        int l = first[u], r = first[v];
        if (l > r) swap(l, r);
        int j = lg[r - l + 1];
        int a = st[j][l], b = st[j][r - (1 << j) + 1];
        return euler[ depth[a] < depth[b] ? a : b ];
    }

    int query(int u, int v) {
        int L = lca(u, v);
        return dist[u] + dist[v] - 2 * dist[L];
    }
};

// dep 跟 dist 不要搞混了谢谢喵
struct Lca {
	int M = 20;
	vector<vector<int>> fa;
	vector<int> dep;
	void init(vector<vector<int>>& g, int rt) {
		int n = g.size() - 1;
		fa.clear();
		fa.resize(n + 1, vector<int>(M, 0));
		dep.clear();
		dep.resize(n + 1, 0);
		dep[0] = 0;
		auto dfs = [&](auto&&self, int u, int f) -> void {
			for (auto v : g[u]) {
				if (v == f) continue;
				fa[v][0] = u;
				dep[v] = dep[u] + 1;
				self(self, v, u);
			}
		};
		dfs(dfs, rt, 0);
		for (int i = 1;i<M;i++) {
			for (int j = 1;j<n+1;j++) {
				fa[j][i] = fa[fa[j][i-1]][i-1];
			}
		}
		return;
	}

	int lca(int x, int y) {
		if (dep[x] < dep[y]) swap(x, y);
		for (int i = M-1;i>=0;i--) {
			if (dep[fa[x][i]] >= dep[y]) {
				x = fa[x][i];
			}
		}
		if (x == y) return x;
		for (int i=M-1;i>=0;i--) {
			if (fa[x][i] != fa[y][i]) {
				x = fa[x][i], y = fa[y][i];
			}
		}
		return fa[x][0];
	}

	int query(int x, int y) {
		int z = lca(x, y);
		return dep[x] + dep[y] - 2 * dep[z];
	}
} solver;
```
