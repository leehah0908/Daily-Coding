import java.util.Scanner;
import java.util.Stack;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int N = input.nextInt();
        int[] seq = new int[N];
        for (int i = 0; i < N; i++) {
            seq[i] = input.nextInt();
        }

        StringBuilder sb = new StringBuilder();
        Stack<Integer> stack = new Stack<>();
        int current = 1;
        boolean flag = true;

        for (int i = 0; i < N; i++) {
            int num = seq[i];

            while (current <= num) {
                stack.push(current);
                sb.append("+\n");
                current++;
            }

            if (stack.peek() == num) {
                stack.pop();
                sb.append("-\n");
            } else {
                flag = false;
                break;
            }
        }

        if (flag) {
            System.out.println(sb);
        } else {
            System.out.println("NO");
        }
    }
}
