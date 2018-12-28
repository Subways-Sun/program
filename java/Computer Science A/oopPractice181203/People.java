package oopPractice181203;
public class People {
	public People(String name, String wealthLevel) {
		this.name = name;
		this.wealthLevel = wealthLevel;
	}
	public People(String name, String wealthLevel, String girlfriend) {
		this.name = name;
		this.wealthLevel = wealthLevel;
		this.girlfriend = girlfriend;
	}
	public String name;
	public String wealthLevel;
	public String girlfriend;
	public void show(String name2, String item) {
		System.out.printf("成功向 %s 展示了 %s", name2, item);
	}
}
