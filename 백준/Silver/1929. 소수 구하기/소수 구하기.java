import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static int[] isPrime(int M, int N) {
        int[] arr = new int[N + 1];

        for (int i = 2; i <= N; i++) {
            arr[i] = i;
        }

        for (int i = 2; i <= N; i++) {
            if (arr[i] == 0) {
                continue;
            }
            
            for (int j = i + i; j <= N; j += i) {
                arr[j] = 0;
            }
        }
        return arr;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int M = Integer.parseInt(st.nextToken());
        int N = Integer.parseInt(st.nextToken());

        int[] prime = isPrime(M, N);
        for (int i = M; i <= N; i++) {
            if (prime[i] != 0) {
                System.out.println(prime[i]);
            }
        }
    }
}

