#include <bits/stdc++.h>

int main()
{
    int n;
    std::cin >> n;

    std::set<int> s;
    for (int i=0; i<n; i++)
    {
        s.insert(i+1);
    }

    for (int i=0; i<n-1; i++)
    {
        int x;
        std::cin >> x;
        s.erase(x);
    }

    for (std::set<int>::iterator it=s.begin(); it!=s.end(); it++)
    {
        std::cout << *it;
    }

    return 0;
}
