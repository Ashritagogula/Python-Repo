import java.util.Scanner;

public class PowerModulo {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        int y = sc.nextInt();
        int M = sc.nextInt();
        long result = (long) Math.pow(x, y) % M;
        System.out.println(result);
    }
}
