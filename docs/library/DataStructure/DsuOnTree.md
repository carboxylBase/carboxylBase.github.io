# DsuOnTree

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

struct DsuOnTree {
	vector<vector<int>> g;
	int n,cntDfn;
	vector<int> dfn,L,R,son,siz;
	// 先填充 g
	void init() {
		cntDfn = 0;
		dfn.resize(n + 1,0);
		L.resize(n + 1,0);
		R.resize(n + 1,0);
		son.resize(n + 1,0);
		siz.resize(n + 1,0);
		g.resize(n + 1);
		return;
	}

	void dfsPre (int u,int f) {
		dfn[u] = ++cntDfn;
		L[u] = dfn[u];
		siz[u] = 1;
		for (auto v : g[u]) {
			if (v == f) continue;
			dfsPre(v,u);
			siz[u] += siz[v];
			if (!son[u] || siz[son[u]] < siz[v]) {
				son[u] = v;
			}
		}
		R[u] = cntDfn;
		return;
	};

	void add(int x) {
		return;
	}

	void del(int x) {
        return;
	}

	void dfs(int u,int f,bool keep) {
		for (auto v : g[u]) {
			if (v == f || v == son[u]) {
				continue;
			}
			dfs(v,u,0);
		}

		if (son[u]) dfs(son[u],u,1);
		
		for (auto v : g[u]) {
			if (v == f || v == son[u]) {
				continue;
			}
			for (int i = L[v];i<=R[v];i++) {
				// add();
			}
		}
		// add();

		if (!keep) {
			for (int i = L[u];i<=R[u];i++) {
				// del();
			}
		}
		return;
	};

};
```
