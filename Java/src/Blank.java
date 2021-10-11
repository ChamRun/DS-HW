import java.util.Arrays;

public class Blank {
    public static void main(String[] args) {

        String[] stringArray = {"foo", "bar", "baz"};
        String[] modifiedArray = Arrays.copyOfRange(stringArray, 1, stringArray.length);


        System.out.println(Arrays.toString(stringArray));
        System.out.println(Arrays.toString(modifiedArray));

    }
}
