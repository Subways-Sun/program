package hiddenWord;
public class HiddenWord {
	public String s;
	public HiddenWord(String a) {
		s=a;
	}
	public void getHint(String a) {
		String x="";
		for (int i=0;i<s.length();i++) {
			if (s.indexOf(a.charAt(i))==-1) x+="*";
			else if (s.indexOf(a.charAt(i),i)==i) x+=a.charAt(i);
			else if (!(s.indexOf(a.charAt(i))==i)) x+="+";
		}
		System.out.println(x);
	}
	public static void main(String[] args) {
		HiddenWord a=new HiddenWord("HARPS");
		a.getHint("AAAAA");
		a.getHint("HELLO");
		a.getHint("HEART");
		a.getHint("HARMS");
		a.getHint("HARPS");
	}
}
