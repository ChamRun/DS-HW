#include <iostream>

using namespace std;

int main()
{

    int t;
    cin >> t;

    for (size_t j = 0; j < t; j++)
    {

        int n;
        cin >> n;
        int a[n];
        int max = 0;

        for (size_t i = 0; i < n; i++)
        {
            cin >> a[i];
            if (max < a[i])
            {
                max = a[i];
            }
        }

        printf("a: ");
        for (size_t i = 0; i < n; i++)
        {
            cout << a[i] << " ";
        }
        

        int sorted[max + 1];


        for (size_t i = 0; i < n; i++)
        {
            sorted[a[i]] = 0;
        }

        printf("\nsorted: ");
        for (size_t i = 0; i <= max; i++)
        {
            cout << sorted[i] << " ";
        }

        int counter = n;

        for (size_t i = 0; i < n; i++)
        {
            sorted[a[i]]++;
        }


        for (size_t i = 0; i < max; i++)
        {
            counter += ((1 + sorted[i]) * sorted[i]) / 2;
        }
        

        cout << "\n\nans: " << counter << "\n";
    }
}
