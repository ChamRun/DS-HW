//package HW1;

import java.util.Arrays;
import java.util.Scanner;

public class HW1Ver2 {
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

        difference = counter(firstDigit, difference, numbs);

        printResult(firstDigit, secondDigit, difference, n);

    }

    private static int counter(int firstDigit, int difference, int... numbs) {

        switch (numbs.length){
            case 0:
                return difference;

            case 1:
                // pr("1: ");
                if (numbs[0] == firstDigit)
                    difference++;
                else
                    difference--;
                return difference;

            case 2:
                if (numbs[0] == numbs[1]) {
                    if (numbs[0] == firstDigit)
                        difference += 2;
                    else
                        difference -= 2;
                }
                pr(Arrays.toString(numbs) + " : " + difference);
                return difference;

            default:
                for (int i = 0; i < numbs.length; i += 2) {
                    if (i + 1 < numbs.length)
                        difference = counter(firstDigit, difference, numbs[i], numbs[i + 1]);
                    else
                        difference = counter(firstDigit, difference, numbs[i]);
                    pr("diff: " + difference);
                }

        }

        return difference;

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

    static void pr(String toBePrinted){
        //System.out.println(toBePrinted);
    }

}



