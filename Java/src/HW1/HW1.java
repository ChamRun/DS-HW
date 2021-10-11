package HW1;

import java.util.Scanner;



public class HW1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int firstDigit = sc.nextInt();
        int secondDigit = sc.nextInt();

        int[] numbs = new int[n];

        for (int i = 0; i < n; i++) {
            numbs[i] = sc.nextInt();
        }

        boolean firstIsMore = counter(firstDigit, secondDigit);

        if (firstIsMore)
            System.out.print(firstDigit);
        else
            System.out.println(secondDigit);

    }

    private static boolean counter(int firstDigit, int secondDigit) {
        
    }
}


