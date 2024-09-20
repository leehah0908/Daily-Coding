import java.util.Arrays;
import java.util.Scanner;
import java.util.Stack;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        char[][] arr = new char[5][];
        String tempStr;
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < arr.length; i++) {
            tempStr = input.nextLine();
            char[] charArr = tempStr.toCharArray();
            arr[i] = charArr;
        }

        for (int i = 0; i < 15; i++) {
            for (int j = 0; j < arr.length; j++) {
                try {
                    sb.append(arr[j][i]);
                } catch (Exception e) {
                }
            }
        }
        System.out.println(sb);
    }
}

