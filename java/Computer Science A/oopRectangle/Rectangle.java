package oopRectangle;
public class Rectangle {
	private int width;
	private int height;
	public Rectangle() {
		width=1;
		height=1;
	}
	public Rectangle(int a) {
		width=a;
		height=a;
	}
	public Rectangle(int a, int b) {
		width=a;
		height=b;
	}
	public void setWidth(int a) {
		width=a;
	}
	public void setHeight(int a) {
		height=a;
	}
	public int getWidth() {
		return width;
	}
	public int getHeight() {
		return height;
	}
	public int getCircumference() {
		return 2*(width+height);
	}
	public int getArea() {
		return width*height;
	}
}
