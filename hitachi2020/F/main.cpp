#include <bits/stdc++.h>
using namespace std;

const long long MOD = 998244353;

void solve(long long N, std::vector<long long> a, std::vector<long long> b){

}

// Generated by 1.1.6 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
int main(){
    long long N;
    scanf("%lld",&N);
    std::vector<long long> a(N-1);
    std::vector<long long> b(N-1);
    for(int i = 0 ; i < N-1 ; i++){
        scanf("%lld",&a[i]);
        scanf("%lld",&b[i]);
    }
    solve(N, std::move(a), std::move(b));
    return 0;
}
