import java.util.Scanner;
public class Palindrome{
    public static void main(String args[]){
        Scanner read=new Scanner(System.in);
        String n=read.nextLine();
        int start=0;
        int end=n.length()-1;
        boolean isPalindrome=true;
        while(start<end){
            char leftChar=Character.toLowerCase(n.charAt(start));
            char rightChar=Character.toLowerCase(n.charAt(end));
            if(leftChar!=rightChar){
                isPalindrome=false;
                break;
            }
            start++;
            end--;
        }
        if(isPalindrome){
            System.out.println("Palindrome");
        }
        else{
            System.out.println("Not Palindrome");
        }
        read.close();
    }
}