package circle;
import java.util.Scanner;
import java.lang.Math;
public class Circle {
	
	public static double circleinput() {
		double s=0;
		while(true){
			try{
				System.out.print("The radius is: ");
				Scanner radius=new Scanner(System.in);
				double r=radius.nextDouble();
				s=Math.pow(r,2)*Math.PI;
				radius.close();
				System.out.println("The area is: "+String.format("%.2f", s));
				return s;
			}
			catch(Exception e){
				System.out.println("Error occured. Please try again.\n");
			}
		}
	}
	public static void main(String[] args) {
		circleinput();
	}
}
