//package HW1;

import java.util.Arrays;
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

        difference = counter(numbs, firstDigit, difference);

        printResult(firstDigit, secondDigit, difference, n);

    }

    private static int counter(int[] numbs, int firstDigit, int difference) {

        if (numbs.length < 2){

            if (numbs.length == 0)
                return difference;

            if (numbs[0] == firstDigit)
                difference++;
            else
                difference--;

            return difference;
        }

        int[] new_numbs;

        if (numbs[0] == numbs[1]) {
            if (numbs[0] == firstDigit)
                difference += 2;
            else
                difference -= 2;
        }

        //System.arraycopy(numbs, 2, new_numbs, 0, new_numbs.length);
        new_numbs = Arrays.copyOfRange(numbs, 2, numbs.length);
        return counter(new_numbs, firstDigit, difference);

    }


    private static void printResult(int firstDigit, int secondDigit, int difference, int length) {

        //difference = (length + Math.abs(difference)) / 2;
        //System.out.println("diff: " + difference);

        if (0 < difference) {
            System.out.println(firstDigit + " " + ((length + difference) / 2));
        }

        else {
            System.out.println(secondDigit + " " + ((length - difference) / 2));
        }
    }

}


