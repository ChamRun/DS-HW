package HW2;

import java.util.Arrays;

public class Sort1ToN2 {
    // A function to do counting sort of arr[] according to
    // the digit represented by exp.
    void countSort(int arr[], int n, int exp)
    {
        int output[] = new int[n]; // output array
        int i, count[] = new int[n] ;
        for (i=0; i < n; i++)
            count[i] = 0;


        System.out.println("c9:\t" + Arrays.toString(count));

        // Store count of occurrences in count[]
        System.out.println("exp: " + exp);
        for (i = 0; i < n; i++) {
            System.out.println("DD: " + (arr[i] / exp) + "\nD: " + (arr[i] / exp) % n);
            count[(arr[i] / exp) % n]++;
        }

        System.out.println("c0:\t" + Arrays.toString(count));
        // Change count[i] so that count[i] now contains actual
        // position of this digit in output[]
        for (i = 1; i < n; i++)
            count[i] += count[i - 1];
        System.out.println("c1:\t" + Arrays.toString(count));

        // Build the output array
        for (i = n - 1; i >= 0; i--)
        {
            output[count[ (arr[i]/exp)%n] - 1] = arr[i];
            count[(arr[i]/exp)%n]--;
        }
        System.out.println("c2:\t" + Arrays.toString(count));
        System.out.println("O0:\t" + Arrays.toString(output));

        // Copy the output array to arr[], so that arr[] now
        // contains sorted numbers according to current digit
        for (i = 0; i < n; i++)
            arr[i] = output[i];
    }


    // The main function to that sorts arr[] of size n using Radix Sort
    void sort(int arr[], int n)
    {
        // Do counting sort for first digit in base n. Note that
        // instead of passing digit number, exp (n^0 = 1) is passed.
        countSort(arr, n, 1);
        System.out.println("1:\t" + Arrays.toString(arr));

        // Do counting sort for second digit in base n. Note that
        // instead of passing digit number, exp (n^1 = n) is passed.
        countSort(arr, n, n);
    }

    // A utility function to print an array
    void printArr(int arr[], int n)
    {
        for (int i = 0; i < n; i++)
            System.out.print(arr[i]+" ");
    }

    // Driver program to test above functions
    public static void main(String args[])
    {
        Sort1ToN2 ob = new Sort1ToN2();

        // Since array size is 7, elements should be from 0 to 48
        int arr[] = {40, 12, 45, 32, 33, 1, 22};
        int n = arr.length;
        System.out.println("0:\t" + Arrays.toString(arr));
        //ob.printArr(arr, n);

        ob.sort(arr, n);

        System.out.println("-1:\t" + Arrays.toString(arr));
        //ob.printArr(arr, n);
    }
}
