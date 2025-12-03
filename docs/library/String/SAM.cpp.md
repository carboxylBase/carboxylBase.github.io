# SAM

```cpp
#include <bits/stdc++.h>

using namespace std;
using ll = long long;
using pii = pair<int,int>;
using pll = pair<ll,ll>;
using db = long double;
using pdd = pair<db, db>;
using i128 = __int128_t;

const ll N = 2000000;
const ll INF = 5e18;
const ll MOD = 1e9 + 7;

// 广义
// 注意这个模版中用的是 char 类型, 如果插入的是别的记得改一下
namespace SAM {
    struct state {
        int len, link;
        std::map<char, int> next;
    };
    constexpr int MAXLEN = 1000110;
    state st[MAXLEN * 2];
    int sz, last;
    long long endpos_cnt[MAXLEN * 2];

    void sam_init() {
        st[0].len = 0;
        st[0].link = -1;
        sz = 1; last = 0;
    }

    void sam_extend(char c) {
        int cur = sz++;
        st[cur].len = st[last].len + 1;
        endpos_cnt[cur] = 1;
        int p = last;
        while (p != -1 && !st[p].next.count(c)) {
            st[p].next[c] = cur;
            p = st[p].link;
        }
        if (p == -1) st[cur].link = 0;
        else {
            int q = st[p].next[c];
            if (st[p].len + 1 == st[q].len) st[cur].link = q;
            else {
                int clone = sz++;
                st[clone].len = st[p].len + 1;
                st[clone].next = st[q].next;
                st[clone].link = st[q].link;
                while (p != -1 && st[p].next[c] == q) {
                    st[p].next[c] = clone;
                    p = st[p].link;
                }
                st[q].link = st[cur].link = clone;
            }
        }
        last = cur;
    }

    void build_endpos() {
        vector<int> order(sz);
        iota(order.begin(), order.end(), 0);
        sort(order.begin(), order.end(),
             [&](int a, int b){ return st[a].len > st[b].len; });
        for (int v : order) {
            if (st[v].link != -1) {
                endpos_cnt[st[v].link] += endpos_cnt[v];
            }      
        }     
    }
}

// 小写字母字符集
namespace SAM {
    struct state {
        int len, link;
        int next[26];
    };
    constexpr int MAXLEN = 1000110;
    state st[MAXLEN * 2];
    int sz, last;
    long long endpos_cnt[MAXLEN * 2];

    void sam_init() {
        st[0].len = 0;
        st[0].link = -1;
        sz = 1; last = 0;
    }

    void sam_extend(char c) {
        int cur = sz++;
        st[cur].len = st[last].len + 1;
        endpos_cnt[cur] = 1;
        int p = last;
        while (p != -1 && !st[p].next[c - 'a']) {
            st[p].next[c - 'a'] = cur;
            p = st[p].link;
        }
        if (p == -1) st[cur].link = 0;
        else {
            int q = st[p].next[c - 'a'];
            if (st[p].len + 1 == st[q].len) st[cur].link = q;
            else {
                int clone = sz++;
                st[clone].len = st[p].len + 1;
                for (int i = 0;i<26;i++) {
                    st[clone].next[i] = st[q].next[i];
                }
                st[clone].link = st[q].link;
                while (p != -1 && st[p].next[c - 'a'] == q) {
                    st[p].next[c - 'a'] = clone;
                    p = st[p].link;
                }
                st[q].link = st[cur].link = clone;
            }
        }
        last = cur;
    }

    void build_endpos() {
        vector<int> order(sz);
        iota(order.begin(), order.end(), 0);
        sort(order.begin(), order.end(),
             [&](int a, int b){ return st[a].len > st[b].len; });
        for (int v : order) {
            if (st[v].link != -1) {
                endpos_cnt[st[v].link] += endpos_cnt[v];
            }      
        }     
    }
}

```
