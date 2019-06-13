package interfaceCSA;
public class ClientProgram {
	public static void main(String[] args) {
		Bank a = new Bank(30000);
		a.deposit(3);
		a.displayMoney();
	}
}
