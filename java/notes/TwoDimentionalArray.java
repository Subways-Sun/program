package notes;
public class TwoDimentionalArray {
	public static void main(String[] args) {
		int[][]a=new int[10][6]; //Ten rows, six columns
		for (int i=0;i<a.length;i++) { //a.length means the number of rows
			for (int j=0;j<a[i].length;j++) { //a[i].length means the number of columns (numbers) in each row
				a[i][j]=i+j;
				System.out.print(a[i][j]);
			}
			System.out.println();
		}
		int[][]b= {{1,2,3,4},{6,5,4},{9},{8,0}}; //Each {} means a row
		for (int [] row:b) {
			for (int column:row) {
				System.out.println(column);
			}
			System.out.println();
		}
	}
}
