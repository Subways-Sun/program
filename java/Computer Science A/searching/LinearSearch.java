package searching;

import java.util.Scanner;

public class LinearSearch {
	public static int Search(int[] a, int b) {
		for (int i=0;i<a.length;i++) if (b==a[i]) return i;
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
