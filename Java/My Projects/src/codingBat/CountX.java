package codingBat;
public class CountX {
	public static void main(String[] args) {
		String str="xxHHxHxx";
		String s=str.substring(0,1);
		for (int i=1;i<=str.length()-2;i++) {
			System.out.println(str.substring(i,i+1));
			if (str.substring(i,i+1).equals("x")) continue;
			s+=str.substring(i,i+1);
			System.out.println(s);
			System.out.println();
		}
		s+=str.substring(str.length()-1);
	}
}
