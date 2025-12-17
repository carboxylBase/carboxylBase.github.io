# Splay

```cpp
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const ll N = 2000000;

/*
支持自定义结构体从小到大排序的平衡树
注意在使用 suc 或者 pre 时,如果树中不存在这个前后驱,会 re
可通过插入正负无穷解决这个问题
*/

template<typename T, typename Compare = std::less<T>>
class SplayTree {
private:
    int siz;
    struct Node {
        T key;
        Node *left, *right, *parent;
        int cnt;  
        std::size_t sz; 
        Node(const T& k, Node* p=nullptr)
          : key(k), left(nullptr), right(nullptr), parent(p), cnt(1), sz(1) {}
    };

    Node* root = nullptr;
    Compare comp;

    void update(Node* x) {
        x->sz = x->cnt
              + (x->left ? x->left->sz : 0)
              + (x->right ? x->right->sz : 0);
    }

    void rotate_left(Node* x) {
        Node* y = x->right;
        x->right = y->left;
        if (y->left) y->left->parent = x;
        y->parent = x->parent;
        if (!x->parent) root = y;
        else if (x == x->parent->left) x->parent->left = y;
        else x->parent->right = y;
        y->left = x; x->parent = y;
        update(x); update(y);
    }

    void rotate_right(Node* x) {
        Node* y = x->left;
        x->left = y->right;
        if (y->right) y->right->parent = x;
        y->parent = x->parent;
        if (!x->parent) root = y;
        else if (x == x->parent->left) x->parent->left = y;
        else x->parent->right = y;
        y->right = x; x->parent = y;
        update(x); update(y);
    }

    void splay(Node* x) {
        while (x->parent) {
            Node* p = x->parent;
            Node* g = p->parent;
            if (!g) {
                if (x == p->left) rotate_right(p);
                else rotate_left(p);
            } else if ((x == p->left) == (p == g->left)) {
                if (x == p->left) { rotate_right(g); rotate_right(p); }
                else { rotate_left(g); rotate_left(p); }
            } else {
                if (x == p->left) { rotate_right(p); rotate_left(g); }
                else { rotate_left(p); rotate_right(g); }
            }
        }
    }

    Node* find_node(const T& key) {
        Node* x = root;
        while (x) {
            if (comp(key, x->key)) x = x->left;
            else if (comp(x->key, key)) x = x->right;
            else return x;
        }
        return nullptr;
    }

public:
    SplayTree(Compare c = Compare()) : comp(c) {}

    void insert(const T& key) {
        siz++;
        if (!root) {
            root = new Node(key);
            return;
        }
        Node* x = root;
        Node* p = nullptr;
        while (x && !( !comp(key, x->key) && !comp(x->key, key) )) {
            p = x;
            x = comp(key, x->key) ? x->left : x->right;
        }
        if (x) {
            x->cnt++;
            splay(x);
        } else {
            x = new Node(key, p);
            if (comp(key, p->key)) p->left = x;
            else p->right = x;
            splay(x);
        }
    }

    bool contains(const T& key) {
        Node* x = find_node(key);
        if (x) { splay(x); return true; }
        return false;
    }

    void erase(const T& key) {
        Node* x = find_node(key);
        if (!x) return;
        siz--;
        splay(x);
        if (x->cnt > 1) {
            x->cnt--;
            update(x);
            return;
        }
        Node* L = x->left;
        Node* R = x->right;
        delete x;
        if (L) L->parent = nullptr;
        if (!L) {
            root = R;
            if (R) R->parent = nullptr;
        } else {
            Node* m = L;
            while (m->right) m = m->right;
            splay(m);
            m->right = R;
            if (R) R->parent = m;
            root = m;
            update(root);
        }
    }

    bool empty() const { return root == nullptr; }

    std::size_t size() const { return root ? root->sz : 0; }

    T kth(std::size_t k) {
        if (!root || k<1 || k>root->sz) throw std::out_of_range("k");
        Node* x = root;
        while (x) {
            std::size_t L = x->left? x->left->sz : 0;
            if (k <= L) x = x->left;
            else if (k > L + x->cnt) {
                k -= L + x->cnt;
                x = x->right;
            } else {
                splay(x);
                return x->key;
            }
        }
        throw std::out_of_range("k");
    } 

    std::size_t getRank(const T& key) {
        if (!root) return 0;
        Node* x = root;
        std::size_t rank = 0;
        while (x) {
            if (comp(key, x->key)) {
                x = x->left;
            } else {
                std::size_t L = x->left? x->left->sz : 0;
                rank += L;
                if (!comp(x->key, key) && !comp(key, x->key)) {
                    splay(x);
                    return rank;
                }
                rank += x->cnt;
                x = x->right;
            }
        }
        if (x) splay(x);
        return rank;
    } 

    T pre(const T& key) {
        Node* x = root;
        Node* pred = nullptr;
        while (x) {
            if (comp(x->key, key)) {
                pred = x;
                x = x->right;
            } else x = x->left;
        }
        if (!pred) throw std::out_of_range("no predecessor");
        splay(pred);
        return pred->key;
    }  

    T suc(const T& key) {
        Node* x = root;
        Node* succ = nullptr;
        while (x) {
            if (comp(key, x->key)) {
                succ = x;
                x = x->left;
            } else x = x->right;
        }
        if (!succ) throw std::out_of_range("no successor");
        splay(succ);
        return succ->key;
    } 

    int size() {
        return siz;
    }
};
```
