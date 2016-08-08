
public class RecursiveBinarySearch {
	// Recursive binary search algorithm
	static private int recursiveBinarySearchFunc(int array[], int low, int high, int key) {
		int mid = (low + high) / 2;
		
		if (high < low) {
			return -1;
		}

		if (array[mid] == key) {
			return mid;
		} else if (key < array[mid]) {
			return recursiveBinarySearchFunc(array, low, mid - 1, key);
		} else {
			return recursiveBinarySearchFunc(array, mid + 1, high, key);
		}
	}

	public static void main(String[] args) {
		int array[] = { 10, 20, 30, 40, 50, 60, 70, 80, 90, 100 };
		int key = 70;
		int low = 0;
		int high = array.length - 1;

		int res = recursiveBinarySearchFunc(array, low, high, key);

		if (res != -1) {
			System.out.println("Key is found at index: " + (res + 1));

		} else {
			System.out.println("Key is Not Found");
		}

	}

}
