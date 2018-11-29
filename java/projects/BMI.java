package projects;
import java.util.Scanner;
public class BMI {
	public static double calculateBMI() {
		while(true) {
			try {
				System.out.print("Please input your height (in meters): ");
				Scanner input1=new Scanner(System.in);
				double hei=input1.nextDouble();
				System.out.print("Please input your weight (in kilograms): ");
				Scanner input2=new Scanner(System.in);
				double wei=input2.nextDouble();
				double bmi=wei/Math.pow(hei, 2);
				if (bmi<0) {
					System.out.println("Error occured. Please enter a correct number.");
				}
				else {
					System.out.println("Your BMI is: "+String.format("%.2f", bmi));
					if (bmi<16) {
						System.out.println("You are seriously underweight.");
						return bmi;
					}
					else if (bmi<18) {
						System.out.println("You are underweight.");
						return bmi;
					}
					else if (bmi<24) {
						System.out.println("You are at normal weight.");
						return bmi;
					}
					else if (bmi<29) {
						System.out.println("You are overweight.");
						return bmi;
					}
					else if (bmi<35) {
						System.out.println("You are seriously overweight.");
						return bmi;
					}
					else if (bmi>=35) {
						System.out.println("You are gravely overweight.");
						return bmi;
					}
				}
			}
			catch (Exception e) {
				System.out.println("Error occured. Please enter a correct number.\n");
			}
		}
	}
	public static void main(String[] args) {
		calculateBMI();
	}
}
