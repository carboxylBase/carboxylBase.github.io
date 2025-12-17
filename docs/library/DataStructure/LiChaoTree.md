# LiChaoTree

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;
const ll INF = 1e18;
/*
查最小值就把整棵树按照 x 轴翻转
先用 init 函数初始化
注意空间开到 4 倍!!!

使用方法是先 add 再 update
*/
struct LiChaoTree {
    typedef pair<double, int> pdi;

    const double eps = 1e-9;
    const double NINF = -1e18;
    int cmp(double x, double y) {
        if (x - y > eps) return 1;
        if (y - x > eps) return -1;
        return 0;
    }

    struct line {
        double k, b;
    } p[100005];

    int s[160005];
    int cnt;

    void init(int x) {
        cnt = 0;
        p[0].k = 0; p[0].b = NINF;                  
        fill(s, s + x * 4 + 10, 0);
    }


    double calc(int id, int d) { return p[id].b + p[id].k * d; }

    void add(int x0, int y0, int x1, int y1) {
        cnt++;
        if (x0 == x1)  // 特判直线斜率不存在的情况
            p[cnt].k = 0, p[cnt].b = max(y0, y1); 
        else
            p[cnt].k = double(1) * (y1 - y0) / (x1 - x0), p[cnt].b = y0 - p[cnt].k * x0;
    }

    void upd(int root, int cl, int cr, int u) {  // 对线段完全覆盖到的区间进行修改
        int &v = s[root], mid = (cl + cr) >> 1;
        int bmid = cmp(calc(u, mid), calc(v, mid));
        if (bmid == 1 || (!bmid && u < v)) swap(u, v);
        int bl = cmp(calc(u, cl), calc(v, cl)), br = cmp(calc(u, cr), calc(v, cr));
        if (bl == 1 || (!bl && u < v)) upd(root << 1, cl, mid, u);
        if (br == 1 || (!br && u < v)) upd(root << 1 | 1, mid + 1, cr, u);
    }

    void update(int root, int cl, int cr, int l, int r,
                int u) {  // 定位插入线段完全覆盖到的区间
        if (l <= cl && cr <= r) {
            upd(root, cl, cr, u);
            return;
        }
        int mid = (cl + cr) >> 1;
        if (l <= mid) update(root << 1, cl, mid, l, r, u);
        if (mid < r) update(root << 1 | 1, mid + 1, cr, l, r, u);
    }

    pdi pmax(pdi x, pdi y) {  // pair max函数
        if (cmp(x.first, y.first) == -1)
            return y;
        else if (cmp(x.first, y.first) == 1)
            return x;
        else
            return x.second < y.second ? x : y;
    }

    pdi query(int root, int l, int r, int d) {  // 查询
        if (r < d || d < l) return {0, 0};
        int mid = (l + r) >> 1;
        double res = calc(s[root], d);
        if (l == r) return {res, s[root]};
        return pmax({res, s[root]}, pmax(query(root << 1, l, mid, d),
                            query(root << 1 | 1, mid + 1, r, d)));
    }
};

/*
当插入的线段 k 和 b 都为整数时,使用这个版本可以提高精度.

直接 addLine(k,b) 插入, query(x) 查询.
*/
struct LiChao {
    struct Line { ll m, b; };
    struct Node { Line ln; Node *l, *r; 
        Node(Line v):ln(v),l(nullptr),r(nullptr){}
    };
    ll L, R;
    Node *root;
    LiChao(ll _L, ll _R):L(_L),R(_R),root(nullptr){}
    
    ll eval(const Line &ln, ll x) {
        return ln.m*x + ln.b;
    }
    
    void addLine(Line nw, Node *&nd, ll l, ll r) {
        if (!nd) { nd = new Node(nw); return; }
        ll m = (l + r) >> 1;
        bool lef = eval(nw, l) < eval(nd->ln, l);
        bool mid = eval(nw, m) < eval(nd->ln, m);
        if (mid) swap(nw, nd->ln);
        if (r - l == 0) return;
        if (lef != mid) addLine(nw, nd->l, l, m);
        else addLine(nw, nd->r, m+1, r);
    }
    
    void addLine(ll m, ll b) {
        addLine({m, b}, root, L, R);
    }
    
    ll query(ll x, Node *nd, ll l, ll r) {
        if (!nd) return INF;
        ll res = eval(nd->ln, x);
        if (l==r) return res;
        ll m = (l + r) >> 1;
        if (x <= m) return min(res, query(x, nd->l, l, m));
        else return min(res, query(x, nd->r, m+1, r));
    }
    
    ll query(ll x) {
        return query(x, root, L, R);
    }
};

/*
应对 db 的版本
init 函数中给出定义域即可
long double 比 double 慢得多, 慎用!!!
*/

using db = double;
const db INF_LD = numeric_limits<db>::infinity();

struct LiChao {
    struct Line { db m, b; };
    struct Node { Line ln; Node *l, *r; Node(Line v):ln(v),l(nullptr),r(nullptr){} };
    db L, R;
    Node *root;
    int maxDepth;
    LiChao(db _L = 0, db _R = 0, int _maxDepth = 50):L(_L),R(_R),root(nullptr),maxDepth(_maxDepth){}
    inline db eval(const Line &ln, db x) const { return ln.m * x + ln.b; }
    void addLine(Line nw, Node *&nd, db l, db r, int depth) {
        if (!nd) { nd = new Node(nw); return; }
        db m = (l + r) / 2;
        bool lef = eval(nw, l) < eval(nd->ln, l);
        bool mid = eval(nw, m) < eval(nd->ln, m);
        if (mid) swap(nw, nd->ln);
        if (depth == 0) return;
        if (lef != mid) addLine(nw, nd->l, l, m, depth-1);
        else addLine(nw, nd->r, m, r, depth-1);
    }
    void addLine(db m, db b) { addLine({m,b}, root, L, R, maxDepth); }
    db query(db x, Node *nd, db l, db r, int depth) const {
        if (!nd) return INF_LD;
        db res = eval(nd->ln, x);
        if (depth == 0) return res;
        db mid = (l + r) / 2;
        if (x <= mid) return min(res, query(x, nd->l, l, mid, depth-1));
        else return min(res, query(x, nd->r, mid, r, depth-1));
    }
    db query(db x) const { return query(x, root, L, R, maxDepth); }
    void init(db _L, db _R, int _maxDepth = 50) {
        L = _L;
        R = _R;
        maxDepth = _maxDepth;
        root = nullptr;
    }
};
```
