package notes;
public class Comparison {
	public static void main(String[] args) {
		/*
		 * .equals() is used to compare the value.
		 * == is used to compare the address in memory.
		 * 'new' is used to open a new space in the memory.
		 * Arithmetic Operator + - * /
		 * Logical Operator ! && ||
		 * 		If the logical operator begins with "true||" or "false&&" (the result can be determined), the following code will NOT be executed, EVEN WITH AN ERROR.
		 * Relational Operator == > < >= <=
		 */
		int a=1;
		int b=1;
		System.out.println(a==b);
		//System.out.println(a.equals(b)); Cannot be used, since .equals() can only be used when writing non-basic-variable style such as "Integer".
		String c=new String("aaa"); //Opened a new space in the memory.
		String d=new String("aaa");
		System.out.println(c==d); //The address in memory is different since the use of 'new'.
		System.out.println(c.equals(d));
	}
}
