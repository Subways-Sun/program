package projects;
import java.util.Scanner;
public class TwoDimentionalArray2 {
	public static void main(String[] args) {
		//The First Figure
		char[][]a=new char[4][4];
		for (int i=0;i<a.length;i++) {
			for (int j=0;j<a[i].length;j++) {
				for (int k=0;k<=i;k++) {
					a[i][k]='*';
				}
			}
		}
		for (char[]row:a) {
			for (char column:row) {
				System.out.print(column);
			}
			System.out.println();
		}
		System.out.println();
		//The Second Figure
		char[][]b=new char[4][4];
		for (int i=0;i<b.length;i++) {
			for (int j=0;j<b[i].length;j++) {
				for (int k=3;k>=i;k--) {
					b[i][k]='*';
				}
			}
		}
		for (char[]row:b) {
			for (char column:row) {
				System.out.print(column);
			}
			System.out.println();
		}
		System.out.println();
		//The Third Figure
		char[][]c=new char[4][4];
		for (int i=0;i<c.length;i++) {
			for (int j=0;j<c[i].length;j++) {
				for (int k=3;k>=i-2;k--) {
					if(k<0) {
						break;
					}
					c[i][k]=' ';
				}
				for (int k=3;k>=3-i;k--) {
					c[i][k]='*';
				}
			}
		}
		for (char[]row:c) {
			for (char column:row) {
				System.out.print(column);
			}
			System.out.println();
		}
		System.out.println();
		//The Fourth Figure
		char[][]d=new char[4][4];
		for (int i=0;i<d.length;i++) {
			for (int j=0;j<d[i].length;j++) {
				for (int k=0;k<=i-1;k++) {
					d[i][k]=' ';
				}
				for (int k=3;k>=i;k--) {
					d[i][k]='*';
				}
			}
		}
		for (char[]row:d) {
			for (char column:row) {
				System.out.print(column);
			}
			System.out.println();
		}
		System.out.println();
		//Christmas Tree
		System.out.print("Please input the number of floors: ");
		Scanner in=new Scanner(System.in);
		int num=in.nextInt();
		char[][]e=new char[num][2*num-1];
		for (int i=0;i<e.length;i++) {
			for (int j=0;j<e[i].length;j++) {
				for (int k=(e[i].length-1)/2-1;k>=0;k--) {
					if(k<0) {
						break;
					}
					e[i][k]=' ';
				}
				for (int k=(e[i].length-1)/2+1;k<=e.length;k++) {
					e[i][k]=' ';
				}
				for (int k=(e[i].length-1)/2-i;k<=(e[i].length-1)/2+i;k++) {
					e[i][k]='*';
				}
			}
		}
		for (char[]row:e) {
			for (char column:row) {
				System.out.print(column);
			}
			System.out.println();
		}
		for (int i=0;i<num-2;i++) {
			System.out.print(" ");
		}
		System.out.print("***");
		System.out.println();
		System.out.println();
		
		//Multiplication Table
		int[]multi= {1,2,3,4,5,6,7,8,9};
		for (int i=0;i<9;i++) {
			for (int j=0;j<=i;j++) {
				System.out.printf("%dx%d=%d",multi[j],multi[i],multi[i]*multi[j]);
				System.out.print(" ");
			}
			System.out.println();
		}
		//Rhombus
		System.out.print("Please input the number of floors: ");
		Scanner in2=new Scanner(System.in);
		int num2=in2.nextInt();
		char[][]f=new char[2*num2-1][2*num2-1];
		for (int i=0;i<f.length;i++) {
			for (int j=0;j<(f[i].length-1)/2;j++) {
				for (int k=(f[i].length-1)/2-1;k>=0;k--) {
					if(k<0) {
						break;
					}
					f[i][k]=' ';
				}
				for (int k=(f[i].length-1)/2+1;k<f[i].length;k++) {
					f[i][k]=' ';
				}
				for (int k=(f[i].length-1)/2-i;k<=(f[i].length-1)/2+i;k++) {
					f[i][k]='*';
				}
			}
			for (int j=(f.length-1)/2;j<f.length;j++) {
				for (int k=0;k<=i-(f[i].length-1)/2;k++) {
					f[i][k]=' ';
				}
				for (int k=(f[i].length-1)/2-1;k>=(f[i].length-1)/2;k--) {
					if(k<0) {
						break;
					}
					f[i][k]=' ';
				}
				for (int k=i-(f[i].length-1)/2;k<=(f[i].length-1)/2+i;k++) {
					f[i][k]='*';
				}
			}
		}
		for (char[]row:f) {
			for (char column:row) {
				System.out.print(column);
			}
			System.out.println();
		}
		in.close();
		in2.close();
	}
}
