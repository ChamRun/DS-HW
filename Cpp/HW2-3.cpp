#include <iostream>
#include <math.h>

using namespace std;

int main()
{
    long double ans = 0;

    for (int i = 0; i < 4; i++)
    {
        ans += 1 / (pow(2, i));   
    }

    cout << ans;
    
}
