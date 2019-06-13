package sort;
import java.util.ArrayList;
import java.util.Scanner;
public class InsertionSort {
	public static int[] Sort(int[] a) {
		ArrayList<Integer> b=new ArrayList<Integer>();
		for (int x:a) b.add(x);
		for (int i=1; i<b.size(); i++) { 
			for (int j=0; j<i; j++) {
				if (b.get(i)<=b.get(j)) {
					int temp=b.get(i);
					b.remove(i);
					b.add(j,temp);
				}
			}
		}
		int[] c=new int[a.length];
		for (int i=0; i<c.length; i++) c[i]=b.get(i);
		return c;
	}
	public static void main(String[] args) {
		System.out.println("----Insertion Sort----");
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
