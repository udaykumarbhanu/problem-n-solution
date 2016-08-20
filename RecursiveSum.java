
public class RecursiveSum {

	private static int sum(int num) {
		if (num <= 0) {
			return 0;
		}
		return num + sum(num - 1);
	}

	public static void main(String[] args) {
		int n = 4;
		int res = sum(n);
		System.out.println("Result is " + res);
	}

}
