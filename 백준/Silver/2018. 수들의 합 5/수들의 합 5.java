import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int N = input.nextInt();

        int start = 0, end = 0, sum = 1, count = 0;
        int[] array = new int[N];

        for (int i = 0; i < N; i++) {
            array[i] = i + 1;
        }

        while (end < N) {
            if (sum == N) {
                count++;
                end++;
                if (end < N) {
                    sum += array[end];
                }
            } else if (sum > N) {
                sum -= array[start++];
            } else {
                sum += array[++end];
            }
        }
        System.out.println(count);
    }
}