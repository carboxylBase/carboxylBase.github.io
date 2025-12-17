# Flow

```cpp
#include <bits/stdc++.h>
using namespace std;
#define DEBUG 1
#define FUCK if (DEBUG) cout << "fuck" << endl;
using ll = long long;
using pii = pair<int,int>;
using i128 = __int128_t;
using pll = pair<ll,ll>;
const ll N = 2000000;
const ll INF = 5e18;
const ll MOD = 1e9 + 7;


class Graph {
public:
    int n;        
    struct Edge {
        int next, to, rev;
        ll w;
    } edge[2 * N];  
    int head[N];      
    int cnt; 

    void init(int N_) {
        n = N_;
        for (int i = 0; i <= n; i++)
            head[i] = 0;
        cnt = 0;
    }

    void add_edge(int u, int v, ll w) {
        cnt++;
        edge[cnt].to = v;
        edge[cnt].w = w;
        edge[cnt].next = head[u];
        head[u] = cnt;
        int forward_index = cnt;
        cnt++;
        edge[cnt].to = u;
        edge[cnt].w = 0;
        edge[cnt].next = head[v];
        head[v] = cnt;
        int reverse_index = cnt;
        edge[forward_index].rev = reverse_index;
        edge[reverse_index].rev = forward_index;
    }
} g;

class Dinic {
private:
    Graph* G;       
    int s, t;             
    vector<ll> d;         
    vector<int> cur;       

    bool bfs() {
        fill(d.begin(), d.end(), -1);
        queue<int> q;
        d[s] = 0;
        q.push(s);
        while (!q.empty()) {
            int u = q.front(); q.pop();
            for (int i = G->head[u]; i; i = G->edge[i].next) {
                int v = G->edge[i].to;
                if (d[v] < 0 && G->edge[i].w > 0) {
                    d[v] = d[u] + 1;
                    q.push(v);
                }
            }
        }
        return d[t] >= 0;
    }

    ll dfs(int u, ll flow) {
        if (u == t) return flow;
        for (int &i = cur[u]; i; i = G->edge[i].next) {
            int v = G->edge[i].to;
            if (d[v] == d[u] + 1 && G->edge[i].w > 0) {
                ll pushed = dfs(v, min(flow, G->edge[i].w));
                if (pushed) {
                    G->edge[i].w -= pushed;
                    G->edge[G->edge[i].rev].w += pushed;
                    return pushed;
                }
            }
        }
        return 0;
    }

public:
    Dinic(Graph* graph, int source, int sink) : G(graph), s(source), t(sink) {
        d.resize(G->n + 1);
        cur.resize(G->n + 1);
    }

    ll max_flow() {
        ll flow = 0;
        while (bfs()) {
            for (int i = 0; i <= G->n; i++)
                cur[i] = G->head[i];
            while (ll pushed = dfs(s, INF))
                flow += pushed;
        }
        return flow;
    }
};

template<typename T>
class MinCostMaxFlow {
public:
    struct Edge {
        int next, to;
        T w, c;
    };
 
    int n,cnt;                             
    vector<Edge> edge;                   
    vector<T> dis,flow;           
    vector<int> pre,last,head;            
    vector<bool> vis;          
 

    MinCostMaxFlow(int n, int edgeCapacity = 4000000) : n(n) {
        head.assign(n + 1, 0);
        edge.resize(edgeCapacity + 1);
        cnt = 1; 
        dis.assign(n + 1, 0);
        pre.assign(n + 1, -1);
        last.assign(n + 1, 0);
        flow.assign(n + 1, 0);
        vis.assign(n + 1, false);
    }
 
    void init(int n) {
        this->n = n;
        fill(head.begin(), head.end(), 0);
        cnt = 1;
    }
 
    void addEdge(int u, int v, T w,T c) {
        edge[++cnt] = { head[u], v, w, c };
        head[u] = cnt;
        edge[++cnt] = { head[v], u, 0, -c };
        head[v] = cnt;
    }
 
    bool spfa(int s, int t) {
        const int INF = 0x3f3f3f3f;
        fill(dis.begin(), dis.end(), INF);
        fill(flow.begin(), flow.end(), INF);
        fill(vis.begin(), vis.end(), false);
        fill(pre.begin(), pre.end(), -1);
 
        queue<int> q;
        q.push(s);
        vis[s] = true;
        dis[s] = 0;
        flow[s] = INF;
 
        while (!q.empty()) {
            int u = q.front();
            q.pop();
            vis[u] = false;
            for (int i = head[u]; i; i = edge[i].next) {
                int v = edge[i].to;
                if (edge[i].w > 0 && dis[v] > dis[u] + edge[i].c) {
                    dis[v] = dis[u] + edge[i].c;
                    pre[v] = u;
                    last[v] = i;
                    flow[v] = min(flow[u], edge[i].w);
                    if (!vis[v]) {
                        q.push(v);
                        vis[v] = true;
                    }
                }
            }
        }
        return pre[t] != -1;
    }
 
    pair<T, T> run(int s, int t) {
        T maxFlow = 0, minCost = 0;
        while (spfa(s, t)) {
            int f = flow[t];
            maxFlow += f;
            minCost += f * dis[t];
            for (int u = t; u != s; u = pre[u]) {
                int i = last[u];
                edge[i].w -= f;
                edge[i ^ 1].w += f;
            }
        }
        return { maxFlow, minCost };
    }
};


// 有源汇上下界最大流
// add(S, E, L, R) 插入边
// solve(S, E) 输出最大流, -1 表示无解!!!
namespace MCMF{
    const int MAXN = 100000 + 3;
    const int MAXM = 700000 + 3; // 增大上界，避免边数超界
    int H[MAXN], V[MAXM], N[MAXM];
    ll F[MAXM]; // 改为 ll
    int o = 1, n;
    void add0(int u, int v, ll f){
        V[++ o] = v; N[o] = H[u]; H[u] = o; F[o] = f;
        V[++ o] = u; N[o] = H[v]; H[v] = o; F[o] = 0;
        n = max(n, u);
        n = max(n, v);
    }
    ll D[MAXN];
    bool bfs(int s, int t){
        queue <int> Q;
        for(int i = 1;i <= n;++ i) D[i] = 0;
        Q.push(s); D[s] = 1;
        while(!Q.empty()){
            int u = Q.front(); Q.pop();
            for(int i = H[u]; i; i = N[i]){
                int v = V[i];
                ll cap = F[i];
                if(cap != 0 && !D[v]){
                    D[v] = D[u] + 1;
                    Q.push(v);
                }
            }
        }
        return D[t] != 0;
    }
    int C[MAXN];
    ll dfs(int s, int t, int u, ll maxf){
        if(u == t) return maxf;
        ll totf = 0;
        for(int &i = C[u]; i; i = N[i]){
            int v = V[i];
            ll cap = F[i];
            if(cap && D[v] == D[u] + 1){
                ll pushed = dfs(s, t, v, min(F[i], maxf));
                if(pushed == 0) continue;
                F[i] -= pushed;
                F[i ^ 1] += pushed;
                totf += pushed;
                maxf -= pushed;
                if(maxf == 0) return totf;
            }
        }
        return totf;
    }
    ll mcmf(int s, int t){
        ll ans = 0;
        while(bfs(s, t)){
            memcpy(C, H, sizeof(H));
            ans += dfs(s, t, s, (ll)1e18);
        }
        return ans;
    }
    ll G[MAXN];
    void add(int u, int v, ll l, ll r){
        G[v] += l;
        G[u] -= l;
        add0(u, v, r - l);
    }
    void clear(){
        for(int i = 1;i <= o;++ i){
            N[i] = 0; F[i] = 0; V[i] = 0;
        }
        for(int i = 1;i <= n;++ i){
            H[i] = 0; G[i] = 0; C[i] = 0;
        }
        o = 1; n = 0;
    }
    bool solve(){ // 无源汇可行性检查
        int s = ++ n;
        int t = ++ n;
        ll sum = 0;
        for(int i = 1;i <= n - 2;++ i){
            if(G[i] < 0) add0(i, t, -G[i]);
            else add0(s, i,  G[i]), sum += G[i];
        }
        auto res = mcmf(s, t);
        if(res != sum) return false;
        return true;
    }
    ll solve(int s0, int t0){ // 有源汇上下界最大流
        add0(t0, s0, (ll)1e18);
        int s = ++ n;
        int t = ++ n;
        ll sum = 0;
        for(int i = 1;i <= n - 2;++ i){
            if(G[i] < 0) add0(i, t, -G[i]);
            else add0(s, i,  G[i]), sum += G[i];
        }
        auto res = mcmf(s, t);
        if(res != sum) return -1;
        return mcmf(s0, t0);
    }
}
```
