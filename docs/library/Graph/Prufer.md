# Prufer

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

/*
做模版题的时候发现这个 push_back 的常数真不是一般的大
数据量大的时候慎用这个 push_back 吧
*/
struct Prufer {
	// 注意 g 的下标从 1 开始
	// vector<int> getPrufer(vector<vector<int>>& g) {
	// 	int n = g.size() - 1;
	// 	vector<int> d(n + 1, 0);
	// 	for (int i = 1;i<n+1;i++) {
	// 		d[i] = g[i].size();
	// 	}
	// 	vector<int> fa(n + 1, 0);
	// 	{
	// 		vector<int> stk;
	// 		stk.push_back(n);
	// 		while (!stk.empty()) {
	// 			int u = stk.back(); stk.pop_back();
	// 			for (auto v : g[u]) {
	// 				if (v == fa[u]) continue;
	// 				fa[v] = u;
	// 				stk.push_back(v);
	// 			}
	// 		}
	// 	}
	// 	vector<int> p;
	// 	for (int i = 1;i<=n&&p.size()<n-2;i++) {
	// 		if (d[i] == 1 && fa[i]) {
	// 			p.push_back(fa[i]);
	// 			d[fa[i]] --;
	// 			d[i] --;
	// 			int u = fa[i];
	// 			while (d[u] == 1 && u<i+1 && fa[u] && p.size()<n-2) {
	// 				p.push_back(fa[u]);
	// 				d[fa[u]] --;
	// 				d[u] --;
	// 				u = fa[u];
	// 			}
	// 		}
	// 	}
	// 	return p;
	// }
	vector<int> getPrufer(vector<int>& fa) {
		int n = fa.size() - 1;
		vector<int> d(n + 1, 0);
		for (int i = 1;i<n+1;i++) {
			if (fa[i]) {
				d[i] ++; d[fa[i]] ++;
			}
		}
		vector<int> p;
		for (int i = 1;i<=n&&p.size()<n-2;i++) {
			if (d[i] == 1 && fa[i]) {
				p.push_back(fa[i]);
				d[fa[i]] --;
				d[i] --;
				int u = fa[i];
				while (d[u] == 1 && u<i+1 && fa[u] && p.size()<n-2) {
					p.push_back(fa[u]);
					d[fa[u]] --;
					d[u] --;
					u = fa[u];
				}
			}
		}
		return p;
	}

	// 注意 p 的下标是从 0 开始
	// 返回的 fa 数组是从 1 开始
	vector<int> getTree(vector<int>& p) {
		int n = p.size() + 2;
		vector<int> d(n + 1, 1);
		for (auto v : p) {
			d[v] ++;
		}
		vector<int> fa(n + 1, 0);
		for (int i = 1,j=0;i<=n&&j<p.size();i++) {
			if (d[i] == 1) {
				fa[i] = p[j];
				d[i] --; d[p[j]] --;
				int u = p[j]; j ++;
				while (d[u] == 1&&j<p.size()&&u<i+1) {
					fa[u] = p[j];
					d[u] --; d[p[j]] --;
					u = p[j]; j ++;
				}
			}
		}
		for (int i = 1;i<n;i++) {
			if (d[i] == 1) {
				fa[i] = n;
				break;
			}
		}
		return fa;
	}
} solver;
```
