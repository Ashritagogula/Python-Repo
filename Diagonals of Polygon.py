import java.util.Scanner;
public class Diagonals{
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        int n=sc.nextInt();
        int r=(n*(n-3))/2;
        System.out.println(r);
    }
}