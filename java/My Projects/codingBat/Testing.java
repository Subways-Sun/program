package codingBat;
import java.util.ArrayList;
public class Testing {
	public static void main(String[] args) {
		String str="yakpak";
		String a="";
		ArrayList<Integer> posi=new ArrayList<Integer>();
		for (int i=0;i<str.length()-2;i++){
			if (str.substring(i,i+3).equals("yak")){
				i+=2;
				continue;
				}
			posi.add(i);
		}
		if ((posi.get(posi.size()-1)<str.length()-1)&&(!(str.substring(str.length()-3).equals("yak")))){
			posi.add(str.length()-2);
			posi.add(str.length()-1);
		}
		System.out.println(posi);
		for (int every:posi){
			a+=str.substring(every,every+1);
		}
		System.out.println(a);
	}
}
