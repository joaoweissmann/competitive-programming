#include <bits/stdc++.h>

int main()
{
    std::string dna;
    std::cin >> dna;
    // std::cout << "dna = " << dna << std::endl;

    int best = 0;
    char curr = dna[0];
    char prev = dna[0];
    int currCount = 0;
    for (std::string::iterator it=dna.begin(); it!=dna.end(); it++)
    {
        curr = *it;
        // std::cout << curr;

        // std::cout << "curr = " << curr " ; prev = " << prev << std::endl;
        
        if (it == dna.begin())
        {
            currCount = 1;
        }
        else
        {
            if (curr == prev)
            {
                // std::cout << curr << " == " prev << std::endl;
                currCount++;
            }
            else
            {
                currCount = 1;
            }
        }
        if (currCount > best)
        {
            best = currCount;
        }
        prev = curr;
    }

    std::cout << best;

    return 0;
}