import java.util.Scanner;
public class Compare{
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        String str1 = sc.nextLine();
        String str2 = sc.nextLine();
        if(str1.equals(str2)){
            System.out.println("Strings are Equal");
        }
        else{
            System.out.println("Strings are not Equal");
        }
       sc.close();  
    }
   
}