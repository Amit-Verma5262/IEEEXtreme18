import java.util.Arrays;
import java.util.Scanner;

public class Digit {

    public static int[] swapDigits(int[] digitArray, int swapTimes) {
        int count = 0; // Count for how many times we swap
        int[] sortedDigitArray = digitArray.clone(); // Clone the original array
        Arrays.sort(sortedDigitArray); // Sort the array in ascending order
        reverseArray(sortedDigitArray); // Reverse it to get descending order

        for (int i = 0; i < digitArray.length; i++) {
            if (count == swapTimes) {
                break;
            } else if (digitArray[i] == sortedDigitArray[i]) {
                // If the value is already in the correct position
                continue;
            } else {
                // Get the indices where the current maximum value appears
                int j = findRightmostIndex(digitArray, sortedDigitArray[i]);
                
                // Only swap if the indices are different
                if (i != j) {
                    // Swap values
                    int temp = digitArray[i];
                    digitArray[i] = digitArray[j];
                    digitArray[j] = temp;
                    count++;
                }
            }
        }
        return digitArray;
    }

    // Method to reverse an array
    public static void reverseArray(int[] array) {
        int left = 0;
        int right = array.length - 1;
        while (left < right) {
            int temp = array[left];
            array[left] = array[right];
            array[right] = temp;
            left++;
            right--;
        }
    }

    // Method to find the rightmost index of the value in the array
    public static int findRightmostIndex(int[] array, int value) {
        for (int i = array.length - 1; i >= 0; i--) {
            if (array[i] == value) {
                return i;
            }
        }
        return -1; // This shouldn't happen if the value exists
    }

    public static void main(String[] args) {
        // Get input setups
        Scanner scanner = new Scanner(System.in);
        String[] valueAndSwap = scanner.nextLine().split(" ");
        String value = valueAndSwap[0]; // str
        int swap = Integer.parseInt(valueAndSwap[1]); // swap is the value to be swapped

        int[] digitArray = new int[value.length()]; // Create an array of integers
        for (int i = 0; i < value.length(); i++) {
            digitArray[i] = Character.getNumericValue(value.charAt(i)); // Convert to an array of integers
        }

        // Swap the value in the array
        int[] result = swapDigits(digitArray, swap);

        // Print the result
        for (int i : result) {
            System.out.print(i);
        }
        scanner.close();
    }
}