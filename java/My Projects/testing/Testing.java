package testing;

import java.util.ArrayList;

public class Testing {
	public static String a(String s) {
		System.out.println(s);
		return s;
	}
	public static boolean check(String s) {
		return s.length()>=2 && (s.charAt(0) == s.charAt(1) || check(s.substring(1)));
	}
	public static void main(String[] args) {
		ArrayList<Double> b=new ArrayList<Double>();
		b.add(1.1);
		b.add(2.1);
		b.add(1.3);
		b.add(2.1);
		for (int i=0; i<b.size(); i++) if (b.get(i)==2.1) b.remove(b.get(i));
		System.out.println(b);
		@SuppressWarnings("deprecation")
		Integer a=new Integer(1);
		a.toString();
	}
}
