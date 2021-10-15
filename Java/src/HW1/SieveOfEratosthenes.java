package HW1;

import java.util.Scanner;

public class SieveOfEratosthenes {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        boolean[] isPrime = new boolean[n + 1];

        isPrime[0] = false;
        isPrime[1] = false;

        for (int i = 2; i < n + 1; i++) {
            isPrime[i] = true;
        }

        // 1
        for (int i = 2; i < n + 1; i++) {
            if (isPrime[i]){
                //2
                for (int j = 2; j * i < n + 1; j++) {
                    isPrime[j * i] = false;
                }
            }
        }

        for (int i = 0; i < n + 1; i++) {
            if (isPrime[i])
                System.out.print(i + " ");
        }





    }
}
