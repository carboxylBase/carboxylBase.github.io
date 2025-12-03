# Hash

```cpp
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const ll N = 2000000;


// 双模数 hash, 记得先 init
struct Hash {
	int x,y,MOD1 = 1000000007,MOD2 = 1000000009;
	Hash(){x = y = 0;}
	Hash(int _x,int _y) { x = _x; y = _y; }
	Hash operator + (const Hash &a) const {
		return Hash((x + a.x) % MOD1,(y + a.y) % MOD2);
	}	
	Hash operator - (const Hash &a) const {
		return Hash((x - a.x + MOD1) % MOD1,(y - a.y + MOD2) % MOD2);
	}
	Hash operator * (const Hash &a) const {
		return Hash(1ll * x * a.x % MOD1,1ll * y * a.y % MOD2);
	}
    Hash operator * (const ll &a) const {
		return Hash(1ll * x * a % MOD1,1ll * y * a % MOD2);
	}
    bool operator == (const Hash &a) const {
		return (x == a.x && y == a.y);
	}
	bool operator<(const Hash& a) const {
		if (x != a.x) {
			return x < a.x;
		}
		return y < a.y;
	}
	bool operator>(const Hash& a) const {
		if (x != a.x) {
			return x > a.x;
		}
		return y > a.y;
	}
}base(131,13331),hs[N],bs[N];

void hash_init(int n){
	bs[0] = Hash(1,1);
	for(int i = 1;i <= n;i ++) {
		bs[i] = bs[i-1] * base;
	}
}
```
