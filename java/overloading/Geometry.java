package overloading;
public class Geometry {
	public double perimeter(int r, double pi) { //circle
		double perimeter=2*r*pi;
		return perimeter;
	}
	public int perimeter(int a) { //square
		int perimeter=4*a;
		return perimeter;
	}
	public int perimeter(int a, int b) { //rectangle
		int perimeter=2*(a+b);
		return perimeter;
	}
	public double area(int r, double pi) { //circle
		double area=r*r*pi;
		return area;
	}
	public int area(int a) { //square
		int area=a*a;
		return area;
	}
	public int area(int a, int b) { //rectangle
		int area=a*b;
		return area;
	}
}
