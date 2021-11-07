#include <iostream>

using namespace std;

int main()
{

    int t;
    cin >> t;

    for (size_t i = 0; i < t; i++)
    {

        int n;
        cin >> n;
        int arr[n];
        for (size_t i = 0; i < n; i++)
        {
            cin >> arr[i];
        }

        int cou = n;

        for (size_t i = 0; i < n - 1; i++)
        {
            for (size_t j = i + 1; j < n; j++)
            {
                if(arr[i] == arr[j]){
                    cou++;
                }
            }
        }

        cout << cou << "\n";

        
    }
}
