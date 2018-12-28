package testing;
public class Testing {
	public static String a(String s) {
		System.out.println(s);
		return s;
	}
	public static boolean check(String s) {
		return s.length()>=2 && (s.charAt(0) == s.charAt(1) || check(s.substring(1)));
	}
	public static void main(String[] args) {
		System.out.println(check(a("abcdefgghij")));
	}
}
