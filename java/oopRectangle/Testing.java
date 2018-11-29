package oopRectangle;
public class Testing {
	public static void main(String[] args) {
		Rectangle a=new Rectangle();
		System.out.println("The circumference of rectangle a is: "+a.getCircumference());
		System.out.println("The area of rectangle a is: "+a.getArea());
		Rectangle b=new Rectangle(5);
		System.out.println("The circumference of rectangle b is: "+b.getCircumference());
		System.out.println("The area of rectangle b is: "+b.getArea());
		Rectangle c=new Rectangle(5,7);
		System.out.println("The circumference of rectangle c is: "+c.getCircumference());
		System.out.println("The area of rectangle c is: "+c.getArea());
	}
}
