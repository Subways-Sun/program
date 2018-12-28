package hiddenWord;
public class HiddenWordPackage {
	public String s;
	public HiddenWordPackage(String a) {
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
}
