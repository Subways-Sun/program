package oopPractice181203;
public class Testing {
	public static void main(String[] args) {
		People zhangsan = new People("张三", "富二代", "李四");
		Car bentley = new Car("宾利", "白色");
		zhangsan.show(zhangsan.girlfriend, bentley.display());
	}
}
