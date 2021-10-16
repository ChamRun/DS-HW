package HW1;

import java.util.Arrays;
import java.util.Scanner;

public class HW1Ver4 {
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


        int length = numbs.length;
        if (0 < difference) {
            System.out.println(firstDigit + " " + ((length + difference) / 2));
        }
        else {
            System.out.println(secondDigit + " " + ((length - difference) / 2));
        }

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
                return difference;

            default:

                int[] firstHalf = Arrays.copyOfRange(numbs, 1, numbs.length / 2);
                int[] secondHalf = Arrays.copyOfRange(numbs, numbs.length / 2 + 1, numbs.length);

                difference = counter(firstDigit, difference, firstHalf)
                           + counter(firstDigit, difference, secondHalf);


        }

        return difference;

    }



}

