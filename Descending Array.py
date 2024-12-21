import java.util.*;
public class DescendingArray{
    public static void main(String args[]){
        Scanner sc= new Scanner(System.in);
        int t= sc.nextInt();
        int[] arr = new int[t];
        for(int i = 0; i < t;i++ ){
            arr[i] = sc.nextInt();
        }
     //   System.out.println(Arrays.toString(arr));
     for(int i=1;i<t;i++){
            if(arr[i]>=arr[i-1]){
                System.out.println("no");
                return;
            }
        }
    System.out.println("yes");
    }

}
