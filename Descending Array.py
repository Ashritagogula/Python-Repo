import java.util.Scanner;
public class DescendingArray {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        if (n == 0) {
            System.out.println("yes");
            return;
        }
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = scanner.nextInt();
        }
        for (int i = 1; i < n; i++) {
            if (arr[i] >= arr[i - 1]) {
                System.out.println("no");
                return;
            }
        }
        System.out.println("yes");
    }
}