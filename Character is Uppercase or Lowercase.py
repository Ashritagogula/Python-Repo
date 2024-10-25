import java.util.Scanner;
public class CheckingCase{
    public static void main(String args[]){
        Scanner sc=new Scanner(System.in);
        char ch= sc.next().charAt(0);
        if(ch>='a' && ch<='z'){
            System.out.println("lowercase alphabet");
        }
        else if(ch>='A' && ch<='Z'){
            System.out.println("uppercase alphabet");
        }
        else{
            System.out.println("not an alphabet");
        }
    }
}