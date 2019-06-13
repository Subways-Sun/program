package test;
import java.util.ArrayList;
public class MockExam {
	public static void manipulate(ArrayList<String> animals) {
		for (int k=animals.size()-1; k>0; k--) {
			if (animals.get(k).substring(0,1).equals("b")) {
				animals.add(animals.size()-k, animals.remove(k));
				System.out.println(animals);
			}
		}
	}
	public static void main(String[]args) {
		ArrayList<String> animals=new ArrayList<String>();
		animals.add("bear");
		animals.add("zebra");
		animals.add("bass");
		animals.add("cat");
		animals.add("koala");
		animals.add("baboon");
		manipulate(animals);
		System.out.print(animals);
	}
}
	
