package overloading;
public class Testing {
	public static void main(String[] args) {
		Geometry a=new Geometry();
		System.out.println(a.perimeter(3, 3.14));//circle
		System.out.println(a.perimeter(2));//square
		System.out.println(a.perimeter(2, 3));//rectangle
		System.out.println(a.area(3, 3.14));//circle
		System.out.println(a.area(2));//square
		System.out.println(a.area(2, 3));//rectangle
	}
}
