package searching;
import java.util.Scanner;
public class BinarySearch {
	public static int Search(int[] a, int b) {
		int hi=a.length-1;
		int lo=0;
		int mid=(hi-lo)/2;
		for (int i=1; i<a.length+1; i++) {
			if (b<a[mid]) {
				hi=mid;
				mid=lo+(hi-lo)/2;
			}
			if (b>a[mid]) {
				lo=mid;
				mid=lo+(hi-lo)/2;
			}
			if (b==a[mid]) {
				return mid;
			}
		}
		return -1;
	}
	public static void main(String[] args) {
		Scanner a=new Scanner(System.in);
		System.out.print("Enter the array: ");
		String b=a.next();
		String split="";
		int i=0;
		try {
			for (i=0; i<b.length(); i++) {
				Integer.parseInt(b.substring(i,i+1));
			}
		}
		catch(Exception e) {
			split=b.substring(i,i+1);
		}
		String[] s=b.split(split);
		int[] e=new int[s.length];
		for (int j=0; j<s.length; j++) e[j]=Integer.parseInt(s[j]);
		Scanner c=new Scanner(System.in);
		System.out.print("Enter the integer: ");
		int d=c.nextInt();
		if (Search(e,d)>=0) System.out.print("The index of "+d+" is "+Search(e,d)+".");
		else System.out.print("The integer "+d+" is not in the array.");
		a.close();
		c.close();
	}
}
