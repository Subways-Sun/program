package guessNumber;
import java.util.Random;
import java.util.Scanner;
public class GuessNumber {
	public static void guess() {
		System.out.println("----------Game Started----------");
		Random a=new Random();
		int rand=a.nextInt(100);
		System.out.println(rand);
		System.out.print("Please guess a number: ");
		while(true) {
			try{
				Scanner b=new Scanner(System.in);
				int input=b.nextInt();
				if(input>rand) {
					System.out.print("Your guess is too large, please try again: ");
				}
				else if(input<rand) {
					System.out.print("Your guess is too small, please try again: ");
				}
				else if(input==rand) {
					System.out.print("--------Congratulations!--------");
					break;
				}
			}
			catch(Exception e) {
				System.out.print("Error occured. Please enter a integar: ");
			}
		}
	}
	public static void main(String[] args) {
		guess();
	}
}
