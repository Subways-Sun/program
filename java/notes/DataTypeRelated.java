package notes;
import java.util.Random;
public class DataTypeRelated {
	/*
	 * 8 numerical data types
	 * byte			8-bit signed
	 * short		16-bit signed (integer)
	 * int			32-bit signed (integer)
	 * long			64-bit signed (integer)
	 * float		32-bit IEEE 754 Single precision decimal
	 * 		When declaring a float, "f" needed to be added to the end of the number
	 * 		Eg：float a=1.2f
	 * double		64-bit IEEE 754 Double precision decimal
	 * Declare 
	 * The level of data types increases from top to bottom
	 * boolean		True/False
	 * char			Single Character
	 * char a='\u1233'; // \u1233 is unicode encoding
	 * String is NOT a basic data type, it is a class
	 */
	/*
	 * java.lang.Math does not need to be imported
	 */
	public static void main(String[] args) {
		int a=(int)3.5; //type narrowing
		int b=4;
		System.out.println(a++); //Rear ++ has the lowest priority
		System.out.println(++a); //Front ++ has the highest priority
		System.out.println(a+++b); //a++ +b
		System.out.println(a+ ++b); //a+ ++b
		System.out.println(a!=b);
		int i=(int)(Math.random()*100);
		System.out.println(i);
		Random j=new Random();
		int k=j.nextInt(10);
		System.out.println("k="+k);
	}
}
