package BoundedTuples;

import java.util.*;
import java.io.*;

public class Main {
    static int numVariables, numConstraints;
    static long MOD = 998244353;
    static Constraint[] constraints;
    static long solutionCount = 0;
    static long[] lowerBounds, upperBounds;

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokenizer = new StringTokenizer(reader.readLine());

        numVariables = Integer.parseInt(tokenizer.nextToken());
        numConstraints = Integer.parseInt(tokenizer.nextToken());

        lowerBounds = new long[numVariables];
        upperBounds = new long[numVariables];
        Arrays.fill(lowerBounds, 0);
        Arrays.fill(upperBounds, Long.MAX_VALUE / 2);

        constraints = new Constraint[numConstraints];
        boolean[] isBounded = new boolean[numVariables];
        Arrays.fill(isBounded, false);

        for (int i = 0; i < numConstraints; i++) {
            tokenizer = new StringTokenizer(reader.readLine());
            long lowBound = Long.parseLong(tokenizer.nextToken());
            long highBound = Long.parseLong(tokenizer.nextToken());
            int numIndices = Integer.parseInt(tokenizer.nextToken());
            int[] indices = new int[numIndices];
            for (int j = 0; j < numIndices; j++) {
                indices[j] = Integer.parseInt(tokenizer.nextToken()) - 1;
            }
            constraints[i] = new Constraint(lowBound, highBound, indices);
            if (highBound != Long.MAX_VALUE) {
                for (int idx : indices) {
                    isBounded[idx] = true;
                }
            }
        }

        boolean hasInfiniteSolution = false;
        for (int i = 0; i < numVariables; i++) {
            if (!isBounded[i]) {
                hasInfiniteSolution = true;
                break;
            }
        }

        if (hasInfiniteSolution) {
            System.out.println("infinity");
            return;
        }

        List<long[]> variableRanges = precomputeVariableRanges();

        depthFirstSearch(0, new long[numVariables], variableRanges);
        System.out.println(solutionCount % MOD);
    }

    static List<long[]> precomputeVariableRanges() {
        List<long[]> variableRanges = new ArrayList<>();
        for (int i = 0; i < numVariables; i++) {
            long minVal = lowerBounds[i];
            long maxVal = upperBounds[i];

            for (Constraint constraint : constraints) {
                if (contains(constraint.indices, i)) {
                    int numVarsInConstraint = constraint.indices.length;
                    long minSumOtherVars = 0;
                    long maxSumOtherVars = 0;
                    for (int idx : constraint.indices) {
                        if (idx != i) {
                            minSumOtherVars += lowerBounds[idx];
                            maxSumOtherVars += upperBounds[idx];
                        }
                    }
                    long minPossibleValue = Math.max(lowerBounds[i], constraint.lowBound - maxSumOtherVars);
                    long maxPossibleValue = Math.min(upperBounds[i], constraint.highBound - minSumOtherVars);
                    minVal = Math.max(minVal, minPossibleValue);
                    maxVal = Math.min(maxVal, maxPossibleValue);
                }
            }

            if (minVal > maxVal) {
                // No possible assignment for variable i
                System.out.println(0);
                System.exit(0);
            }

            variableRanges.add(new long[]{minVal, maxVal});
        }
        return variableRanges;
    }

    static void depthFirstSearch(int idx, long[] assignment, List<long[]> variableRanges) {
        if (idx == numVariables) {
            if (checkConstraints(assignment)) {
                solutionCount = (solutionCount + 1) % MOD;
            }
            return;
        }

        long minVal = variableRanges.get(idx)[0];
        long maxVal = variableRanges.get(idx)[1];

        for (long val = minVal; val <= maxVal; val++) {
            assignment[idx] = val;
            if (isPossibleSoFar(idx, assignment)) {
                depthFirstSearch(idx + 1, assignment, variableRanges);
            }
        }
    }

    static boolean isPossibleSoFar(int idx, long[] assignment) {
        for (Constraint constraint : constraints) {
            long sumAssigned = 0;
            long sumUnassignedMin = 0;
            long sumUnassignedMax = 0;
            boolean relevantConstraint = false;

            for (int varIdx : constraint.indices) {
                if (varIdx <= idx) {
                    sumAssigned += assignment[varIdx];
                    relevantConstraint = true;
                } else {
                    sumUnassignedMin += lowerBounds[varIdx];
                    sumUnassignedMax += upperBounds[varIdx];
                }
            }

            if (relevantConstraint) {
                long possibleSumMin = sumAssigned + sumUnassignedMin;
                long possibleSumMax = sumAssigned + sumUnassignedMax;
                if (possibleSumMax < constraint.lowBound || possibleSumMin > constraint.highBound) {
                    return false;
                }
            }
        }
        return true;
    }

    static boolean checkConstraints(long[] assignment) {
        for (Constraint constraint : constraints) {
            long sum = 0;
            for (int idx : constraint.indices) {
                sum += assignment[idx];
            }
            if (sum < constraint.lowBound || sum > constraint.highBound) {
                return false;
            }
        }
        return true;
    }

    static boolean contains(int[] arr, int val) {
        for (int x : arr) {
            if (x == val) return true;
        }
        return false;
    }

    static class Constraint {
        long lowBound, highBound;
        int[] indices;

        Constraint(long lowBound, long highBound, int[] indices) {
            this.lowBound = lowBound;
            this.highBound = highBound;
            this.indices = indices;
        }
    }
}