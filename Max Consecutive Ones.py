/*import java.util.*;
public class MaxOnes{
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        
        int[] arr = new int[t];
        for(int i=0; i <t;i++){
            arr[i] = sc.nextInt();
        }
        for(int i=0;i<t;i++){
            int c=0;
            if(arr[i]=='1' && arr[i+1]=='1'){
                c++;
            }
            if(arr[i]==0){
                break;
            }  
            System.out.println(c); 
        }
        
    }
}*/
import java.util.Scanner;

public class MaxOnes {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        int[] arr = new int[t];
        for (int i = 0; i < t; i++) {
            arr[i] = sc.nextInt();
        }
        int c = 0, max = 0;
        for (int i = 0; i < t; i++) {
            if (arr[i] == 1) {
                c++;
                if (c > max) {
                    max = c;
                }
            }
            if (arr[i] == 0) {
                c = 0;
            }
        }
        System.out.println(max);
    }
}