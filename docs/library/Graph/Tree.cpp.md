# Tree

```cpp
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const ll N = 2000000;
class Tree{
public:
    vector<int> g[N];
    int n;
    int fa[N],dep[N],siz[N];
public:
    Tree(int N) {
        n = N;
    }
    void init(){
        for (int i = 1;i<n;i++){
            int u,v;
            cin >> u >> v;
            g[u].push_back(v);
            g[v].push_back(u);
        }
        return;
    }
    void dfs_pre(int u,int f){
        siz[u] = 1;
        fa[u] = f;
        dep[u] = dep[f] + 1;
        for (auto v:g[u]){
            if (v == f) continue;
            dfs_pre(v,u);
        }
        return;
    }
};

using pii = pair<int, int>;
pii getDiameter(vector<vector<int>>& g) {
	int s = 1, e;
	int mxDep = -1;
	auto dfs = [&](auto&&self, int u, int dep, int f) -> void {
		if (mxDep < dep) {
			mxDep = dep;
			e = u;
		}
		for (auto v : g[u]) {
			if (v == f) continue;
			self(self, v, dep + 1, u);
		}
		return;
	};
	dfs(dfs, 1, 0, 1);
	swap(s, e); mxDep = -1;
	dfs(dfs, s, 0, s);
	return {s, e};
}
```
