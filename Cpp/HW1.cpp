#include <iostream>

using namespace std;


int counter(int first_digit, int difference, int arr[])
{

    int n = *(&arr + 1) - arr;

    switch (n)
    {
    case 0:
        return difference;

    case 1:
        if (arr[0] == first_digit)
        {
            return (difference + 1);
        }
        else
        {
            return (difference - 1);
        }

    case 2:
        if (arr[0] == arr[1])
        {
            if (arr[0] == first_digit)
                return difference + 2;
            else
                return difference - 2;
        }

    default:
        for (int i = 0; i < n; i += 2)
        {
            

            if (i + 1 < n){
                int devided_arr[] = {arr[0], arr[1]};
                difference = counter(first_digit, difference, devided_arr);
            }
            else{
                int devided_arr[] = {arr[0]};
                difference = counter(first_digit, difference, devided_arr);
            }
        }
        return difference;
    }

    cout << "OUT OF SWITCH?!";
}

int main()
{

    int n;
    cin >> n;

    int first_digit;
    cin >> first_digit;
    int second_digit;
    cin >> second_digit;

    int arr[n];

    for (size_t i = 0; i < n; i++)
    {
        cin >> arr[i];
    }

    int difference = counter(first_digit, 0, arr);

    if (0 < difference) {
            cout << first_digit << " " << ((n + difference) / 2 + 1);
        }
        else {
            cout << second_digit << " " << ((n - difference) / 2 + 1);
        }

    return 0;
}
