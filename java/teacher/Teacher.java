package teacher;
public class Teacher {
	private String name;
	private String subject;
	private int age;
	public Teacher(String name, String subject, int age) {
		super();
		this.setName(name);
		this.setSubject(subject);
		this.setAge(age);
	}
	public int getAge() {
		return age;
	}
	public void setAge(int age) {
		this.age = age;
	}
	public String getSubject() {
		return subject;
	}
	public void setSubject(String subject) {
		this.subject = subject;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
}
