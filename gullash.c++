#include <bits/stdc++.h>
using namespace std;
using ll = long long;
const int MAXN = 1000000;
const int INF = MAXN + 3;
int n, k, l, r;
int dp[MAXN + 5];
deque<int> pos;
void t_main()
{
    cin >> n >> k;
    dp[0] = dp[n + 1] = INF;
    dp[n + 1]++;
    for (int i = 1; i <= n; i++)
        cin >> dp[i];
    pos.push_back(k);
    bool isRight = (k == 1 || dp[k - 1] > dp[k]);
    l = r = pos.back();
    vector<int> ans;
    while (1 <= l || r <= n)
    {
        if (isRight)
        {
            int cur = ++r;
            while (pos.size() > 1)
            {
                if (dp[pos.back()] < dp[cur])
                    ans.push_back(pos.back()), pos.pop_back();
                else
                    break;
            }
            if (pos.size() == 1 && dp[pos.back()] < dp[cur])
                isRight = !isRight;
            pos.push_back(cur);
        }
        else
        {
            int cur = --l;
            while (pos.size() > 1)
            {
                if (dp[pos.front()] < dp[cur])
                    ans.push_back(pos.front()), pos.pop_front();
                else
                    break;
            }
            if (pos.size() == 1 && dp[pos.front()] < dp[cur])
                isRight = !isRight;
            pos.push_front(cur);
        }
    }
    for (int i = 0; i < n; i++)
        cout << ans[i] << " \n"[i == n - 1];
}
signed main()
{
    signed t = 1;
    cin.tie(nullptr)->sync_with_stdio(false);
    while (t--)
    {
        t_main();
        cout << '\n';
    }
    return 0;
}