import java.util.Scanner;
public class GradesCalculator {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int marks1 = sc.nextInt();
        int marks2 = sc.nextInt();
        int marks3 = sc.nextInt();
        int marks4 = sc.nextInt();
        int marks5 = sc.nextInt();
        int totalMarks = marks1 + marks2 + marks3 + marks4 + marks5;
        double percentage = (totalMarks / 5.0);
        if (percentage >= 90) System.out.println("Grade A");
        else if (percentage >= 80) System.out.println("Grade B");
        else if (percentage >= 70) System.out.println("Grade C");
        else if (percentage >= 60) System.out.println("Grade D");
        else if (percentage >= 40) System.out.println("Grade E");
        else System.out.println("Grade F");
    }
}