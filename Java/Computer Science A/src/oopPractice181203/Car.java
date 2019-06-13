package oopPractice181203;
public class Car {
	public Car(String brand, String color) {
		this.brand = brand;
		this.color = color;
	}
	public String brand;
	public String color;
	public String display() {
		return color+" "+brand;
	}
}
