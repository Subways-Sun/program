package sort;
import java.util.Scanner;
public class SelectionSort {
	public static int[] Sort(int[] a) {
		for (int i=0;i<a.length;i++) {
			int minIndex=i;
			for (int j=i;j<a.length;j++) if (a[j]<a[minIndex]) minIndex=j;
			int temp=a[minIndex];
			a[minIndex]=a[i];
			a[i]=temp;
			System.out.println(i);
			if (i==a.length-2) return a;
		}
		return a;
	}
	public static void main(String[] args) {
		System.out.println("----Selection Sort----");
		Scanner s=new Scanner(System.in);
		System.out.print("Enter your array (split each number with a comma): ");
		String b=s.next();
		String[] c=b.split(",");
		int[] a=new int[c.length];
		for (int i=0;i<a.length;i++) {
			a[i]=Integer.parseInt(c[i]);
		}
		a=Sort(a);
		System.out.print("The new array is: ");
		System.out.print(a[0]);
		for (int i=1;i<a.length;i++) System.out.print(","+a[i]);
		s.close();
	}
}
