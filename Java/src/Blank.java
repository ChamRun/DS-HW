import java.util.Arrays;

public class Blank {
    public static void main(String[] args) {
        int[] g = {1, 2, 3};
        int[] h = new int[g.length - 1];
        System.arraycopy(g, 1, h, 0, h.length);

        System.out.println(Arrays.toString(g));
        System.out.println(Arrays.toString(h));

    }
}
