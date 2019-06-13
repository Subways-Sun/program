package notes;
public class StringNotes {
	public static void main(java.lang.String[] args) {
		String a=",1,2,3,4,5,6,7,8,9,10,";
		String[] b=a.split(",",1000);
		for (String x:b) {
			System.out.println(x);
		}
		System.out.println("stop");
	}
}
