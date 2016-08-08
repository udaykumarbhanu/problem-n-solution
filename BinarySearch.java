
public class BinarySearch {
	// This binary search algorithm is iterative in its nature.
	private static int binarySearchFunc(int array[], int key) {
		int index = -1;
		int low = 0;
		int high = array.length - 1;
		int mid;
		while (high >= low) {
			mid = (low + high) / 2;
			if (array[mid] == key) {
				index = mid;
				return index;
			} else if (array[mid] > key) {
				high = mid - 1;
			} else {
				low = mid + 1;
			}
		}
		return index;

	}

	public static void main(String[] args) {
		int array[] = { 10, 20, 30, 40, 50, 60, 70, 80, 90 };
		int key = 60;
		int res = binarySearchFunc(array, key);

		if (res != -1) {
			System.out.println("Key is found at index: " + (res+1));
		} else {
			System.out.println("Key is NOT found!");
		}
	}

}
