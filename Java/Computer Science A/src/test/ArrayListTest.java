package test;
public class ArrayListTest {
	public static void strRe(String s) {
		if (s.length()<16) {
			System.out.println(s);
		}
		strRe(s+"*");
	}
	public static void main(String[] args) {
		strRe("asdhdhfjakdlasdjdlasdsakda");
	}
}
