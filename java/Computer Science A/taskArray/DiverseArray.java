package taskArray;
public class DiverseArray {
	public static int arraySum(int[] arr) {
		int sum=0;
		for (int i:arr) sum+=i;
		return sum;
	}
	public static int[] rowSums(int[][] arr2D) {
		int[] sum=new int[arr2D.length];
		for (int i=0; i<arr2D.length; i++) sum[i]=arraySum(arr2D[i]);
		return sum;
	}
	public static boolean isDiverse(int[][] arr2D) {
		int[] rowSums=rowSums(arr2D);
		for (int i=0; i<arr2D.length; i++) {
			int temp=rowSums[i];
			for (int j=i+1; j<arr2D.length; j++) if (rowSums[j]==temp) return false;
		}
		return true;
	}
}
