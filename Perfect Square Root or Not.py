import java.util.Scanner;

public class PerfectSquare {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.close();
        int res = (int) Math.sqrt(n);
        boolean isPerfect = res * res == n;
        if (isPerfect) {
            System.out.println("True");
        } else {
            System.out.println("False");
        }
    }
}