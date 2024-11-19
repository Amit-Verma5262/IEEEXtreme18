package IncreasingTable;
import java.util.*;
import java.io.*;

public class Main {
    static final int MOD = 998244353;
    static int totalSteps;
    static int[] stepValues; 
    static int[][] dpTable;

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        totalSteps = Integer.parseInt(reader.readLine());
        stepValues = new int[2 * totalSteps];

        Arrays.fill(stepValues, 0);
        StringTokenizer tokenizer;

        tokenizer = new StringTokenizer(reader.readLine());
        int setASize = Integer.parseInt(tokenizer.nextToken());
        Set<Integer> setA = new HashSet<>();
        for (int i = 0; i < setASize; i++) {
            int num = Integer.parseInt(tokenizer.nextToken());
            setA.add(num);
        }

        tokenizer = new StringTokenizer(reader.readLine());
        int setBSize = Integer.parseInt(tokenizer.nextToken());
        Set<Integer> setB = new HashSet<>();
        for (int i = 0; i < setBSize; i++) {
            int num = Integer.parseInt(tokenizer.nextToken());
            setB.add(num);
        }

        for (int pos = 0; pos < 2 * totalSteps; pos++) {
            int num = pos + 1; 
            if (setA.contains(num)) {
                stepValues[pos] = 1; 
            } else if (setB.contains(num)) {
                stepValues[pos] = -1; 
            }
        }

        dpTable = new int[2 * totalSteps + 1][totalSteps + 1];
        dpTable[0][0] = 1;

        for (int pos = 0; pos < 2 * totalSteps; pos++) {
            for (int openSteps = 0; openSteps <= totalSteps; openSteps++) {
                int currentValue = dpTable[pos][openSteps];
                if (currentValue == 0) continue;

                int upSteps = (pos + openSteps) / 2;
                int downSteps = pos - upSteps;
                if (upSteps > totalSteps || downSteps > totalSteps) continue;

                if (stepValues[pos] != 0) {
                    if (stepValues[pos] == 1) { 
                        if (openSteps + 1 <= totalSteps && upSteps + 1 <= totalSteps) {
                            dpTable[pos + 1][openSteps + 1] = (dpTable[pos + 1][openSteps + 1] + currentValue) % MOD;
                        }
                    } else { 
                        if (openSteps - 1 >= 0 && downSteps + 1 <= totalSteps) {
                            dpTable[pos + 1][openSteps - 1] = (dpTable[pos + 1][openSteps - 1] + currentValue) % MOD;
                        }
                    }
                } else {
                    if (openSteps + 1 <= totalSteps && upSteps + 1 <= totalSteps) {
                        dpTable[pos + 1][openSteps + 1] = (dpTable[pos + 1][openSteps + 1] + currentValue) % MOD;
                    }
                    if (openSteps - 1 >= 0 && downSteps + 1 <= totalSteps) {
                        dpTable[pos + 1][openSteps - 1] = (dpTable[pos + 1][openSteps - 1] + currentValue) % MOD;
                    }
                }
            }
        }

        System.out.println(dpTable[2 * totalSteps][0]);
    }
}