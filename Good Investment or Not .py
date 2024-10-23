import java.util.Scanner;
public class InvestmentCheck {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();
        String[] values = input.split(" ");
        int X = Integer.parseInt(values[0]); 
        int Y = Integer.parseInt(values[1]); 
        if (X >= 2 * Y) {
            System.out.println("YES");
        } else {
            System.out.println("NO");
        }
        
        scanner.close();
    }
}