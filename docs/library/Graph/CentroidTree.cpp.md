# CentroidTree

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

// 传入一颗树, 返回对应的点分树, 已删去指向父亲的边!! 入度为 0 的就是根
vector<vector<int>> CentroidTree(vector<vector<int>>&g) {
	int n = g.size() - 1;
	vector<vector<int>> e(n + 1);
	vector<bool> bad(n + 1, 0);
	vector<int> siz(n + 1, 0);
	auto getCenter = [&](int u, int tot) -> int {
		int mn = n + 1, res;
		auto dfs = [&](auto&&self, int u, int f) -> void {
			int val = 1;
			siz[u] = 1;
			for (auto v : g[u]) {
				if (v == f || bad[v]) continue;
				self(self, v, u);
				siz[u] += siz[v];
				val = max(val, siz[v]);
			}
			val = max(val, tot - siz[u]);
			if (val < mn) {
				mn = val;
				res = u;
			}
			return;
		};
		dfs(dfs, u, u);
		return res;
	};
	auto getSiz = [&](auto&&self, int u, int f) -> int {
		int res = 1;
		for (auto v : g[u]) {
			if (v == f || bad[v]) continue;
			res += self(self, v, u);
		}
		return res;
	};
	vector<int> roots;
	int rt = getCenter(1, n);
	roots.push_back(rt);
	while (!roots.empty()) {
		rt = roots.back(); roots.pop_back();
		bad[rt] = 1;
		for (auto v : g[rt]) {
			if (bad[v]) continue;
			v = getCenter(v, getSiz(getSiz, v, v));
			e[rt].push_back(v);
			roots.push_back(v); 
		}
	}
	return e;
};

```
