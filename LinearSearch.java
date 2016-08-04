public class LinearSearch {

	private static int linearSearchFun(int array[], int low, int high, int key) {
		if (low > high) {
			System.out.println("Array indices passed is not correct!");
			return -99;
		} else {
			for (int i = low; i < high; i++) {
				if (array[i] == key) {
					return i + 1;
				}
			}
		}
		return -1;
	}

	public static void main(String[] args) {
		int array[] = { 10, 20, 30, 40, 50, 60 };
		int key = 50;
		int index = linearSearchFun(array, 10, array.length, key);
		if (index == -1) {
			System.out.println("Key is NOT found!");

		} else if (index>=0) {
			System.out.println("Key is found at: " + index);
		}
	}

}
