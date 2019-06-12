package interfaceCSA;
import java.lang.Math;
public class Bank implements BankInterface {
	private double money;
	public Bank(double deposit) {
		this.money = deposit;
	}
	@Override
	public double deposit(int year) {
		double money = this.money*Math.pow((1+BankInterface.interest), year);
		this.money = money;
		return money;
	}
	@Override
	public void displayMoney() {
		System.out.println(money);
	}

}
