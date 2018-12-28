package notes;
import java.util.ArrayList;
public class Array_List {
	public static void main(String[] args) {
		/*
		 * Static array
		 * 1. Fixed length
		 * 2. Can only contain one type of data type
		 */
		ArrayList<Object> b=new ArrayList<Object>();
		b.add(1);
		b.add(2.3);
		b.add(true);
		b.add("hello");
		b.set(1, 3);
		b.add(2, 56);
		b.remove(1);//Removes object of index 1
		b.remove(true);//Removes object "true"
		for(int i=0;i<b.size();i++) {
			/*
			 * Length of each data type
			 * ArrayList.size()
			 * Array.length
			 * String.length()
			 */
			System.out.println(b.get(i));
		}
		for(Object o:b) {//Object should be used
			System.out.println(o);
		}
	}
}
