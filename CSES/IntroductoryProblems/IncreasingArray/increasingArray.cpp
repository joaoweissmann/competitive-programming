#include <bits/stdc++.h>

int main()
{
    int n;
    std::cin >> n;

    std::vector<int> v;
    for (int i=0; i<n; i++)
    {
        int x;
        std::cin >> x;
        v.push_back(x);
    }
    // for (std::vector<int>::iterator it=v.begin(); it!=v.end(); it++)
    // {
    //     std::cout << *it << ", ";
    // }
    
    long long count{0};
    for (std::vector<int>::iterator it=v.begin(); it!=v.end(); it++)
    {
        int curr;
        int prev;
        if (it == v.begin())
        {
            continue;
        }
        else
        {
            curr = *it;
            prev = *(std::prev(it));
            // std::cout << "curr = " << curr << ", prev = " << prev << ", count = " << count << std::endl;
            if (curr < prev)
            {
                count += prev - curr;
                *it += prev - curr;
            }
            // std::cout << "curr = " << curr << ", prev = " << prev << ", count = " << count << std::endl;
        }
    }
    std::cout << count;

    return 0;
}