import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int num = input.nextInt();
        int target = input.nextInt();
        int[] arr = new int[num];
        for (int i = 0; i < num; i++) {
            arr[i] = input.nextInt();
        }
        Arrays.sort(arr);

        int start = 0, end = num - 1, sum, cnt = 0;

        while (start < end) {
            sum = arr[start] + arr[end];
            if (target > sum) {
                start++;
            } else if (target < sum) {
                end--;
            } else {
                cnt++; start++; end--;
            }
        }
        System.out.println(cnt);
    }
}
