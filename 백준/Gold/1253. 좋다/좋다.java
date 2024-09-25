import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int num = input.nextInt();
        int[] arr = new int[num];
        for (int i = 0; i < num; i++) {
            arr[i] = input.nextInt();
        }
        Arrays.sort(arr);

        int start, end, sum, cnt = 0;

        for (int i = 0; i < num; i++) {
            int target = arr[i];
            start = 0;
            end = num - 1;
            while (start < end) {
                if (start == i) {
                    start++;
                    continue;
                }

                if (end == i) {
                    end--;
                    continue;
                }

                sum = arr[start] + arr[end];
                if (target > sum) {
                    start++;
                } else if (target < sum) {
                    end--;
                } else {
                    cnt++;
                    break;
                }
            }
        }
        System.out.println(cnt);
    }
}
