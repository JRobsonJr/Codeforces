// 687B: Remainders Game

#include <bits/stdc++.h>
using namespace std;

long long int gcd(long long int a, long long int b) {
    if (b == 0) return a;
    return gcd(b, a % b);
}

int main() {
    long long int n, k;
    scanf("%lld %lld\n", &n, &k);
    long long int value = 1;
    long long int curr;
    for (long long int i = 0; i < n; i++) {
        scanf("%lld", &curr);
        value = gcd(k, value * curr / gcd(value, curr));
    }
    if (value == k) {
        printf("Yes\n");
    } else {
        printf("No\n");
    }
    return 0;
}
