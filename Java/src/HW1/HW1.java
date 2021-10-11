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

        int difference = 0;

        difference = counter(numbs, firstDigit, secondDigit, difference);

        // System.out.println("diff: " + difference);

        printResult(firstDigit, secondDigit, difference, n);

    }

    private static int counter(int[] numbs, int firstDigit, int secondDigit, int difference) {

        if (numbs.length == 1){
            if (numbs[0] == firstDigit)
                difference++;
            else
                difference--;

            return difference;
        }

        int[] new_numbs = new int[numbs.length - 2];

        if (numbs[0] == numbs[1]) {
            if (numbs[0] == firstDigit)
                difference++;
            else
                difference--;
        }

        System.arraycopy(numbs, 2, new_numbs, 0, new_numbs.length);
        return counter(new_numbs, firstDigit, secondDigit, difference);


    }


    private static void printResult(int firstDigit, int secondDigit, int difference, int length) {

        if (0 < difference) {

            System.out.println(firstDigit + " " + ((length + difference) / 2));
        }

        else {
            System.out.println(secondDigit + " " + ((length - difference) / 2));
        }
    }

}


