package projects;
public class TwoDimentionalArray {
	public static void main(String[] args) {
		int rdx=(int)(Math.random()*100);
		int rdy=(int)(Math.random()*100);
		int[][]a=new int[rdx][rdy];
		for (int i=0;i<a.length;i++) {
			for (int j=0;j<a[i].length;j++) {
				a[i][j]=(int)(Math.random()*100);
			}
		}
		int sum=0;
		int count=0;
		int max=Integer.MIN_VALUE;
		int min=Integer.MAX_VALUE;
		System.out.println("The array is: ");
		for (int [] row:a) {
			for (int column:row) {
				sum=sum+column;
				++count;
				if (column>max) {
					max=column;
				}
				if (column<min) {
					min=column;
				}
				System.out.print(column+" ");
			}
			System.out.println();
		}
		double avg=(double)sum/(double)count;
		System.out.println("The sum is: "+sum);
		System.out.println("The average is: "+String.format("%.2f",avg));
		System.out.println("The minimum value is: "+max);
		System.out.println("The maximum value is: "+min);
	}
}
