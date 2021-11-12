#include <iostream>
#include <math.h>

using namespace std;

int main()
{
    long double ans = 0;

    for (int i = 0; i < 100; i++)
    {
        ans += (pow(3, i)) / (pow(4, i));   
    }

    cout << ans;
    
}
