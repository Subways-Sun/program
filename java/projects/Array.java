package projects;
public class Array {
	public static void main(String[] args) {
		/* 1. The sum and average of an array (line 9-20)
		 * 2. The maximum and minimum value of an array (line 22-34)
		 * 3. Count the amount of each number in an array (line 36-56)
		 * 4. Remove the zeros in an array (line 58-77)
		 */
		int[]a=new int[(int)(Math.random()*100)];
		for(int i=0;i<a.length;i++) {
			a[i]=(int)(Math.random()*100+1);
		}
		int sum=0;
		double avg=0;
		int max=Integer.MIN_VALUE;
		int min=Integer.MAX_VALUE;
		for(int each:a) {
			sum=sum+each;
			avg=(double)sum/(double)a.length;
			if(each>max) {
				max=each;
			}
			if(each<min) {
				min=each;
			}
		}
		System.out.println("The sum of the array is: "+sum);
		System.out.println("The average of the array is: "+String.format("%.2f", avg));
		System.out.println("The maximum value is: "+max);
		System.out.println("The minimum value is: "+min);
		System.out.println("");
		
		int[]b=new int[20];
		for(int i=0;i<b.length;i++) {
			b[i]=(int)(Math.random()*10);
		}
		int[]num= {0,0,0,0,0,0,0,0,0,0};
		for(int each:b) {
			for(int i=0;i<10;i++) {
				if(each==i) {
					num[i]++;
				}
			}
		}
		System.out.print("The array is: ");
		for (int each:b) {
			System.out.print(each+" ");
		}
		System.out.println("");
		for(int i=0;i<10;i++) {
			System.out.printf("The number of %d is: ",i);
			System.out.println(num[i]);
		}
		
		int nonZero=0; //Count the number of !0 in order to create array
		for(int each:b) { //int[] b=new int[10]
			if (each!=0) {
				nonZero++;
			}
		}
		int[]d=new int[nonZero];
		int j=-1; //j is given -1 because j++ is before d[j]=b[i]
		for(int i=0;i<b.length;i++) { //Give value of d for each !0 in b
			j++;
			if(b[i]==0) {
				j--;
				continue;
			}
			d[j]=b[i];
		}
		System.out.print("The array without zeros is: ");
		for(int each:d) {
			System.out.print(each+" ");
		}
	}
}
